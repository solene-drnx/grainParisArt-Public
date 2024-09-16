from bs4 import BeautifulSoup
import requests
import requests_cache
from datetime import timedelta
from modules.firebase import enregistrementFilm, recupererDataFilm


requests_cache.install_cache('film_cache', expire_after=timedelta(minutes=5))

# Récolte les données
def scrap_infoFilm(url, cinema):
    films = []
    response = requests.get(url)
    reponse_text = response.text
    soupReponse = BeautifulSoup(reponse_text, 'html.parser')

    # films_list = soupReponse.find('div', class_="showtimes-list-holder").find_all('div', class_="card entity-card entity-card-list movie-card-theater cf hred")
    films_list_container = soupReponse.find('div', class_="showtimes-list-holder")
    if films_list_container:
        films_list = films_list_container.find_all('div', class_="card entity-card entity-card-list movie-card-theater cf hred")
        for film in films_list:
            titre = film.find("div", class_="meta").find('h2', class_="meta-title").find("a").get_text()
            realisateur_section = film.find("div", class_="meta-body-item meta-body-direction")

            if realisateur_section:
                realisateur = realisateur_section.find('span', class_="dark-grey-link").get_text()
            else:
                realisateur = "Réalisateur non trouvé"

            dataFilm_firebase = recupererDataFilm(titre, realisateur)
            if dataFilm_firebase == 0:
                # Extraction de l'image
                thumbnail_img = film.find('img', class_='thumbnail-img')
                if thumbnail_img and not thumbnail_img['src'].startswith('data:image'):
                    img_url = thumbnail_img['src']
                else:
                    urlAffiche = "https://www.allocine.fr" + film.find("div", class_="meta").find('h2', class_="meta-title").find("a")['href']
                    responseAffiche = requests.get(urlAffiche)
                    pageFilm = BeautifulSoup(responseAffiche.text, 'html.parser')
                    thumbnail_img = pageFilm.find('img', class_='thumbnail-img')
                    img_url = thumbnail_img['src'] if thumbnail_img and not thumbnail_img['src'].startswith('data:image') else 'Image de la vignette non trouvée'

                synopsis = film.find('div', class_="synopsis").find('div', class_="content-txt").get_text() if film.find('div', class_="synopsis") else "synopsis non trouvé"
                acteur_container = film.find("div", class_="meta-body-item meta-body-actor")
                acteurs = [acteur.get_text() for acteur in acteur_container.find_all("span", class_="dark-grey-link")] if acteur_container else ["acteurs non trouvés"]

                horaire_sections = film.find_all("div", class_="showtimes-hour-block")
                horaires = [horaire_section.find('span', class_="showtimes-hour-item-value").get_text() for horaire_section in horaire_sections if horaire_section.find('span', class_="showtimes-hour-item-value")] or ["Horaire non trouvé"]

                genre_container = film.find("div", class_="meta-body-item meta-body-info")
                genres = [span.get_text().strip() for span in genre_container.find_all("span") if 'class' in span.attrs and not span.attrs['class'][0].startswith('spacer') and 'nationality' not in span.attrs['class']] if genre_container else ["Genre non trouvé"]
                if genres: genres.pop(0)

                # Récupération de la durée du film
                url = "https://api.themoviedb.org/3/search/movie?query=" + titre

                headers = {
                    "accept": "application/json",
                    "Authorization": "###"
                }

                response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    data = response.json()
                    if data['results']:
                        film_id = data['results'][0]['id']
                        url = "https://api.themoviedb.org/3/movie/" + str(film_id)
                        response = requests.get(url, headers=headers)

                        data = response.json()
                        duree_film = data['runtime']

                        heure = duree_film // 60
                        minute = duree_film % 60
                    else:
                        heure = 0
                        minute = 0
                else:
                    heure = 0
                    minute = 0

                film_data = {
                    "titre": titre,
                    "realisateur": realisateur,
                    "casting": acteurs,
                    "genres": genres,
                    "duree": {"heure": heure, "minute": minute},
                    "affiche": img_url,
                    "synopsis": synopsis,
                    "horaires": [
                        {
                            "cinema": cinema,
                            "seances": horaires
                        }
                    ]
                }
                enregistrementFilm(film_data)
                print(f"{film_data['titre']} : enregistré dans la db")
            else:
                horaire_sections = film.find_all("div", class_="showtimes-hour-block")
                horaires = [horaire_section.find('span', class_="showtimes-hour-item-value").get_text() for horaire_section in horaire_sections if horaire_section.find('span', class_="showtimes-hour-item-value")] or ["Horaire non trouvé"]

                film_data = {
                    "titre": dataFilm_firebase['titre'],
                    "realisateur": dataFilm_firebase['realisateur'],
                    "casting": dataFilm_firebase['casting'],
                    'genres': ['Drame', 'Romance'], 
                    "duree": dataFilm_firebase['duree'],
                    "affiche": dataFilm_firebase['affiche'],
                    "synopsis": dataFilm_firebase['synopsis'],
                    "horaires": [
                        {
                            "cinema": cinema,
                            "seances": horaires
                        }
                    ]
                }
                print(f"{film_data['titre']} : récupéré dans la db")

            # Ajout du film s'il n'existe pas déjà
            existing_film = next((f for f in films if f["titre"] == titre), None)
            if existing_film:
                existing_film["horaires"].append({
                    "cinema": cinema,
                    "seances": horaires
                })
            else:
                films.append(film_data)
    else:
        print(f"L'élément 'showtimes-list-holder' n'a pas été trouvé pour l'URL {url}")
        films_list = []
    return films

def get_data(cinemas):
    films = []
    for cinema in cinemas:
        result = scrap_infoFilm(cinema["url"], cinema["salle"])
        films.extend(result)
    return films

def cleanFilms(films):
    filmsClean = []
    for film in films:
        existing_film = next((f for f in filmsClean if f["titre"] == film["titre"]), None)
        if existing_film:
            existing_film["horaires"].append({
                "cinema": film["horaires"][0]["cinema"],
                "seances": film["horaires"][0]["seances"]
            })
        else:
            filmsClean.append(film)
    return filmsClean
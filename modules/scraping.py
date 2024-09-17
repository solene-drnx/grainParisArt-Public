import requests
import requests_cache
from datetime import timedelta
from modules.firebase import enregistrementFilm, recupererDataFilm
import re
from datetime import datetime

requests_cache.install_cache('film_cache', expire_after=timedelta(minutes=5))



def scrap_infoFilm(date, cinema):
    
    url = f"https://www.allocine.fr/_/showtimes/theater-{cinema["url"]}/d-{date}/"
    print(url)
    
    films = []
    response = requests.get(url)

    data = response.json()
    if not data.get('error') and 'results' in data:
        for film_data in data['results']:

            all_showtimes = []

            movie = film_data['movie']
            showtimes = film_data['showtimes']
            titre = movie['title']
            realisateur = ', '.join([
                f"{credit['person']['firstName'] or ''} {credit['person']['lastName'] or ''}".strip()
                for credit in movie.get('credits', []) 
                if credit['position']['name'] == 'DIRECTOR'
            ])
            synopsis = movie['synopsis']
            img_url = movie['poster']['url'] if movie.get('poster') else 'Image non disponible'
            runtime = movie['runtime']
            genres = [genre['translate'] for genre in movie['genres']]
            casting = [
                f"{edge['node']['actor']['firstName'] or 'Inconnu'} {edge['node']['actor']['lastName'] or 'Inconnu'}"
                for edge in movie.get('cast', {}).get('edges', [])
                if edge['node']['actor'] is not None
            ]
            match = re.match(r'(?P<heures>\d+)h (?P<minutes>\d+)min', runtime)

            if match:
                heures = int(match.group('heures'))
                minutes = int(match.group('minutes'))
            else:
                heures = 0
                minutes = 0

            for type_showtime in ['dubbed', 'original', 'local', 'multiple']:
                horaires = showtimes.get(type_showtime, [])
                for horaire in horaires:
                    start_time = horaire['startsAt']
                    start_datetime = datetime.fromisoformat(start_time)
                    formatted_time = f"{start_datetime.hour}h{start_datetime.minute:02d}"
                    all_showtimes.append(formatted_time)


            dataFilm_firebase = recupererDataFilm(f"{titre}", f"{realisateur}")

            print(dataFilm_firebase)
            if dataFilm_firebase == 0:
                film_data = {
                    "titre": titre,
                    "realisateur": realisateur if realisateur else "Réalisateur non trouvé",
                    "casting": casting if casting else ["Acteurs non trouvés"],
                    "genres": genres if genres else ["Genre non trouvé"],
                    "duree" :{"heure": heures, "minute": minutes},
                    "affiche": img_url,
                    "synopsis": synopsis,
                    "horaires": [
                        {
                            "cinema": cinema["salle"],
                            "seances": all_showtimes if all_showtimes else ["Horaire non trouvé"]
                        }
                    ]
                }
            
                films.append(film_data)
                enregistrementFilm(film_data)
            else:

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
                                "seances": all_showtimes if all_showtimes else ["Horaire non trouvé"]
                            }
                        ]
                    }
           
                print(f"{film_data['titre']} : récupéré dans la db")

    
                existing_film = next((f for f in films if f["titre"] == titre), None)
                if existing_film:
                    existing_film["horaires"].append({
                        "cinema": cinema,
                        "seances": all_showtimes if all_showtimes else ["Horaire non trouvé"]
                    })
                else:
                    films.append(film_data)
      
    return films 


def get_data(cinemas, date):
    films = []
    for cinema in cinemas:
        result = scrap_infoFilm(date, cinema)
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
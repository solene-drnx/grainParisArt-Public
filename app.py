from flask import Flask, render_template, request
from datetime import datetime, timedelta

# IMPORT DES MODULES 
from modules.Classes import *

cinemas = {
    "C0071": "Écoles Cinéma Club",
    "C2954": "MK2 Bibliothèque",
    "C0050": "MK2 Beaubourg",
    "W7504": "Épée de bois",
    "C0076": "Cinéma du Panthéon",
    "C0089": "Max Linder Panorama",
    "C0013": "Luminor Hotel de Ville",
    "C0072": "Le Grand Action",
    "C0099": "MK2 Parnasse",
    "C0073": "Le Champo",
    "C0020": "Filmothèque du Quartier Latin",
    "C0074": "Reflet Medicis",
    "C0159": "UGC Ciné Cité Les Halles",
    "C0026": "UGC Ciné Cité Bercy"
}

theaters: list[Theater] = []
for id, name in cinemas.items():
    theaters.append(Theater({
        "name": name,
        "internalId": id,
        "location": None
    }))

def getShowtimes(date):
    showtimes:list[Showtime] = []

    for theater in theaters:
        showtimes.extend(theater.getShowtimes(date))

    data = {}

    for showtime in showtimes:
        movie = showtime.movie
        theater = showtime.theater

        if showtime.movie.title not in data.keys():
            data[movie.title] = {
                "title": movie.title,
                "duree": movie.runtime,
                "genres": ", ".join(movie.genres),
                "casting": ", ".join(movie.cast),
                "realisateur": movie.director,
                "synopsis": movie.synopsis,
                "affiche": movie.affiche,
                "director": movie.director,
                "wantToSee": movie.wantToSee,
                "url": f"https://www.allocine.fr/film/fichefilm_gen_cfilm={movie.id}.html",
                "seances": {}
            }

            
        if theater.name not in data[movie.title]["seances"].keys():
            data[movie.title]["seances"][theater.name] = []

        data[movie.title]["seances"][theater.name].append(showtime.startsAt.strftime("%H:%M"))

    data = data.values()

    data = sorted(data, key=lambda x: x["wantToSee"], reverse=True)

    return data

showtimes = []
for i in range(0, 7):
    day_showtimes = getShowtimes(datetime.today()+timedelta(days=i))
    showtimes.append(day_showtimes)
    print(f"{len(day_showtimes)} séances récupéré {i+1}/7!")

app = Flask(__name__)

def translateMonth(num: int):
    match num:
        case 1: return "janv"
        case 2: return "févr"
        case 3: return "mars"
        case 4: return "avr"
        case 5: return "mai"
        case 6: return "juin"
        case 7: return "juil"
        case 8: return "août"
        case 9: return "sept"
        case 10: return "oct"
        case 11: return "nov"
        case 12: return "déc"
        case _: return "???"

def translateDay(weekday: int):
    match weekday:
        case 0: return "lun"
        case 1: return "mar"
        case 2: return "mer"
        case 3: return "jeu"
        case 4: return "ven"
        case 5: return "sam"
        case 6: return "dim"
        case _: return "???"

@app.route('/health')
def health():
    return "OK"

def format(cinema, nb):
    return ({
        "salle": cinema["salle"],
        "url": decalageDate(cinema["url"], nb)
    })

cinemas_data = [
    {
        "salle" : "Écoles Cinéma Club",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0071.html"
    },
    {
        "salle" : "MK2 Bibliothèque",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C2954.html",
    },
    {
        "salle" : "MK2 Beaubourg",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0050.html"
    }, 
    {
        "salle" : "Épée de bois",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=W7504.html"
    }, 
    {
        "salle" : "Cinéma du Panthéon",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0076.html"
    },
    {
        "salle" : "Max Linder Panorama",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0089.html"
    },
    {
        "salle" : "Luminor Hotel de Ville",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0013.html"
    },
    {
        "salle" : "Le Grand Action",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0072.html"
    },
    {
        "salle" : "MK2 Parnasse", 
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0099.html"
    },
    { 
        "salle" : "Le Champo",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0073.html"
    },
    {
        "salle" : "Filmothèque du Quartier Latin",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0020.html"
    },
    {
        "salle" : "Reflet Medicis",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0074.html"
    },
    {
        "salle" : "UGC Ciné Cité Les Halles",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0159.html"
    },
    {
        "salle" : "UGC Ciné Cité Bercy",
        "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0026.html"
    }
]

@app.route('/')
def home():
    delta = request.args.get("delta", default=0, type=int)

<<<<<<< HEAD
    cinemas = cinemas_data;
=======
    if delta > 6: delta = 6
    if delta < 0: delta = 0
>>>>>>> 142c74e5ab8db960a2486bc4c838a4833b807664

    dates = []

    for i in range(0,7):
        day = datetime.today()+timedelta(i)
        dates.append({
            "jour": translateDay(day.weekday()),
            "chiffre": day.day,
            "mois": translateMonth(day.month),
            "choisi": i==delta,
            "index": i
        })

    return render_template('index.html', page_actuelle='home', films=showtimes[delta], dates=dates)

<<<<<<< HEAD
@app.route('/jour1')
@cache.cached(timeout=3600)
def jour1():
    date = {
        "jour1" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 0),
            "chiffre" : testChiffreJour(datetime.today().day, 0),
            "mois" : testMoisNumero(datetime.today().day, 0)
        },
        "jour2" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 1),
            "chiffre" : testChiffreJour(datetime.today().day, 1),
            "mois" : testMoisNumero(datetime.today().day, 1)
        },
        "jour3" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 2),
            "chiffre" : testChiffreJour(datetime.today().day, 2),
            "mois" : testMoisNumero(datetime.today().day, 2)
        },
        "jour4" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 3),
            "chiffre" : testChiffreJour(datetime.today().day, 3),
            "mois" : testMoisNumero(datetime.today().day, 3)
        },
        "jour5" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 4),
            "chiffre" : testChiffreJour(datetime.today().day, 4),
            "mois" : testMoisNumero(datetime.today().day, 4)
        },
        "jour6" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 5),
            "chiffre" : testChiffreJour(datetime.today().day, 5),
            "mois" : testMoisNumero(datetime.today().day, 5)
        },
        "jour7" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 6),
            "chiffre" : testChiffreJour(datetime.today().day, 6),
            "mois" : testMoisNumero(datetime.today().day, 6)
        }
    }

    films = []

    cinemas = list(map(lambda cinema: format(cinema, 1), cinemas))

    films = get_data(cinemas)
    filmsClean = cleanFilms(films)

    return render_template('jours/jour1.html', page_actuelle='jour1', films=filmsClean, date=date)

@app.route('/jour2')
@cache.cached(timeout=3600)
def jour2():
    date = {
        "jour1" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 0),
            "chiffre" : testChiffreJour(datetime.today().day, 0),
            "mois" : testMoisNumero(datetime.today().day, 0)
        },
        "jour2" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 1),
            "chiffre" : testChiffreJour(datetime.today().day, 1),
            "mois" : testMoisNumero(datetime.today().day, 1)
        },
        "jour3" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 2),
            "chiffre" : testChiffreJour(datetime.today().day, 2),
            "mois" : testMoisNumero(datetime.today().day, 2)
        },
        "jour4" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 3),
            "chiffre" : testChiffreJour(datetime.today().day, 3),
            "mois" : testMoisNumero(datetime.today().day, 3)
        },
        "jour5" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 4),
            "chiffre" : testChiffreJour(datetime.today().day, 4),
            "mois" : testMoisNumero(datetime.today().day, 4)
        },
        "jour6" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 5),
            "chiffre" : testChiffreJour(datetime.today().day, 5),
            "mois" : testMoisNumero(datetime.today().day, 5)
        },
        "jour7" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 6),
            "chiffre" : testChiffreJour(datetime.today().day, 6),
            "mois" : testMoisNumero(datetime.today().day, 6)
        }
    }

    films = []

    cinemas = list(map(lambda cinema: format(cinema, 2), cinemas))

    films = get_data(cinemas)
    filmsClean = cleanFilms(films)
    
    return render_template('jours/jour2.html', page_actuelle='jour2', films=filmsClean, date=date)

@app.route('/jour3')
@cache.cached(timeout=3600)
def jour3():
    date = {
        "jour1" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 0),
            "chiffre" : testChiffreJour(datetime.today().day, 0),
            "mois" : testMoisNumero(datetime.today().day, 0)
        },
        "jour2" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 1),
            "chiffre" : testChiffreJour(datetime.today().day, 1),
            "mois" : testMoisNumero(datetime.today().day, 1)
        },
        "jour3" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 2),
            "chiffre" : testChiffreJour(datetime.today().day, 2),
            "mois" : testMoisNumero(datetime.today().day, 2)
        },
        "jour4" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 3),
            "chiffre" : testChiffreJour(datetime.today().day, 3),
            "mois" : testMoisNumero(datetime.today().day, 3)
        },
        "jour5" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 4),
            "chiffre" : testChiffreJour(datetime.today().day, 4),
            "mois" : testMoisNumero(datetime.today().day, 4)
        },
        "jour6" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 5),
            "chiffre" : testChiffreJour(datetime.today().day, 5),
            "mois" : testMoisNumero(datetime.today().day, 5)
        },
        "jour7" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 6),
            "chiffre" : testChiffreJour(datetime.today().day, 6),
            "mois" : testMoisNumero(datetime.today().day, 6)
        }
    }

    films = []

    cinemas = list(map(lambda cinema: format(cinema, 3), cinemas))

    films = get_data(cinemas)
    filmsClean = cleanFilms(films)
    
    return render_template('jours/jour3.html', page_actuelle='jour3', films=filmsClean, date=date)

@app.route('/jour4')
@cache.cached(timeout=3600)
def jour4():
    date = {
        "jour1" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 0),
            "chiffre" : testChiffreJour(datetime.today().day, 0),
            "mois" : testMoisNumero(datetime.today().day, 0)
        },
        "jour2" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 1),
            "chiffre" : testChiffreJour(datetime.today().day, 1),
            "mois" : testMoisNumero(datetime.today().day, 1)
        },
        "jour3" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 2),
            "chiffre" : testChiffreJour(datetime.today().day, 2),
            "mois" : testMoisNumero(datetime.today().day, 2)
        },
        "jour4" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 3),
            "chiffre" : testChiffreJour(datetime.today().day, 3),
            "mois" : testMoisNumero(datetime.today().day, 3)
        },
        "jour5" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 4),
            "chiffre" : testChiffreJour(datetime.today().day, 4),
            "mois" : testMoisNumero(datetime.today().day, 4)
        },
        "jour6" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 5),
            "chiffre" : testChiffreJour(datetime.today().day, 5),
            "mois" : testMoisNumero(datetime.today().day, 5)
        },
        "jour7" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 6),
            "chiffre" : testChiffreJour(datetime.today().day, 6),
            "mois" : testMoisNumero(datetime.today().day, 6)
        }
    }

    films = []

    cinemas = list(map(lambda cinema: format(cinema, 4), cinemas))

    films = get_data(cinemas)
    filmsClean = cleanFilms(films)
    
    return render_template('jours/jour4.html', page_actuelle='jour4', films=filmsClean, date=date)

@app.route('/jour5')
@cache.cached(timeout=3600)
def jour5():
    date = {
        "jour1" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 0),
            "chiffre" : testChiffreJour(datetime.today().day, 0),
            "mois" : testMoisNumero(datetime.today().day, 0)
        },
        "jour2" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 1),
            "chiffre" : testChiffreJour(datetime.today().day, 1),
            "mois" : testMoisNumero(datetime.today().day, 1)
        },
        "jour3" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 2),
            "chiffre" : testChiffreJour(datetime.today().day, 2),
            "mois" : testMoisNumero(datetime.today().day, 2)
        },
        "jour4" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 3),
            "chiffre" : testChiffreJour(datetime.today().day, 3),
            "mois" : testMoisNumero(datetime.today().day, 3)
        },
        "jour5" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 4),
            "chiffre" : testChiffreJour(datetime.today().day, 4),
            "mois" : testMoisNumero(datetime.today().day, 4)
        },
        "jour6" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 5),
            "chiffre" : testChiffreJour(datetime.today().day, 5),
            "mois" : testMoisNumero(datetime.today().day, 5)
        },
        "jour7" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 6),
            "chiffre" : testChiffreJour(datetime.today().day, 6),
            "mois" : testMoisNumero(datetime.today().day, 6)
        }
    }

    films = []

    cinemas = list(map(lambda cinema: format(cinema, 5), cinemas))
    films = get_data(cinemas)
    filmsClean = cleanFilms(films)
    
    return render_template('jours/jour5.html', page_actuelle='jour5', films=filmsClean, date=date)

@app.route('/jour6')
@cache.cached(timeout=3600)
def jour6():
    date = {
        "jour1" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 0),
            "chiffre" : testChiffreJour(datetime.today().day, 0),
            "mois" : testMoisNumero(datetime.today().day, 0)
        },
        "jour2" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 1),
            "chiffre" : testChiffreJour(datetime.today().day, 1),
            "mois" : testMoisNumero(datetime.today().day, 1)
        },
        "jour3" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 2),
            "chiffre" : testChiffreJour(datetime.today().day, 2),
            "mois" : testMoisNumero(datetime.today().day, 2)
        },
        "jour4" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 3),
            "chiffre" : testChiffreJour(datetime.today().day, 3),
            "mois" : testMoisNumero(datetime.today().day, 3)
        },
        "jour5" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 4),
            "chiffre" : testChiffreJour(datetime.today().day, 4),
            "mois" : testMoisNumero(datetime.today().day, 4)
        },
        "jour6" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 5),
            "chiffre" : testChiffreJour(datetime.today().day, 5),
            "mois" : testMoisNumero(datetime.today().day, 5)
        },
        "jour7" : {
            "jour" : anglais_intoJourFrancais(datetime.today().strftime("%A"), 6),
            "chiffre" : testChiffreJour(datetime.today().day, 6),
            "mois" : testMoisNumero(datetime.today().day, 6)
        }
    }

    films = []

    cinemas = list(map(lambda cinema: format(cinema, 6), cinemas))

    films = get_data(cinemas)
    filmsClean = cleanFilms(films)
    
    return render_template('jours/jour6.html', page_actuelle='jour6', films=filmsClean, date=date)

"""
@app.route('/process')
def process():
    # Simule un traitement long
    time.sleep(5)
    return jsonify(status='success', message='Traitement terminé')
"""
if __name__ == '__main__':
    app.run(debug=True) 
=======
if __name__ == '__main__':
    app.run() 
>>>>>>> 142c74e5ab8db960a2486bc4c838a4833b807664

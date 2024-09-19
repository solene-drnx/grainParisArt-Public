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

@app.route('/')
@app.route('/index')
def home():
    delta = request.args.get("delta", default=0, type=int)

    if delta > 6: delta = 6
    if delta < 0: delta = 0

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

if __name__ == '__main__':
    app.run() 
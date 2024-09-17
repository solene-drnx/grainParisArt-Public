from flask import Flask, render_template, request
from datetime import datetime
from flask_caching import Cache
import asyncio

# IMPORT DES MODULES 
from modules.date import chiffre_intoMonth, anglais_intoJourFrancais, testChiffreJour, testMoisNumero
from modules.scraping import scrap_infoFilm, get_data, cleanFilms
from modules.urlGenerator import decalageDate

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

def jour_general(jour_num):
    date = {
        f"jour{i}": {
            "jour": anglais_intoJourFrancais(datetime.today().strftime("%A"), i-1),
            "chiffre": testChiffreJour(datetime.today().day, i-1),
            "mois": testMoisNumero(datetime.today().month, i-1)
        } for i in range(1, 8)
    }

    cinemas = [
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

    films = get_data(cinemas)
    filmsClean = cleanFilms(films)

    return render_template(f'jours/jour{jour_num}.html', page_actuelle=f'jour{jour_num}', films=filmsClean, date=date)


@app.route('/')
@cache.cached(timeout=3600)
def home():
    return jour_general(1)

@app.route('/jour1')
@cache.cached(timeout=3600)
def jour1():
    return jour_general(1)

@app.route('/jour2')
@cache.cached(timeout=3600)
def jour2():
    return jour_general(2)

@app.route('/jour3')
@cache.cached(timeout=3600)
def jour3():
    return jour_general(3)

@app.route('/jour4')
@cache.cached(timeout=3600)
def jour4():
    return jour_general(4)

@app.route('/jour5')
@cache.cached(timeout=3600)
def jour5():
    return jour_general(5)

@app.route('/jour6')
@cache.cached(timeout=3600)
def jour6():
    return jour_general(6)

@app.route('/jour7')
@cache.cached(timeout=3600)
def jour7():
    return jour_general(7)


"""
@app.route('/process')
def process():
    # Simule un traitement long
    time.sleep(5)
    return jsonify(status='success', message='Traitement terminé')
"""
if __name__ == '__main__':
    app.run(debug=True)  
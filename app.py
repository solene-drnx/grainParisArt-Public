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

@app.route('/')
@cache.cached(timeout=3600)
def home():
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

    return render_template('index.html', page_actuelle='home', films=filmsClean, date=date)


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

    cinemas = [
        {
            "salle" : "Écoles Cinéma Club",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0071.html#shwt_date=", 1)
        },
        {
            "salle" : "MK2 Bibliothèque",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C2954.html#shwt_date=l",1)
        },
        {
            "salle" : "MK2 Beaubourg",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0050.html#shwt_date=",1)
        }, 
        {
            "salle" : "Épée de bois",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=W7504.html#shwt_date=",1)
        }, 
        {
            "salle" : "Cinéma du Panthéon",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0076.html#shwt_date=",1)
        },
        {
            "salle" : "Max Linder Panorama",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0089.html#shwt_date=",1)
        },
        {
            "salle" : "Luminor Hotel de Ville",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0013.html#shwt_date=",1)
        },
        {
            "salle" : "Le Grand Action",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0072.html#shwt_date=",1)
        },
        {
            "salle" : "MK2 Parnasse", 
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0099.html#shwt_date=",1)
        },
        { 
            "salle" : "Le Champo",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0073.html#shwt_date=",1)
        },
        {
            "salle" : "Filmothèque du Quartier Latin",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0020.html#shwt_date=",1)
        },
        {
            "salle" : "Reflet Medicis",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0074.html#shwt_date=",1)
        },
        {
            "salle" : "UGC Ciné Cité Les Halles",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0159.html#shwt_date=",1)
        },
        {
            "salle" : "UGC Ciné Cité Bercy",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0026.html#shwt_date=",1)
        }
    ]

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

    cinemas = [
        {
            "salle" : "Écoles Cinéma Club",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0071.html#shwt_date=", 2)
        },
        {
            "salle" : "MK2 Bibliothèque",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C2954.html#shwt_date=l",2)
        },
        {
            "salle" : "MK2 Beaubourg",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0050.html#shwt_date=",2)
        }, 
        {
            "salle" : "Épée de bois",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=W7504.html#shwt_date=",2)
        }, 
        {
            "salle" : "Cinéma du Panthéon",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0076.html#shwt_date=",2)
        },
        {
            "salle" : "Max Linder Panorama",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0089.html#shwt_date=",2)
        },
        {
            "salle" : "Luminor Hotel de Ville",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0013.html#shwt_date=",2)
        },
        {
            "salle" : "Le Grand Action",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0072.html#shwt_date=",2)
        },
        {
            "salle" : "MK2 Parnasse", 
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0099.html#shwt_date=",2)
        },
        { 
            "salle" : "Le Champo",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0073.html#shwt_date=",2)
        },
        {
            "salle" : "Filmothèque du Quartier Latin",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0020.html#shwt_date=",2)
        },
        {
            "salle" : "Reflet Medicis",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0074.html#shwt_date=",2)
        },
        {
            "salle" : "UGC Ciné Cité Les Halles",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0159.html#shwt_date=",2)
        },
        {
            "salle" : "UGC Ciné Cité Bercy",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0026.html#shwt_date=",2)
        }
    ]

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

    cinemas = [
        {
            "salle" : "Écoles Cinéma Club",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0071.html#shwt_date=", 3)
        },
        {
            "salle" : "MK2 Bibliothèque",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C2954.html#shwt_date=l",3)
        },
        {
            "salle" : "MK2 Beaubourg",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0050.html#shwt_date=",3)
        }, 
        {
            "salle" : "Épée de bois",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=W7504.html#shwt_date=",3)
        }, 
        {
            "salle" : "Cinéma du Panthéon",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0076.html#shwt_date=",3)
        },
        {
            "salle" : "Max Linder Panorama",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0089.html#shwt_date=",3)
        },
        {
            "salle" : "Luminor Hotel de Ville",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0013.html#shwt_date=",3)
        },
        {
            "salle" : "Le Grand Action",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0072.html#shwt_date=",3)
        },
        {
            "salle" : "MK2 Parnasse", 
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0099.html#shwt_date=",3)
        },
        { 
            "salle" : "Le Champo",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0073.html#shwt_date=",3)
        },
        {
            "salle" : "Filmothèque du Quartier Latin",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0020.html#shwt_date=",3)
        },
        {
            "salle" : "Reflet Medicis",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0074.html#shwt_date=",3)
        },
        {
            "salle" : "UGC Ciné Cité Les Halles",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0159.html#shwt_date=",3)
        },
        {
            "salle" : "UGC Ciné Cité Bercy",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0026.html#shwt_date=",3)
        }
    ]

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

    cinemas = [
        {
            "salle" : "Écoles Cinéma Club",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0071.html#shwt_date=", 4)
        },
        {
            "salle" : "MK2 Bibliothèque",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C2954.html#shwt_date=l",4)
        },
        {
            "salle" : "MK2 Beaubourg",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0050.html#shwt_date=",4)
        }, 
        {
            "salle" : "Épée de bois",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=W7504.html#shwt_date=",4)
        }, 
        {
            "salle" : "Cinéma du Panthéon",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0076.html#shwt_date=",4)
        },
        {
            "salle" : "Max Linder Panorama",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0089.html#shwt_date=",4)
        },
        {
            "salle" : "Luminor Hotel de Ville",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0013.html#shwt_date=",4)
        },
        {
            "salle" : "Le Grand Action",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0072.html#shwt_date=",4)
        },
        {
            "salle" : "MK2 Parnasse", 
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0099.html#shwt_date=",4)
        },
        { 
            "salle" : "Le Champo",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0073.html#shwt_date=",4)
        },
        {
            "salle" : "Filmothèque du Quartier Latin",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0020.html#shwt_date=",4)
        },
        {
            "salle" : "Reflet Medicis",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0074.html#shwt_date=",4)
        },
        {
            "salle" : "UGC Ciné Cité Les Halles",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0159.html#shwt_date=",4)
        },
        {
            "salle" : "UGC Ciné Cité Bercy",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0026.html#shwt_date=",4)
        }
    ]

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

    cinemas = [
        {
            "salle" : "Écoles Cinéma Club",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0071.html#shwt_date=",5)
        },
        {
            "salle" : "MK2 Bibliothèque",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C2954.html#shwt_date=l",5)
        },
        {
            "salle" : "MK2 Beaubourg",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0050.html#shwt_date=",5)
        }, 
        {
            "salle" : "Épée de bois",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=W7504.html#shwt_date=",5)
        }, 
        {
            "salle" : "Cinéma du Panthéon",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0076.html#shwt_date=",5)
        },
        {
            "salle" : "Max Linder Panorama",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0089.html#shwt_date=",5)
        },
        {
            "salle" : "Luminor Hotel de Ville",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0013.html#shwt_date=",5)
        },
        {
            "salle" : "Le Grand Action",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0072.html#shwt_date=",5)
        },
        {
            "salle" : "MK2 Parnasse", 
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0099.html#shwt_date=",5)
        },
        { 
            "salle" : "Le Champo",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0073.html#shwt_date=",5)
        },
        {
            "salle" : "Filmothèque du Quartier Latin",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0020.html#shwt_date=",5)
        },
        {
            "salle" : "Reflet Medicis",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0074.html#shwt_date=",5)
        },
        {
            "salle" : "UGC Ciné Cité Les Halles",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0159.html#shwt_date=",5)
        },
        {
            "salle" : "UGC Ciné Cité Bercy",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0026.html#shwt_date=",5)
        }
    ]

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

    cinemas = [
        {
            "salle" : "Écoles Cinéma Club",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0071.html#shwt_date=", 6)
        },
        {
            "salle" : "MK2 Bibliothèque",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C2954.html#shwt_date=l",6)
        },
        {
            "salle" : "MK2 Beaubourg",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0050.html#shwt_date=",6)
        }, 
        {
            "salle" : "Épée de bois",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=W7504.html#shwt_date=",6)
        }, 
        {
            "salle" : "Cinéma du Panthéon",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0076.html#shwt_date=",6)
        },
        {
            "salle" : "Max Linder Panorama",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0089.html#shwt_date=",6)
        },
        {
            "salle" : "Luminor Hotel de Ville",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0013.html#shwt_date=",6)
        },
        {
            "salle" : "Le Grand Action",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0072.html#shwt_date=",6)
        },
        {
            "salle" : "MK2 Parnasse", 
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0099.html#shwt_date=",6)
        },
        { 
            "salle" : "Le Champo",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0073.html#shwt_date=",6)
        },
        {
            "salle" : "Filmothèque du Quartier Latin",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0020.html#shwt_date=",6)
        },
        {
            "salle" : "Reflet Medicis",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0074.html#shwt_date=",6)
        },
        {
            "salle" : "UGC Ciné Cité Les Halles",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0159.html#shwt_date=",6)
        },
        {
            "salle" : "UGC Ciné Cité Bercy",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0026.html#shwt_date=",6)
        }
    ]

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
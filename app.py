from flask import Flask, render_template
from datetime import datetime
from flask_caching import Cache
from datetime import datetime, timedelta
# IMPORT DES MODULES 
from modules.date import anglais_intoJourFrancais, testChiffreJour, testMoisNumero
from modules.scraping import get_data, cleanFilms

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
def format_date(date):
    return date.strftime('%Y-%m-%d')


def jour_general(jour_num):
   
    if jour_num == 0:
        jour_num += 1

    dates = [format_date(datetime.today() + timedelta(days=i)) for i in range(7)]
    date = {
        f"jour{i + 1}": {
            "jour": anglais_intoJourFrancais(datetime.today().strftime("%A"), i),
            "chiffre": testChiffreJour(datetime.today().day, i),
            "mois": testMoisNumero(datetime.today().month, i)
        } for i in range(7)
    }
   

    cinemas = [
        {
            "salle": "Écoles Cinéma Club",
            "url": "C0071"
        },
        {
            "salle": "MK2 Bibliothèque",
            "url": "C2954"
        },
        {
            "salle": "MK2 Beaubourg",
            "url": "C0050"
        },
        {
            "salle": "Épée de bois",
            "url": "W7504"
        },
        {
            "salle": "Cinéma du Panthéon",
            "url": "C0076"
        },
        {
            "salle": "Max Linder Panorama",
            "url": "C0089"
        },
        {
            "salle": "Luminor Hotel de Ville",
            "url": "C0013"
        },
        {
            "salle": "Le Grand Action",
            "url": "C0072"
        },
        {
            "salle": "MK2 Parnasse",
            "url": "C0099"
        },
        {
            "salle": "Le Champo",
            "url": "C0073"
        },
        {
            "salle": "Filmothèque du Quartier Latin",
            "url": "C0020"
        },
        {
            "salle": "Reflet Medicis",
            "url": "C0074"
        },
        {
            "salle": "UGC Ciné Cité Les Halles",
            "url": "C0159"
        },
        {
            "salle": "UGC Ciné Cité Bercy",
            "url": "C0026"
        }
    ]

    films = get_data(cinemas, dates[jour_num-1])
    filmsClean = cleanFilms(films)

    if jour_num == 0:
        return render_template('index.html', page_actuelle='home', films=filmsClean, date=date)
    else:
        return render_template(f'jours/jour{jour_num}.html', page_actuelle=f'jour{jour_num}', films=filmsClean, date=date)


@app.route('/')
@cache.cached(timeout=3600)
def home():
    return jour_general(0)

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
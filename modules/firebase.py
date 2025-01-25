import firebase_admin
from firebase_admin import credentials, db
import urllib.parse

cred = credentials.Certificate('static/firebase/firebase_grainParisArt.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': '###'  
})

ref = db.reference('/')

film = {
    'titre': "L'I.A. du mal", 
    'realisateur': 'Luca Guadagnino', 
    'casting': [' Zendaya', "Josh O'Connor", 'Mike Faist'], 
    'genres': ['Drame', 'Romance'], 
    'duree': {'heure': 2, 'minute': 12}, 
    'affiche': 'https://fr.web.img2.acsta.net/c_310_420/pictures/24/01/15/10/08/2202044.jpg', 
    'synopsis': '\nDurant leurs études, Patrick et Art, tombent amoureux de Tashi. À la fois amis, amants et rivaux, ils voient tous les trois leurs chemins se recroiser des années plus tard. Leur passé et leur présent s’entrechoquent et des tensions jusque-là inavouées refont surface.\n', 
    'horaires': [{'cinema': 'MK2 Parnasse', 'seances': ['20:45']}]
}

def encode_node_name(name):
    replacements = {
        '.': '__dot__',
        '$': '__dollar__',
        '#': '__hash__',
        '[': '__lbrack__',
        ']': '__rbrack__',
        '/': '__slash__',
        '?': '__question__'
    }
    
    for char, replacement in replacements.items():
        name = name.replace(char, replacement)
    
    return name


def enregistrementFilm(film):
    cleaned_movie_name = encode_node_name(film['titre'])
    movie_ref = ref.child(cleaned_movie_name)
    movie_ref.set({
        'titre': film['titre'],
        'realisateur': film['realisateur'],
        'casting': film['casting'],
        'genres': film['genres'],
        'duree': film['duree'],
        'affiche': film['affiche'],
        'synopsis': film['synopsis']
    })
    print(f"Node '{film['titre']}' created successfully with details!")

def recupererDataFilm(nomFilm, realisateur):
    cleaned_movie_name = encode_node_name(nomFilm)
    print(cleaned_movie_name)
    movie_ref = ref.child(cleaned_movie_name)
    
    # Lire les données du nœud
    movie_data = movie_ref.get()
    
    if movie_data:
        # Vérifier si le réalisateur correspond
        if movie_data.get('realisateur') == realisateur:
            return movie_data
        else:
            return 0
    else:
        return 0
    
def supprimerTousLesFilms():
    root_ref = ref
    root_ref.delete()
    print("Tous les films ont été supprimés.")

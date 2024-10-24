from datetime import datetime
import requests

class Movie:
    def __init__(self, data) -> None:
        self.data = data
        self.title = data["title"]
        self.id = data['internalId']
        self.runtime = data["runtime"]
        self.synopsis = data["synopsis"]
        self.genres = [genre['translate'] for genre in data["genres"]]
        self.wantToSee = data['stats']["wantToSeeCount"]
        try:
            self.affiche = data["poster"]["url"]
        except:
            self.affiche = "/static/images/nocontent.png"
            
        self.cast = []

        # Noms des acteurs
        for actor in data["cast"]["edges"]:
            if actor["node"]["actor"] == None: continue

            if actor["node"]["actor"]["lastName"] == None:
                actor["node"]["actor"]["lastName"] = ""
                
            if actor["node"]["actor"]["firstName"] == None:
                actor["node"]["actor"]["firstName"] = ""

            name = f'{actor["node"]["actor"]["firstName"]} {actor["node"]["actor"]["lastName"]}'
            name = name.lstrip()
            self.cast.append(name)

        # Nom du réalisateur
        if len(data["credits"]) == 0:
            self.director = "Inconnu"
        else:
            if data["credits"][0]["person"]["lastName"] == None:
                data["credits"][0]["person"]["lastName"] = ""
                
            if data["credits"][0]["person"]["firstName"] == None:
                data["credits"][0]["person"]["firstName"] = ""

            self.director = f'{data["credits"][0]["person"]["firstName"]} {data["credits"][0]["person"]["lastName"]}'
            self.director = self.director.lstrip()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.title}>"

class Showtime:
    def __init__(self, data, theather, movie:Movie) -> None:
        self.startsAt = datetime.fromisoformat(data['startsAt'])
        self.diffusionVersion = data['diffusionVersion']
        self.services = data["service"]
        self.theater:Theater = theather
        self.movie = movie

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.movie.title} startsAt={self.startsAt}>"

class Theater:
    def __init__(self, data) -> None:
        self.name = data['name']
        self.id = data['internalId']
        self.location = data['location']

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.name}>"

    def getShowtimes(self, date: datetime, page: int = 1, showtimes: list = None) -> list[Showtime]:
        if showtimes is None:
            showtimes = []
        
        datestr = date.strftime("%Y-%m-%d")
        r = requests.get(f"https://www.allocine.fr/_/showtimes/theater-{self.id}/d-{datestr}/p-{page}/")
        
        if r.status_code != 200:
            raise Exception(f"Error: {r.status_code} - {r.content}")
        
        try:
            data = r.json()
        except Exception as e:
            raise Exception(f"Can't parse JSON: {str(e)} - {r.content}")
        
        if data["message"] == "no.showtime.error":
            return []
        
        if data["message"] == "next.showtime.on":
            return []

        if data.get('error'):
            raise Exception(f"API Error: {data}")
        
        for movie in data['results']:
            inst = Movie(movie["movie"])
            movie_showtimes = movie["showtimes"].get("dubbed", []) + \
                            movie["showtimes"].get("original", []) + \
                            movie["showtimes"].get("local", [])

            for showtime_data in movie_showtimes:
                showtimes.append(Showtime(showtime_data, self, inst))
        
        if int(data['pagination']['page']) < int(data['pagination']["totalPages"]):
            return self.getShowtimes(date, page + 1, showtimes)
        
        return showtimes
    
    @staticmethod
    def new(query:str):
        r = requests.get(f"https://www.allocine.fr/_/localization_city/{query}")

        try:
            data = r.json()
        except:
            return {"error": True, "message": "Can't parse JSON", "content": r.content}

        if len(data["values"]["theaters"]) == 0:
            return {"error": True, "message": "Not found", "content": r.content}
        
        return Theater(data["values"]["theaters"][0]["node"])

if __name__ == "__main__":
    cgr = Theater.new("CGR Brest Le Celtic")
    print(f"{cgr.name} ({cgr.id})")
    print(f"{cgr.location['zip']} {cgr.location['city']}")

    showtimes = cgr.getShowtimes(datetime.today())

    print(showtimes[0])
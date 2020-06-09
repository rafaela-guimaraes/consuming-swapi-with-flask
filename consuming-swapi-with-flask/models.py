import re


class BaseQuerySet(object):
    def __init__(self):
        self.items = []

    def order_by(self, order_attr, descending=False):
        return sorted(self.items, key=lambda k: getattr(k, order_attr), reverse=descending)

    def get_all(self):
        return self.items


class BaseModel(object):
    def get_id(self, url):
        return re.search(re.compile('[0-9]+'), url).group(0)

    def get_ids_list(self, urls):
        if not urls:
            return []

        return [self.get_id(url) for url in urls]


class Starship(BaseModel):
    def __init__(self, cargo_capacity, consumables, cost_in_credits, created,
                 crew, edited, hyperdrive_rating, length, MGLT,  manufacturer, max_atmosphering_speed,
                 model, name, passengers, films, pilots, starship_class, url, **kwargs):

        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.cost_in_credits = cost_in_credits
        self.crew = crew
        self.created = created
        self.edited = edited
        self.hyperdrive_rating = hyperdrive_rating,
        self.length = length
        self.MGLT = MGLT
        self.manufacturer = manufacturer,
        self.max_atmosphering_speed = max_atmosphering_speed,
        self.model = model
        self.name = name
        self.passengers = passengers,
        self.films = self.get_ids_list(films),
        self.pilots = pilots
        self.starship_class = starship_class
        self.url = url
        try:
            self.score = float(hyperdrive_rating) / int(cost_in_credits),
        except:
            self.score = 0,
        self.id = self.get_id(url)


class StarshipQuerySet(BaseQuerySet):
    def __init__(self, starships):
        super(StarshipQuerySet, self).__init__()
        for starship in starships:
            self.items.append(Starship(**starship))
        
    def get_starships_as_choices(self):
        return [(starship.id, starship.name) for starship in self.items]


class Person(BaseModel):
    def __init__(self, name, birth_year, eye_color, gender,
                 hair_color, height, mass, skin_color, homeworld,  films, species,
                 starships, vehicles, created, edited, url, **kwargs):

        self.name = name
        self.birth_year = birth_year
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.gender = gender
        self.height = height
        self.mass = mass
        self.skin_color = skin_color
        self.homeworld = self.get_id(homeworld)
        self.films = self.get_ids_list(films)
        self.species = species
        self.starships = self.get_ids_list(starships)
        self.vehicles = self.get_ids_list(vehicles)
        self.created = created
        self.edited = edited
        self.url = url
        self.id = self.get_id(url)


class PersonQuerySet(BaseQuerySet):
    def __init__(self, people):
        super(PersonQuerySet, self).__init__()
        for person in people:
            self.items.append(Person(**person))

    def get_filtered_people(self, starship_id=None, vehicle_id=None, film_id=None, homeworld_id=None):
        people = self.items

        if not (starship_id or vehicle_id or film_id or homeworld_id):
            return people

        filtered_people = []
        for person in people:
           
            if starship_id and starship_id in person.starships:
                filtered_people.append(person)
            if vehicle_id and vehicle_id in person.vehicles:
                filtered_people.append(person)
            if film_id and film_id in person.films:
                filtered_people.append(person)
            if homeworld_id and homeworld_id == person.homeworld:
                filtered_people.append(person)

        return filtered_people


class Film(BaseModel):
    def __init__(self, title, url, **kwargs):
        self.title = title
        self.url = url
        self.id = self.get_id(url)


class FilmQuerySet(BaseQuerySet):
    def __init__(self, films):
        super(FilmQuerySet, self).__init__()
        for film in films:
            self.items.append(Film(**film))

    def get_films_as_choices(self):
        return [(film.id, film.title) for film in self.items]


class Planet(BaseModel):
    def __init__(self, name, url, **kwargs):
        self.name = name
        self.url = url
        self.id = self.get_id(url)


class PlanetQuerySet(BaseQuerySet):
    def __init__(self, planets):
        super(PlanetQuerySet, self).__init__()
        for planet in planets:
            self.items.append(Planet(**planet))

    def get_planets_as_choices(self):
        return [(planet.id, planet.name) for planet in self.items]


class Vehicle(BaseModel):
    def __init__(self, name, url, **kwargs):
        self.name = name
        self.url = url
        self.id = self.get_id(url)


class VehicleQuerySet(BaseQuerySet):
    def __init__(self, vehicles):
        super(VehicleQuerySet, self).__init__()
        for vehicle in vehicles:
            obj = Vehicle(**vehicle)
            self.items.append(obj)

    def get_vehicles_as_choices(self):
        return [(vehicle.id, vehicle.name) for vehicle in self.items]

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

        self.cargo_capacity = cargo_capacity,
        self.consumables = consumables,
        self.cost_in_credits = cost_in_credits,
        self.crew = crew,
        self.created = created,
        self.edited = edited,
        self.hyperdrive_rating = hyperdrive_rating,
        self.length = length,
        self.MGLT = MGLT,
        self.manufacturer = manufacturer,
        self.max_atmosphering_speed = max_atmosphering_speed,
        self.model = model,
        self.name = name,
        self.passengers = passengers,
        self.films = self.get_ids_list(films),
        self.pilots = pilots,
        self.starship_class = starship_class,
        self.url = url,
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


class Person(BaseModel):
    def __init__(self, name, birth_year, eye_color, gender,
                 hair_color, height, mass, skin_color, homeworld,  films, species,
                 starships, vehicles, created, edited, url, **kwargs):

        self.name = name,
        self.birth_year = birth_year,
        self.eye_color = eye_color,
        self.hair_color = hair_color,
        self.gender = gender,
        self.height = height,
        self.mass = mass,
        self.skin_color = skin_color,
        self.homeworld = self.get_id(homeworld),
        self.films = self.get_ids_list(films),
        self.species = species,
        self.starships = self.get_ids_list(starships),
        self.vehicles = self.get_ids_list(vehicles),
        self.created = created,
        self.edited = edited,
        self.url = url,
        self.id = self.get_id(url)


class PersonQuerySet(BaseQuerySet):
    def __init__(self, people):
        super(PersonQuerySet, self).__init__()
        for person in people:
            self.items.append(Person(**person))


class Film(BaseModel):
    def __init__(self, title, url, **kwargs):
        self.title = title,
        self.url = url,
        self.id = self.get_id(url)


class FilmQuerySet(BaseQuerySet):
    def __init__(self, films):
        super(FilmQuerySet, self).__init__()
        for film in films:
            self.items.append(Film(**film))


class Planet(BaseModel):
    def __init__(self, name, url, **kwargs):
        self.name = name,
        self.url = url,
        self.id = self.get_id(url)


class PlanetQuerySet(BaseQuerySet):
    def __init__(self, planets):
        super(PlanetQuerySet, self).__init__()
        for planet in planets:
            self.items.append(Planet(**planet))


class Vehicle(BaseModel):
    def __init__(self, name, url, **kwargs):
        self.name = name,
        self.url = url,
        self.id = self.get_id(url)


class VehicleQuerySet(BaseQuerySet):
    def __init__(self, vehicles):
        super(VehicleQuerySet, self).__init__()
        for vehicle in vehicles:
            self.items.append(Vehicle(**vehicle))

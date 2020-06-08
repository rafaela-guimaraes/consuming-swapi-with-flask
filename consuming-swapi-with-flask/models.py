class BaseQuerySet(object):
    def __init__(self):
        self.items = []

    def order_by(self, order_attr, descending=False):
        return sorted(self.items, key=lambda k: getattr(k, order_attr), reverse=descending)


class Starship():
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
        self.films = films,
        self.pilots = pilots,
        self.starship_class = starship_class,
        self.url = url,
        try:
            self.score = float(hyperdrive_rating) / int(cost_in_credits),
        except:
            self.score = 0,

class StarshipQuerySet(BaseQuerySet):

    def __init__(self, starships):
        super(StarshipQuerySet, self).__init__()
        for starship in starships:
            self.items.append(Starship(**starship))

class Person():
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
        self.homeworld = homeworld,
        self.films = films,
        self.species = species,
        self.starships = starships,
        self.vehicles = vehicles,
        self.created = created,
        self.edited = edited,
        self.url = url

class PersonQuerySet(BaseQuerySet):

    def __init__(self, people):
        super(PersonQuerySet, self).__init__()
        for person in people:
            self.items.append(Person(**person))
    
    def get_all(self):
        return self.items

import traceback
import requests
from models import StarshipQuerySet, PersonQuerySet, FilmQuerySet, PlanetQuerySet, VehicleQuerySet


class Swapi():

    BASE_URL = "https://swapi.dev/api/"

    @classmethod
    def get_all_results(self, endpoint):
        resource = self.do_request("GET", self.BASE_URL + endpoint)
        results = resource['results']
        while resource.get('next') is not None:
            resource = self.do_request("GET", resource['next'])
            results += resource['results']
        return results

    @classmethod
    def get_people(self):
        results = self.get_all_results('people')
        people = PersonQuerySet(results)
        return people

    @classmethod
    def get_starships(self):
        results = self.get_all_results('starships')
        startships = StarshipQuerySet(
            results)
        return startships

    @classmethod
    def get_films(self):
        results = self.get_all_results('films')
        films = FilmQuerySet(results)
        return films

    @classmethod
    def get_vehicles(self):
        results = self.get_all_results('vehicles')
        vehicles = VehicleQuerySet(results)
        return vehicles

    @classmethod
    def get_planets(self, planet_id=None):
        results = self.get_all_results('planets')
        planets = PlanetQuerySet(results)
        return planets


    @classmethod
    def do_request(self, request_method, endpoint):
        response = requests.request(request_method, endpoint)
        try:
            response.raise_for_status()
            return response.json()
        except:
            # TODO(RGuimaraes) improve execption handling
            traceback.print_exc()
            return {'results': []}

import traceback
import requests


from models import StarshipQuerySet, PersonQuerySet
class Swapi():

    BASE_URL = "https://swapi.dev/api/"

    @classmethod
    def get_people(self):
        resource = self.do_request("GET", self.BASE_URL + 'people/')
        results = resource['results']
        while resource.get('next') is not None:
            resource = self.do_request("GET", resource['next'])
            results += resource['results']
        people = PersonQuerySet(results).get_all()
        return people

    @classmethod
    def get_starships(self):
        resource = self.do_request("GET", self.BASE_URL + 'starships/')
        results = resource['results']
        while resource.get('next') is not None:
            resource = self.do_request("GET", resource['next'])
            results += resource['results']
        
        startships = StarshipQuerySet(results).order_by('score', descending=True)
        return startships

    @classmethod
    def get_films(self, film_id=None):
        endpoint = 'films'
        if film_id:
            endpoint += '/{}'.format(film_id)

        results = self.do_request("GET", endpoint)['results']
        return results

    @classmethod
    def get_vehicles(self, vehicle_id=None):
        endpoint = 'vehicles'
        if vehicle_id:
            endpoint += '/{}'.format(vehicle_id)

        results = self.do_request("GET", endpoint)['results']
        return results

    @classmethod
    def get_planets(self, planet_id=None):
        endpoint = 'planets'
        if planet_id:
            endpoint += '/{}'.format(planet_id)

        results = self.do_request("GET", endpoint)['results']
        return results

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

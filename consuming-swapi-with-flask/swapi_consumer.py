import traceback
import requests


class Swapi():

    BASE_URL = "https://swapi.dev/api/"

    @classmethod
    def get_people(self):
        results = self.do_request('GET', 'people')['results']
        return results

    @classmethod
    def get_starships(self, starship_id=None):
        results = self.do_request("GET", 'starships')['results']
        return results

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
    def get_starships(self, starship_id=None):
        endpoint = 'starships'
        if starship_id:
            endpoint += '/{}'.format(starship_id)

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
        response = requests.request(request_method, self.BASE_URL + endpoint)
        try:
            response.raise_for_status()
            return response.json()
        except:
            # TODO(RGuimaraes) improve execption handling
            traceback.print_exc()
            return {'results': []}

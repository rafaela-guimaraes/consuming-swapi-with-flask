from flask import render_template, jsonify
from flask_paginate import Pagination, get_page_args
from swapi_consumer import Swapi
from forms import PeopleFilterForm

STARSHIPS = Swapi.get_starships()
PEOPLE = Swapi.get_people()
VEHICLES = Swapi.get_vehicles()
PLANETS = Swapi.get_planets()
FILMS = Swapi.get_films()


def starships():
    ordered_starships = STARSHIPS.order_by('score', descending=True)
    starships_count = len(ordered_starships)

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    starships_pagination = ordered_starships[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=starships_count,
                            css_framework='bootstrap4')

    return render_template('starships.html',
                           starships=starships_pagination,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


def people(request):
    form = PeopleFilterForm(request.form)
    form.vehicle.choices = [('', '')] + VEHICLES.get_vehicles_as_choices()
    form.planet.choices = [('', '')] + PLANETS.get_planets_as_choices()
    form.film.choices = [('', '')] + FILMS.get_films_as_choices()
    form.starship.choices = [('', '')] + STARSHIPS.get_starships_as_choices()

    filtered_people = PEOPLE.get_filtered_people()
    
    if request.method == 'POST':
        filtered_people = PEOPLE.get_filtered_people(vehicle_id=form.vehicle.data,
                                                     starship_id=form.starship.data,
                                                     homeworld_id=form.planet.data,
                                                     film_id=form.film.data)
    
    people_count = len(filtered_people)

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    people_pagination = filtered_people[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=people_count,
                            css_framework='bootstrap4')

    return render_template('people.html',
                           people=people_pagination,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           filter_form=form
                           )



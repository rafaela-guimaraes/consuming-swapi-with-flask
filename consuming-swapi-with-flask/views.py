from flask import render_template, jsonify
from flask_paginate import Pagination, get_page_args
from swapi_consumer import Swapi

STARSHIPS = Swapi.get_starships()
PEOPLE = Swapi.get_people()
VEHICLES = Swapi.get_vehicles()
PLANETS = Swapi.get_vehicles()
FILMS = Swapi.get_films()


def starships():
    starships_count = len(STARSHIPS)

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    starships_pagination = STARSHIPS[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=starships_count,
                            css_framework='bootstrap4')

    return render_template('starships.html',
                           starships=starships_pagination,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

def people():
    people_count = len(PEOPLE)

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    people_pagination = PEOPLE[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=people_count,
                            css_framework='bootstrap4')

    return render_template('people.html',
                           people=people_pagination,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

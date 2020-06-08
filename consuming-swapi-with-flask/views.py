from flask import render_template, jsonify
from flask_paginate import Pagination, get_page_args
from swapi_consumer import Swapi

STARSHIPS = Swapi.get_starships()


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

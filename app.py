# -*- coding: utf-8 -*-

import bottle
from sys import argv
from utils import DataBase

db = DataBase("food.db")


@bottle.route("/", method="GET")
def index():
    return bottle.template("index")


@bottle.route("/info", method="GET")
def info():
    food = bottle.request.query.get("food")
    impact = db.get_food(food)
    print(impact)

    if impact is not None:
        # still need to check colors
        return bottle.template("info", impact=impact)
    else:
        choices = db.fetch()
        print(choices)
        return bottle.template("error", choices=choices)


@bottle.route("/static/<path:path>", method="GET")
def static(path):
    return bottle.static_file(path, "./static/")


bottle.run(host="0.0.0.0", port=argv[1])

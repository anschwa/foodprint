# -*- coding: utf-8 -*-

import sqlite3


class DataBase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.rows = [("lamb", "meat", 39.2, 10400, "red", "red"),
                     ("beef", "meat", 27, 15400, "red", "red"),
                     ("pork", "meat", 12.1, 6000, "yellow", "yellow"),
                     ("turkey", "meat", 10.9, 4300, "green", "green"),
                     ("chicken", "meat", 6.9, 4300, "green", "green"),
                     ("eggs", "gps", 4.8, 3265, "green", "green"),
                     ("rice", "gps", 2.7, 2500, "red", "green"),
                     ("tofu", "gps", 2, 926, "green", "green"),
                     ("beans", "gps", 2, 4055, "red", "green"),
                     ("lentils", "gps", 0.9, 4055, "red", "green"),
                     ("peanut butter", "gps", 2.9, 628, "green", "green"),
                     ("potatoes", "gps", 2.9, 322, "green", "green"),
                     ("bread", "gps", 0.75, 1608, "yellow", "green"),
                     ("tomatoes", "fruitvegg", 1.1, 322, "green", "green"),
                     ("nuts", "fruitvegg", 2.3, 9063, "red", "yellow"),
                     ("broccoli", "fruitvegg", 2, 322, "green", "green"),
                     ("strawberries", "fruitvegg", 0.3, 322, "green", "green"),
                     ("apple", "fruitvegg", 0.55, 962, "green", "green"),
                     ("milk", "dairy", 1.9, 3180, "yellow", "green"),
                     ("cheese", "dairy", 13.5, 3178, "yellow", "green"),
                     ("yogurt", "dairy", 2.2, 778.05, "green", "green"),
                     ("butter", "dairy", 23.8, 5553, "red", "yellow")]
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("drop table if exists data;")
        sql = """create table if not exists data (
id integer primary key,
food text not null,
type text not null,
co2 decimal not null,
water integer not null,
local text check (local in ('red', 'yellow', 'green')),
global text check (global in ('red', 'yellow', 'green')));"""
        cursor.execute(sql)
        insert = """insert into data (food, type, co2, water, local, global)
values (?,?,?,?,?,?);"""
        cursor.executemany(insert, self.rows)
        conn.commit()
        cursor.close()
        conn.close()

    def get_food(self, food):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        food = food.lower()
        sql = "select * from data where food = ?"
        cursor.execute(sql, (food,))
        result = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        response = None
        if result is not None:
            response = {"id": result[0],
                        "food": result[1],
                        "type": result[2],
                        "carbon": result[3],
                        "water": result[4],
                        "local": result[5],
                        "global": result[6]}

            if response["type"] == "gps":
                response["type"] = "Grains, Proteins, and Starch"
            elif response["type"] == "fruitvegg":
                response["type"] = "Fruits and Vegetables"
            else:
                response["type"] = response["type"].title()
        return response

    def fetch(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("select food from data;")
        response = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return response

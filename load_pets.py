#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sqlite3 as lite

person = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23),
)

pet = (
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1),
)

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6),
)


con = lite.connect('pets')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS person")
    cur.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INT)")
    cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)

    cur.execute("DROP TABLE IF EXISTS pet")
    cur.execute("CREATE TABLE pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INT, dead INT)")
    cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)

    cur.execute("DROP TABLE IF EXISTS person_pet")
    cur.execute("CREATE TABLE person_pet(person_id INT, pet_id INT)")
    cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)

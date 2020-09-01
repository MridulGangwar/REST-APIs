# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:14:20 2020

@author: mgangwar
"""

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES ('chair',349.99)")
cursor.execute("INSERT INTO items VALUES ('juice',13.99)")

connection.commit()
connection.close()
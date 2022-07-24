import sqlite3
from utils.constants import DB_URI

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

users_query = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username VARCHAR(50),
        password TEXT
    )
    """
items_query = """CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        price real
    )
    """


cursor.execute(users_query)
cursor.execute(items_query)
connection.commit()
connection.close()
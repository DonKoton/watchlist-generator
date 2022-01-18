from functions import movies_db_refactor, people_db_refactor, crew_db_refactor, ratings_db_refactor, roles_db_refactor
import sqlite3


connection = sqlite3.connect("data.db")


def movies_db_create():
    df = movies_db_refactor()
    connection.execute("DROP TABLE IF EXISTS movies;")
    connection.commit()
    df.to_sql('movies', con=connection)


def people_db_create():
    df = people_db_refactor()
    connection.execute("DROP TABLE IF EXISTS people;")
    connection.commit()
    df.to_sql('people', con=connection)


def crew_db_create():
    df = crew_db_refactor()
    connection.execute("DROP TABLE IF EXISTS crew;")
    connection.commit()
    df.to_sql('crew', con=connection)


def ratings_db_create():
    df = ratings_db_refactor()
    connection.execute("DROP TABLE IF EXISTS ratings;")
    connection.commit()
    df.to_sql('ratings', con=connection)


def roles_db_create():
    df = roles_db_refactor()
    connection.execute("DROP TABLE IF EXISTS roles;")
    connection.commit()
    df.to_sql('roles', con=connection)


movies_db_create()
people_db_create()
crew_db_create()
ratings_db_create()
roles_db_create()




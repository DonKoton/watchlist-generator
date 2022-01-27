import sqlite3
from random import sample
from copy import copy
from watchlist.models import Movies, People


connection = sqlite3.connect("data.db", check_same_thread=False)

get_movies_stmt = """
SELECT DISTINCT movies.primaryTitle, movies.startYear, movies.tconst FROM movies
INNER JOIN ratings ON ratings.tconst = movies.tconst
INNER JOIN roles ON roles.tconst = movies.tconst
INNER JOIN crew ON crew.tconst = movies.tconst
INNER JOIN people ON people.nconst = roles.nconst
WHERE averageRating >= ?"""

get_people_stmt = """
SELECT DISTINCT movies.primaryTitle, movies.startYear, movies.tconst FROM movies
INNER JOIN ratings ON ratings.tconst = movies.tconst
INNER JOIN roles ON roles.tconst = movies.tconst
INNER JOIN crew ON crew.tconst = movies.tconst
INNER JOIN people ON people.nconst = roles.nconst
WHERE averageRating >= ?"""

truncate_movies = "DELETE FROM watchlist_movies;"
truncate_people = "DELETE FROM watchlist_people;"


def drop_tables():
    connection2 = sqlite3.connect("db.sqlite3")

    with connection2:
        connection2.execute(truncate_movies)
        connection2.execute(truncate_people)


gms_copy = copy(get_movies_stmt)
gps_copy = copy(get_people_stmt)


def get_movies():
    global gms_copy

    parameters = []

    rating = Movies.objects.last().movie_rating
    if rating:
        parameters.append(str(rating))

    try:
        votes = Movies.objects.last().movie_votes
        if votes:
            gms_copy += ' AND ratings.numVotes >= ?'
            parameters.append(str(votes))
    except AttributeError:
        pass

    try:
        genre = Movies.objects.last().genre
        if genre:
            gms_copy += ' AND genres LIKE ?'
            genre = '%' + genre + '%'
            parameters.append(genre)
    except AttributeError:
        pass

    try:
        prod_year = Movies.objects.last().prod_year
        if prod_year:
            gms_copy += ' AND movies.startYear >= ?'
            parameters.append(str(prod_year))
    except AttributeError:
        pass

    number_of_movies_to_choose = Movies.objects.last().number_of_movies_to_choose

    with connection:
        result = connection.execute(gms_copy, parameters)
        result = result.fetchall()
        result = sample(result, k=number_of_movies_to_choose)

    parameters.clear()
    gms_copy = get_movies_stmt

    return result


def get_people():
    global gps_copy

    parameters = []

    rating = People.objects.last().people_rating
    if rating:
        parameters.append(str(rating))

    try:
        votes = People.objects.last().people_votes
        if votes:
            gps_copy += ' AND ratings.numVotes >= ?'
            parameters.append(str(votes))
    except AttributeError:
        pass

    try:
        role = People.objects.last().role
        if role:
            gps_copy += ' AND roles.category LIKE ?'
            role = '%' + role + '%'
            parameters.append(role)
    except AttributeError:
        pass

    try:
        name = People.objects.last().name
        if name:
            gps_copy += ' AND people.primaryName = ?'
            parameters.append(name)
    except AttributeError:
        pass

    try:
        birth_year = People.objects.last().birth_year
        if birth_year:
            gps_copy += ' AND people.birthYear = ?'
            parameters.append(birth_year)
    except AttributeError:
        pass

    number_of_movies_to_choose = People.objects.last().number_of_movies_to_choose

    with connection:
        result = connection.execute(gps_copy, parameters)
        result = result.fetchall()
        result = sample(result, k=number_of_movies_to_choose)

    parameters.clear()
    gps_copy = get_people_stmt

    return result


if __name__ == '__main__':
    get_movies()
    get_people()
    drop_tables()
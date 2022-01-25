import sqlite3
from random import sample
from copy import copy
from watchlist.models import Movies


connection = sqlite3.connect("data.db", check_same_thread=False)

get_movies_stmt = """
SELECT DISTINCT movies.primaryTitle, movies.startYear, movies.tconst FROM movies
INNER JOIN ratings ON ratings.tconst = movies.tconst
INNER JOIN roles ON roles.tconst = movies.tconst
INNER JOIN crew ON crew.tconst = movies.tconst
INNER JOIN people ON people.nconst = roles.nconst
WHERE averageRating >= ?"""

gms_copy = copy(get_movies_stmt)


def get_movies():
    global gms_copy

    rating = Movies.objects.last().rating
    parameters = [str(rating)]

    votes = Movies.objects.last().votes
    if votes:
        gms_copy += ' AND ratings.numVotes >= ?'
        parameters.append(str(votes))

    genre = Movies.objects.last().genre
    if genre:
        gms_copy += ' AND genres LIKE ?'
        genre = '%' + genre + '%'
        parameters.append(genre)

    prod_year = Movies.objects.last().prod_year
    if prod_year:
        gms_copy += ' AND movies.startYear >= ?'
        parameters.append(str(prod_year))

    role = Movies.objects.last().role
    if role:
        gms_copy += ' AND roles.category LIKE ?'
        role = '%' + role + '%'
        parameters.append(role)

    name = Movies.objects.last().name
    if name:
        gms_copy += ' AND people.primaryName = ?'
        parameters.append(name)

    birth_year = Movies.objects.last().birth_year
    if birth_year:
        gms_copy += ' AND people.birthYear = ?'
        parameters.append(birth_year)

    number_of_movies_to_choose = Movies.objects.last().number_of_movies_to_choose

    with connection:
        result = connection.execute(gms_copy, parameters)
        result = result.fetchall()
        result = sample(result, k=number_of_movies_to_choose)

    parameters.clear()
    gms_copy = get_movies_stmt

    return result

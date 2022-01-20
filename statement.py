import sqlite3
from random import sample
from watchlist.models import Movies


connection = sqlite3.connect("data.db")

get_movies_stmt = """
SELECT movies.primaryTitle, ratings.averageRating FROM movies
INNER JOIN ratings ON ratings.tconst = movies.tconst
INNER JOIN roles ON roles.tconst = movies.tconst
INNER JOIN crew ON crew.tconst = movies.tconst
INNER JOIN people ON people.nconst = roles.nconst
WHERE averageRating >= ?
AND ratings.numVotes >= ?
AND genres LIKE ?
AND movies.startYear >= ?
AND roles.category LIKE ?
AND people.primaryName = ?
AND people.birthYear = ?"""


def get_movies():
    Movies.objects.all().delete()

    rating = Movies.objects.all()[0]['averageRatzing'].fetchone()
    votes = Movies.objects.get().fetchone()
    genre = Movies.objects.get().fetchone()
    prod_year = Movies.objects.get().fetchone()
    role = Movies.objects.get().fetchone()
    name = Movies.objects.get().fetchone()
    birth_year = Movies.objects.get().fetchone()
    number_of_movies_to_choose = Movies.objects.all()

    genre = '%' + genre + '%'
    role = '%' + role + '%'

    with connection:
        result = connection.execute(get_movies_stmt, (rating, votes, genre, prod_year, role, name, birth_year))
    result = result.fetchall()
    result = sample(result, k=number_of_movies_to_choose)

    return result

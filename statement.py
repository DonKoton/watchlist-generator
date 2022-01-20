import sqlite3
from random import sample
from pprint import pprint
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
    rating = Movies.objects.get().fetchone()
    votes = Movies.objects.get().fetchone()
    genre = Movies.objects.get().fetchone()
    prod_year = Movies.objects.get().fetchone()
    role = Movies.objects.get().fetchone()
    name = Movies.objects.get().fetchone()
    birth_year = Movies.objects.get().fetchone()

    genre = '%' + genre + '%'
    role = '%' + role + '%'

    with connection:
        result = connection.execute(get_movies_stmt, (rating, votes, genre, prod_year, role, name, birth_year))
    return result.fetchall()


try:
    pprint(sample(get_movies(), k=15))
except ValueError:
    print(f"Not enough movies matching selected filters! There are only {len(get_movies())} movies matching.")


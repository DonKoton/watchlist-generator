import sqlite3
from random import sample
from pprint import pprint


connection = sqlite3.connect("data.db")

get_movies_stmt = """
SELECT movies.primaryTitle, ratings.averageRating FROM movies
INNER JOIN ratings ON ratings.tconst = movies.tconst
INNER JOIN roles ON roles.tconst = movies.tconst
INNER JOIN crew ON crew.tconst = movies.tconst
INNER JOIN people ON people.nconst = roles.nconst
WHERE averageRating >= ?
AND ratings.numVotes > ?
AND genres LIKE ?
AND movies.startYear >= ?
AND roles.category LIKE ?
AND people.primaryName = ?
AND people.birthYear = ?"""


def get_movies(rating: float, votes: int, genre: str, prod_year: int, role: str, name: str, birth_year):
    genre = '%' + genre + '%'
    role = '%' + role + '%'

    with connection:
        result = connection.execute(get_movies_stmt, (rating, votes, genre, prod_year, role, name, birth_year))
    return result.fetchall()


list_of_movies = get_movies(6.0, 5000, '', 1970, 'actor', 'Dwayne Johnson', 1972)
try:
    pprint(sample(list_of_movies, k=15))
except ValueError:
    print(f"Not enough movies matching selected filters! There are only {len(list_of_movies)} movies matching.")


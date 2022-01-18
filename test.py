import sqlite3
from random import sample
from pprint import pprint

connection = sqlite3.connect("data.db")

get_movies_stmt = "SELECT * FROM movies INNER JOIN ratings ON ratings.tconst = movies.tconst WHERE averageRating > 7.0 AND genres LIKE ? AND movies.startYear > 2000 AND ratings.numVotes > 20000"


def genre(kword):
    kword = '%' + kword + '%'

    with connection:
        result = connection.execute(get_movies_stmt, (kword,))
    return result.fetchall()


list_of_movies = genre('war')
pprint(sample(list_of_movies, k=7))
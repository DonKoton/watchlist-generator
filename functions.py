import requests
import gzip
import shutil
import pandas as pd
from skip_download import read_timestamp


url_people = "https://datasets.imdbws.com/name.basics.tsv.gz"
url_movies = "https://datasets.imdbws.com/title.basics.tsv.gz"
url_rating = "https://datasets.imdbws.com/title.ratings.tsv.gz"
url_roles = "https://datasets.imdbws.com/title.principals.tsv.gz"
url_crew = "https://datasets.imdbws.com/title.crew.tsv.gz"

urls = [url_people, url_crew, url_roles, url_rating, url_movies]


def download_and_unpack():
    result = read_timestamp()
    if result > 86400:
        for url in urls:
            filename_tsv = url.split("/")[-1][:-3]
            filename_gz = 'zipped/' + filename_tsv + '.gz'

            with open(filename_gz, "wb") as f:
                r = requests.get(url)
                f.write(r.content)

            with gzip.open(filename_gz, 'rb') as f_in:
                with open('unpacked/' + filename_tsv, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)


def movies_db_refactor():
    # movies manipulation
    df = pd.read_csv('unpacked/title.basics.tsv', sep='\t', index_col="tconst")
    df = df.drop(['originalTitle', 'isAdult', 'endYear', 'runtimeMinutes'], axis=1)
    df = df.loc[df['titleType'] == 'movie']
    df = df.drop('titleType', axis=1)
    df = df.loc[df['genres'] != '\\N']
    df = df.loc[df['startYear'] != '\\N']
    df['startYear'] = df['startYear'].astype(int)
    df = df.loc[df['startYear'] > 1960]
    return df


def people_db_refactor():
    # people manipulation
    df = pd.read_csv('unpacked/name.basics.tsv', sep='\t')
    df = df.drop(['deathYear', 'knownForTitles'], axis=1)
    df = df.loc[df['birthYear'] != '\\N']
    df['birthYear'] = df['birthYear'].astype(int)
    df = df.dropna()
    df = df.set_index('primaryProfession').filter(regex='.*actor.*|.*actress.*|.*[^_]director.*', axis=0)
    df = df.reset_index().set_index('nconst')
    return df


def crew_db_refactor():
    # crew manipulation
    df = pd.read_csv('unpacked/title.crew.tsv', sep='\t', index_col="tconst")
    df = df.drop(['writers'], axis=1)
    df = df.loc[df['directors'] != '\\N']
    return df


def ratings_db_refactor():
    # ratings manipulation
    df = pd.read_csv('unpacked/title.ratings.tsv', sep='\t', index_col="tconst")
    df['averageRating'] = df['averageRating'].astype(float)
    df['numVotes'] = df['numVotes'].astype(int)
    df = df.loc[df['numVotes'] > 1000]
    return df


def roles_db_refactor():
    # roles manipulation
    df = pd.read_csv('unpacked/title.principals.tsv', sep='\t', index_col="tconst")
    df = df.drop(['job', 'characters', 'ordering'], axis=1)
    df = df.query('category == ["actor", "actress", "director"]')
    return df


if __name__ == '__main__':
    download_and_unpack()
    movies_db_refactor()
    people_db_refactor()
    crew_db_refactor()
    ratings_db_refactor()
    roles_db_refactor()

from copy import copy

import requests
from bs4 import BeautifulSoup
from django.shortcuts import redirect
from django.shortcuts import render

from statement import get_movies
from watchlist.forms import MoviesForm


def index(request):
    if request.method == "POST":
        form = MoviesForm(request.POST)
        form.save()

        return redirect('watchlist:result')

    form = MoviesForm()

    return render(
        request,
        'watchlist/index.html',
        context={
            "form": form
        }
    )


def result(request):
    list_of_movies = get_movies()

    for idx, movie in enumerate(copy(list_of_movies)):
        list_of_movies[idx] = list(list_of_movies[idx])
        list_of_movies[idx][2] = 'https://www.imdb.com/title/' + movie[2] + '/'
        list_of_movies[idx].append('https://www.imdb.com/title/' + movie[2] + '/mediaindex')

    list_of_urls = [images_url[3] for images_url in list_of_movies]

    list_of_sources = []

    for url in list_of_urls:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        images = soup.find_all("img", attrs={"class": "poster"})
        image_src = images[0]['src']

        list_of_sources.append(image_src)

    list_of_movies = [list_of_movies[i][:3] + [list_of_sources[i]] for i in range(len(list_of_movies))]

    return render(
        request,
        'watchlist/result.html',
        context={
            "list_of_movies": list_of_movies
        }
    )

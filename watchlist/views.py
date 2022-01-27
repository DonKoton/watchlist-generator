from copy import copy

import requests
from bs4 import BeautifulSoup
from django.shortcuts import redirect
from django.shortcuts import render

from statement import get_movies, get_people, drop_tables
from watchlist.forms import MoviesForm, PeopleForm, RadioSelect


def home(request):
    return render(
        request,
        'watchlist/home.html'
    )


def forms(request):
    radio_form = RadioSelect()

    return render(
        request,
        'watchlist/forms.html',
        context={
            "radio_form": radio_form
        }
    )


def forms_movies(request):
    if request.method == "POST":

        movies_form = MoviesForm(request.POST)

        if movies_form.is_valid():
            movies_form.save()

        return redirect('watchlist:result_movies')

    movies_form = MoviesForm()

    return render(
        request,
        'watchlist/forms_movies.html',
        context={
            "movies_form": movies_form,
        }
    )


def forms_people(request):
    if request.method == "POST":

        people_form = PeopleForm(request.POST)

        if people_form.is_valid():
            people_form.save()

        return redirect('watchlist:result_people')

    people_form = PeopleForm()

    return render(
        request,
        'watchlist/forms_people.html',
        context={
            "people_form": people_form,
        }
    )


def result_movies(request):
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

    drop_tables()

    return render(
        request,
        'watchlist/result_movies.html',
        context={
            "list_of_movies": list_of_movies
        }
    )


def result_people(request):
    list_of_people = get_people()

    for idx, movie in enumerate(copy(list_of_people)):
        list_of_people[idx] = list(list_of_people[idx])
        list_of_people[idx][2] = 'https://www.imdb.com/title/' + movie[2] + '/'
        list_of_people[idx].append('https://www.imdb.com/title/' + movie[2] + '/mediaindex')

    list_of_urls = [images_url[3] for images_url in list_of_people]

    list_of_sources = []

    for url in list_of_urls:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        images = soup.find_all("img", attrs={"class": "poster"})
        image_src = images[0]['src']

        list_of_sources.append(image_src)

    list_of_people = [list_of_people[i][:3] + [list_of_sources[i]] for i in range(len(list_of_people))]

    drop_tables()

    return render(
        request,
        'watchlist/result_people.html',
        context={
            "list_of_people": list_of_people
        }
    )

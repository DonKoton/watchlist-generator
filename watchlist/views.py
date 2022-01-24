from copy import copy

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

    for idx, el in enumerate(copy(list_of_movies)):
        list_of_movies[idx] = list(list_of_movies[idx])
        list_of_movies[idx][2] = 'https://www.imdb.com/title/' + el[2] + '/'

    return render(
        request,
        'watchlist/result.html',
        context={
            "list_of_movies": list_of_movies
        }
    )

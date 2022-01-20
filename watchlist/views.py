from django.shortcuts import render
from django.shortcuts import redirect
from watchlist.forms import MoviesForm
from statement import get_movies
from watchlist.models import Movies


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

    return render(
        request,
        'watchlist/result.html',
        context={
            "list_of_movies": list_of_movies
        }
    )

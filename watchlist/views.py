from django.shortcuts import render
from django.shortcuts import redirect
from watchlist.forms import MoviesForm
from statement import get_movies


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
    list_of_movies = [movie[0] + ' ----- ' + str(movie[1]) for movie in get_movies()]

    return render(
        request,
        'watchlist/result.html',
        context={
            "list_of_movies": list_of_movies
        }
    )

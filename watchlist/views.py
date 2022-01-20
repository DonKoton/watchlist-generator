from django.shortcuts import render
from django.shortcuts import redirect
from watchlist.forms import MoviesForm


def index(request):

    if request.method == "POST":
        form = MoviesForm(request.POST)
        form.save()

        return redirect('watchlist:index')

    form = MoviesForm()

    return render(
        request,
        'watchlist/index.html',
        context={
            "form": form
        }
    )

from django.shortcuts import render
from django.shortcuts import redirect
from forms import MoviesForm


def index(request):

    if request.method == "POST":
        form = MoviesForm(request.POST)
        form.save()

        return redirect('form_app_advanced:contact3')

    form = MoviesForm()

    return render(
        request,
        'watchlist/index.html',
        context={
            "form": form
        }
    )

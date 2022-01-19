from django import forms
from watchlist.models import Movies


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"
        labels = {
            "rating": "Average rating",
            "votes": "Number of votes",
            "genre": "Movie genre",
            "prod_year": "Year of production",
            "role": "Role in the movie",
            "name": "Name of person",
            "birth_year": "Date of birth",
        }

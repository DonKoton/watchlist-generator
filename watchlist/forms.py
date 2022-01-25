from django import forms
from watchlist.models import Movies


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"
        labels = {
            "rating": "Average rating (min)",
            "votes": "Number of votes (min)",
            "genre": "Movie genre",
            "prod_year": "Year of production (min)",
            "role": "Role in the movie",
            "name": "Name of person",
            "birth_year": "Date of birth",
        }

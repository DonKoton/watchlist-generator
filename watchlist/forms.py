from django import forms

from database import get_max_votes_num
from functions import cur_date
from watchlist.models import Movies, People


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"
        labels = {
            "rating": "Average rating (min)",
            "votes": "Number of votes (min)",
            "genre": "Movie genre",
            "prod_year": "Year of production (min)"
        }
        widgets = {
            "rating": forms.TextInput(attrs={"placeholder": "1 - 10"}),
            "votes": forms.TextInput(attrs={"placeholder": f"1000 - {get_max_votes_num()}"}),
            "prod_year": forms.TextInput(attrs={"placeholder": f"1960 - {cur_date()}"})
        }


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = "__all__"
        labels = {
            "rating": "Average rating (min)",
            "role": "Role in the movie",
            "name": "Name of person",
            "birth_year": "Year of birth"
        }
        widgets = {
            "rating": forms.TextInput(attrs={"placeholder": "1 - 10"}),
            "name": forms.TextInput(attrs={"placeholder": "John Doe/Bruce Lee"}),
            "birth_year": forms.TextInput(attrs={"placeholder": f"1900 - {cur_date()-1}"})
        }


class RadioSelect(forms.Form):
    choices = (('movies', 'Filter by movies'), ('people', 'Filter by people'))
    radio_select = forms.ChoiceField(choices=choices, initial=0, widget=forms.RadioSelect)

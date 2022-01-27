from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic.base import RedirectView


from watchlist import views

app_name = "watchlist"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('forms/', views.forms, name='forms'),
    path('forms/movies_form/', views.forms_movies, name='forms_movies'),
    path('forms/people_form/', views.forms_people, name='forms_people'),
    path('generated_by_movies/', views.result_movies, name='result_movies'),
    path('generated_by_people/', views.result_people, name='result_people'),

]

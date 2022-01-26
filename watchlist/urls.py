from django.urls import path

from watchlist import views

app_name = "watchlist"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('forms/', views.forms, name='forms'),
    path('generated_list/', views.result, name='result')
]
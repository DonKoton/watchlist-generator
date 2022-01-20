from django.urls import path

from watchlist import views

app_name = "watchlist"

urlpatterns = [
    path('', views.index, name="index"),
    path('generated_list/', views.result, name='result'),
]
from django.urls import path, include

from . import views

app_name = "voting"

urlpatterns = [
    path("", views.index, name="index"),
    path("cuartooscuro", views.vote, name="vote"),
    path("urna", views.setvote, name="setvote"),
    path("resultados", views.results, name="results")
]

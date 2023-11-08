from django.contrib import admin
from django.urls import path

from familia.views import listar_familiares

urlpatterns = [
    path("familiares/", listar_familiares)
]
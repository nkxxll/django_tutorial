from django.urls import path

from . import views

app_name = "counter"
urlpatterns = [
    path("", views.index, name="index"),
    path("plus/", views.plus, name="plus"),
    path("minus/", views.minus, name="minus"),
]

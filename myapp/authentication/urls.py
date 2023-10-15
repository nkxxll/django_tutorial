from django.urls import path

from . import views

app_name = "authentication"
urlpatterns = [
    # ex: /polls/
    # you could use the generic view IndexView.as_view()
    path("", views.index, name="index"),
    path("login/", views.login_func, name="login"),
]

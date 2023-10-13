from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    # you could use the generic view IndexView.as_view()
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # ex: /polls/5/
    path("gen/", views.IndexView.as_view(), name="indexGen"),
    path("gen/<int:question_id>/", views.DetailView.as_view(), name="detailGen"),
    # ex: /polls/5/results/
    path("gen/<int:question_id>/results/",
         views.ResultsView.as_view(), name="resultsGen"),
    # ex: /polls/5/vote/
]

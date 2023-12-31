from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("search", views.SearchView.as_view(), name="search"),
    path("<pk>", views.SingleSearch.as_view(), name="single_search"),
]

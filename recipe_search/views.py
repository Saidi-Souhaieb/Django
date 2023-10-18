from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .forms import FormTopics
from .models import Topics, Recipes
from django.core.paginator import Paginator

from django.urls import reverse

# Create your views here.


class IndexView(View):
    def get(self, request):
        topics = Topics.objects.all()
        topic_form = FormTopics()
        context = {
            "topics": topics,
            "form": topic_form
        }
        return render(request, "recipe_search/index.html", context)

    def post(self, request):
        return render(request, "recipe_search/search_result.html")


# def get_recipe(request):
#     topic = request.POST.get("topic")
#     form = FormTopics(request.POST)
#     search_title = form["name"].value()
#     recipes = ""
#     if search_title:
#         search_title.replace(" ", "")
#         recipes = Recipes.objects.filter(
#             topic=topic, title__icontains=search_title)
#     elif topic:
#         recipes = Recipes.objects.filter(
#             topic=topic)
#     recipe_count = 0
#     if not search_title and not topic:
#         recipes = Recipes.objects.all()
#     if recipes:
#         recipe_count += recipes.count()
#     # Set up pagination
#     p = Paginator(recipes, 3)
#     page = request.GET.get("page")
#     recipe = p.get_page(page)
#     return [recipe, recipe_count]

def get_context(request, topic, search_title):
    recipes = ""
    if search_title:
        search_title.replace(" ", "")
        if topic:
            recipes = Recipes.objects.filter(
                topic=topic, title__icontains=search_title)
        else:
            recipes = Recipes.objects.filter(title__icontains=search_title)
    elif topic:
        recipes = Recipes.objects.filter(
            topic=topic)
    recipe_count = 0
    if not search_title and not topic:
        recipes = Recipes.objects.all()
    if recipes:
        recipe_count += recipes.count()
    # Set up pagination
    p = Paginator(recipes, 3)
    page = request.GET.get("page")
    recipe = p.get_page(page)
    return {"recipe": recipe, "count": recipe_count}


class SearchView(View):

    def get(self, request):
        topic = request.session["recipe"][0]
        search_title = request.session["recipe"][1]
        context = get_context(request, topic, search_title)

        return render(request, "recipe_search/search_result.html", context)

    def post(self, request):
        topic = request.POST.get("topic")
        form = FormTopics(request.POST)
        search_title = form["name"].value()
        context = get_context(request, topic, search_title)
        request.session["recipe"] = [topic, search_title]
        return render(request, "recipe_search/search_result.html", context)


class SingleSearch(DetailView):
    template_name = "recipe_search/recipe.html"
    model = Recipes
    context_object_name = "recipe"

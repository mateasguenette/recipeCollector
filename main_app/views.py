from multiprocessing.spawn import import_main_path
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import recipe
# Create your views here.

# class recipe:
#     def __init__(self, name, type, description):
#         self.name = name
#         self.type = type
#         self.description = description

# recipe = [
#     recipe('recipe 1',' desert', 'description'),
#     recipe('recipe 2',' main', 'description'),
#     recipe('recipe 3',' entre', 'description')
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipe_index(request):
    recipes = recipe.objects.all()
    return render(request, 'recipe/index.html', {'recipes': recipes})
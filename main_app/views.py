from dataclasses import field, fields
from multiprocessing.spawn import import_main_path
from pyexpat import model
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import recipe, Food
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

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

class recipeCreate(CreateView):
    model = recipe
    fields = '__all__'
    

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipe_index(request):
    recipes = recipe.objects.all()
    return render(request, 'recipe/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe1 = recipe.objects.get(id=recipe_id)
    feeding_form = FeedingForm()
    food_cat_doesnt_have = Food.objects.exclude(id__in = recipe1.Food.all().values_list('id'))

    return render(request, 'recipe/detail.html', {'recipe': recipe1, 'feeding_form': feeding_form, 'food_cat_doesnt_have': food_cat_doesnt_have})

class recipeUpdate(UpdateView):
    model = recipe
    fields = ['name', 'type', 'description']

class recipeDelete(DeleteView):
    model = recipe
    success_url = '/recipe/'

def add_feeding(request, recipe_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.recipe2_id = recipe_id
        new_feeding.save()
    return redirect('detail', recipe_id=recipe_id)

def assoc_toy(request, recipe_id, food_id):
  # Note that you can pass a toy's id instead of the whole object
  recipe.objects.get(id=recipe_id).toys.add(food_id)
  return redirect('detail', recipe_id=recipe_id)
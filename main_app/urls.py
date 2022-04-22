from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about' ),
    path('recipe/', views.recipe_index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='detail'),
    path('recipe/create/', views.recipeCreate.as_view(), name='recipe_create'),

    #Updating & Deleting Data Using a CBV
    path('cats/<int:pk>/update', views.recipeUpdate.as_view(), name='recipe_update'),
    path('recipe/<int:pk>/delete', views.recipeDelete.as_view(), name='recipe_delete'),

    path('recipe/<int:recipe_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('recipe/<int:recipe_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),
    path('accounts/', include('django.contrib.auth.urls')),
]
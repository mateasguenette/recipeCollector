from django.contrib import admin

from main_app.models import recipe, Feeding, Food

# Register your models here.
admin.site.register(recipe)

admin.site.register(Feeding)

admin.site.register(Food)
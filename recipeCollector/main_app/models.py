from django.db import models

# Create your models here.
class recipe(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

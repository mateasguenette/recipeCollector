from unicodedata import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# A tuple of 2-tuples
EVENTS = (
    ('B', 'BirthDay'),
    ('r', 'religiousceremonie'),
    ('D', 'DinnerParty')
)
class Food(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Create your models here.
class recipe(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    foods = models.ManyToManyField(Food)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})

class Feeding(models.Model):
  date = models.DateField()
  event = models.CharField(
    max_length=1,
	 choices=EVENTS,
	 default=EVENTS[0][0]
  )
  recipe2 = models.ForeignKey(recipe, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.event()} on {self.date}"
    

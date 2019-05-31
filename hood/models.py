from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Neighborhood(models.Model):
  name=models.CharField(max_length=50)
  hood_image=models.ImageField(upload_to='hood/',default='city.jpeg')
  members=models.IntegerField()

  def __str__(self):
    self.name

class NeighborProfile(models.Model):
  name=models.CharField(max_length=60)
  neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
  email=models.CharField(max_length=100)

  def __str__(self):
    self.name

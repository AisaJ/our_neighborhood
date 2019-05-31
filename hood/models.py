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
  def save_hood(self):
    self.save()

class NeighborProfile(models.Model):
  name=models.CharField(max_length=60)
  neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
  email=models.CharField(max_length=100)

  def __str__(self):
    self.name
  def save_neighbour(self):
    self.save()

class Business(models.Model):
  name=models.CharField(max_length=50)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
  description=HTMLField()
  business_mail=models.CharField(max_length=100)

  def __str__(self):
    self.name
  def save_business(self):
    self.save()
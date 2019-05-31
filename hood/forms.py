from django import forms
from .models import Neighborhood,NeighborProfile,Business

class NewHoodForm(forms.ModelForm):
  class Meta:
    model=Neighborhood

class NewProfileForm(forms.ModelForm):
  class Meta:
    model=NeighborProfile
    exclude=['neighborhood']

class NewBusinessForm(forms.ModelForm):
  class Meta:
    model=Business
    exclude=['user','neighborhood']
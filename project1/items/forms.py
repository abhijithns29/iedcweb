

# forms.py
from django import forms
from .models import items  # Import your model

INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'

class NewitemForm(forms.ModelForm):
    class Meta:
        model = items  # Specify the model
        fields = ('category','name','decription','price','image')  # List the fields to include in the form
    
        widgets ={
              'category':forms.Select(attrs={
              'class':INPUT_CLASSES
             }),
              'name':forms.TextInput(attrs={
              'class':INPUT_CLASSES
             }),
              'decription':forms.Textarea(attrs={
              'class':INPUT_CLASSES
             }),
              'price':forms.TextInput(attrs={
              'class':INPUT_CLASSES
             }),
              'image':forms.FileInput(attrs={
              'class':INPUT_CLASSES
             })
        }


class EdititemForm(forms.ModelForm):
    class Meta:
        model = items  # Specify the model
        fields = ('name','decription','price','image','is_sold')  # List the fields to include in the form
    
        widgets ={
              'name':forms.TextInput(attrs={
              'class':INPUT_CLASSES
             }),
              'decription':forms.Textarea(attrs={
              'class':INPUT_CLASSES
             }),
              'price':forms.TextInput(attrs={
              'class':INPUT_CLASSES
             }),
              'image':forms.FileInput(attrs={
              'class':INPUT_CLASSES
             })
        }
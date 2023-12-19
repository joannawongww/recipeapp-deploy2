from django import forms
from django.shortcuts import render
from .models import Recipe

CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

DIFF__CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard'),

)

# class-based Form


class RecipeSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFF__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class CreateRecipeForm(forms.Form):
    name = forms.CharField(max_length=50)
    cooking_time = forms.IntegerField(help_text='in mins')
    ingredients = forms.CharField(max_length=300, help_text='Separate by a comma and a space')
    
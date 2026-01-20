from django import forms

class ThingForm(forms.Form):
    Title = forms.CharField(max_length=10,min_length=3)
    description = forms.CharField(max_length=200)
    value = forms.IntegerField()
    photo = forms.ImageField()
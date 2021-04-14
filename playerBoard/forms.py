from django import forms
from django.forms import ModelForm, fields
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"
        widgets = {"name": forms.TextInput(attrs={"class": "nameInput"})}

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = False

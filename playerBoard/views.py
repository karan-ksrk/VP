from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm


def index(request):
    players = Player.objects.all()

    form = PlayerForm()

    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(request.POST)
        return redirect("/")

    context = {"players": players, "form": form}
    return render(request, "playerBoard/index.html", context=context)

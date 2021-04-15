from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm


def index(request):
    players = Player.objects.all()

    form = PlayerForm()

    if request.method == "POST" and "addPerson" in request.POST:
        print(request.POST)
        change_request = request.POST.copy()
        change_request.update({"points": 0})
        form = PlayerForm(data=change_request)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            print(form.cleaned_data)
        return redirect("/")

    if request.method == "POST" and "deletePerson" in request.POST:
        item_id = request.POST["playerID"]
        print(item_id)
        player = Player.objects.get(id=int(item_id))
        player.delete()
        return redirect("/")

    context = {"players": players, "form": form}
    return render(request, "playerBoard/index.html", context=context)


def updatePlayer(request, pk):
    player = Player.objects.get(id=pk)

    form = PlayerForm(instance=player)

    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}

    return render(request, "playerBoard/update_player.html", context=context)

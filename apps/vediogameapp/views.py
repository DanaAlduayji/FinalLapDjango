from django.shortcuts import render
from .models import Developer, Game
# Create your views here.

def landingpage(request):
    return render(request , 'vediogameapp/landingpage.html')

def list(request):

    games = Game.objects.all()

    return render(request, 'vediogameapp/listpage.html', {'games': games})
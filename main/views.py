from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Szin, Meret, Termek, Kategoria, Color

# Create your views here.
def homepage(request):
    termekek = Termek.objects.all()
    kategoriak = Kategoria.objects.all()
    context = {
        'termekek': termekek,
        'kategoriak': kategoriak,
    }

    return render(request, 'main/home.html', context)



def kapcsolat(request):

    return render(request, 'main/kapcsolat.html')

def rolunk(request):
    return render(request, 'main/rolunk.html')



def kategoriak(request,id, slug):
    kategoria = Kategoria.objects.filter(id=id)
    kat = kategoria.first()

    boritokep = ""
    for foo in kategoria:
        boritokep = foo.borito

    context = {
        'kategoria': kategoria,
        'boritokep': boritokep,
        'kat': kat,
    }
    return render(request, 'main/kategoriak.html', context)

def termekek(request, id, slug):
    termekek = Termek.objects.filter(kategoria_id=id).order_by("sorrend")
    kat = Kategoria.objects.filter(id=id).first()
    colors = Color.objects.filter(szin=id)


    context = {
        'termekek': termekek,
        'kat': kat,
        'colors': colors,
    }
    return render(request, 'main/termekek.html', context)


def viszonteladoknak(request):

    return render(request, 'main/viszonteladoknak.html')

def cegeknek(request):
    uzenet = "Cégeknek oldal"
    context = {
        'uzenet': uzenet,
    }
    return render(request, 'main/cegeknek.html', context)

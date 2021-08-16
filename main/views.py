from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Szin, Meret, Termek, Kategoria, Color, Carousel

# Create your views here.
def homepage(request):
    carousels = Carousel.objects.all()
    termekek = Termek.objects.all()
    kategoriak = Kategoria.objects.all()
    context = {
        'termekek': termekek,
        'kategoriak': kategoriak,
        'carousels': carousels,
    }

    return render(request, 'main/home.html', context)


def kapcsolat(request):
    return render(request, 'main/kapcsolat.html')

def rolunk(request):
    return render(request, 'main/rolunk.html')


def kategoriak(request, category_id, category_slug):
    categories = Kategoria.objects.filter(id=category_id)
    termekek = Termek.objects.filter(kategoria_id__in=categories.get_descendants())
    boritokep = ""

    for foo in categories:
        boritokep = foo.borito

    context = {
        'categories': categories,
        'termekek': termekek,
        'boritokep': boritokep,
    }
    return render(request, 'main/kategoriak.html', context)

def termekek(request, category_id, category_slug):
    categories = Kategoria.objects.filter(id=category_id)
    termekek = Termek.objects.filter(kategoria_id__in=categories.get_descendants(include_self=True))
    products = Termek.objects.filter(kategoria_id=category_id)
    kat = Kategoria.objects.filter(id=category_id).first()
    colors = Color.objects.filter(szin=category_id)

    context = {
        'termekek': termekek,
        'category': kat,
        'categories': categories,
        'colors': colors,
    }

    if products.count() > 1 or kat.get_descendants():
        return render(request, 'main/kategoriak.html', context)
    else:
        product = Termek.objects.filter(kategoria_id=category_id).first()
        context['product'] = product
        return render(request, 'main/oneProduct.html', context)


def oneProduct(request, category_id, category_slug, product_id, product_slug):
    product = Termek.objects.get(id=product_id)
    category = Kategoria.objects.get(id=category_id)


    context = {
        'product': product,
        'category': category,
    }

    return render(request, 'main/oneProduct.html', context)


def viszonteladoknak(request):
    return render(request, 'main/viszonteladoknak.html')


def blog(request):
    return render(request, 'main/blog.html')


def cegeknek(request):
    uzenet = "Cégeknek oldal"
    context = {
        'uzenet': uzenet,
    }
    return render(request, 'main/cegeknek.html', context)

def kereses(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        context = {
            'searched': searched
        }
        return render(request, 'main/kereses.html', context)
    else:
        return render(request, 'main/kereses.html')


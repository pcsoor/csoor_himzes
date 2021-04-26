from .models import Szin, Meret, Termek, Kategoria

def extras(request):
    kategoriak = Kategoria.objects.all()
    context = {
        'kategoriak': kategoriak,
    }
    return context

from django.shortcuts import render
from .models import Torta, Categoria, Testimonio
from correo.forms import ContactoForm 

def index(request):
    tortas = Torta.objects.all()
    categorias = Categoria.objects.all()    
    testimonios = Testimonio.objects.filter(visible=True).order_by('-id')[:6]
    form = ContactoForm()
    
    context = {
        'tortas': tortas,
        'categorias': categorias,
        'testimonios': testimonios,
        'form': form
    }
    return render(request, 'web/index.html', context)
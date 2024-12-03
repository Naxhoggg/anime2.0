from django.shortcuts import render, get_object_or_404
from .models import Galeria, Categoria, Personaje
from django.core.paginator import Paginator

# Create your views here.

def galeria(request):
    # QuerySet básico que obtiene todas las galerías
    galerias = Galeria.objects.all()
    # QuerySet para obtener todas las categorías
    categorias = Categoria.objects.all()
    
    paginator = Paginator(galerias, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'gallery/galeria.html', {
        "page_obj": page_obj,
        "categorias": categorias
    })

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    galerias = Galeria.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    
    paginator = Paginator(galerias, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'gallery/galeria.html', {
        "page_obj": page_obj,
        "categorias": categorias,
        "categoria_actual": categoria
    })
    
def personajes(request, galeria_id):
    galeria = get_object_or_404(Galeria, id=galeria_id)
    personajes = Personaje.objects.filter(galeria=galeria)
    
    return render(request, 'gallery/personajes.html', {
        'galeria': galeria,
        'personajes': personajes
    })
    
    



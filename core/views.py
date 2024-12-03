from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def index(request):
    return render(request,"core/index.html")

def clasicos(request):
    return render(request,"core/clasicos.html")

def actuales(request):
    return render(request,"core/actuales.html")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio o a donde desees
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def energia(request):
    return render(request, 'energia.html')

def educacion(request):
    return render(request, 'educacion.html')

def economia(request):
    return render(request, 'economia.html')

def cambio(request):
    return render(request, 'cambio.html')

def contacto(request):
    return render(request, 'contacto.html')


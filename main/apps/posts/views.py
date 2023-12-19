from django.shortcuts import render

# Create your views here.
def cambio(request):
    return render(request, 'cambio.html')

def mi_vista(request):
    return render(request, 'mi_vista.html')
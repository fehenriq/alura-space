from django.shortcuts import render, get_object_or_404, redirect
from galery.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, "galery/index.html", {"cards": fotografias})


def image(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galery/imagem.html", {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, "galery/buscar.html", {"cards": fotografias})
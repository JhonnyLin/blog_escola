from django.shortcuts import render
# render funciona como um atalho pegando a pagian no templates e passando para HttpResponde
from django.http import HttpResponse

def home(request):
    # os 3 parametros são requisição, pagina e um texto, que no caso é um dicionario
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contato.html')

def videos(request):
    return render(request, 'videos.html')

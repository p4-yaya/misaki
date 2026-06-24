from django.shortcuts import render
from django.http import HttpResponse

def tela1(request):
    return render(request,"misaki/login.html")

def tela2(request):
    return render(request,"misaki/inicial.html")

def tela3(request):
    return render(request,"misaki/produtos.html")

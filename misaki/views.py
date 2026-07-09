from django.shortcuts import render

def login(request):
    return render(request,"misaki/login.html")

def inicial(request):
    return render(request,"misaki/inicial.html")

def produtos(request):
    return render(request,"misaki/produtos.html")

def produtos2(request):
    return render(request,"misaki/produtos2.html")

def contato(request):
    return render(request,"misaki/contato.html")
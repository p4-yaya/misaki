from django.shortcuts import render
from django.http import HttpResponse

def tela1(request):
    return HttpResponse("login")

def tela2(request):
    return HttpResponse("inicial")

def tela3(request):
    return HttpResponse("produtos")
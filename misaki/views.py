from django.shortcuts import render

def login(request):
    return render(request, "misaki/login.html")

def inicial(request):

    produtos = [
        {"titulo": "Nome do Produto", 
         "preco": 10.99,
         "descricao": "Descrição do produto"
         },

        {"titulo": "Produto 2", 
         "preco": 19.99, 
         "descricao": "Descrição do produto 2"
         },
    ]

    context = {
        "produtos": produtos
    }

    return render(request, "misaki/inicial.html")

def sobre(request):
    return render(request, "misaki/sobre.html")

def produtos(request):
    return render(request, "misaki/produtos.html")



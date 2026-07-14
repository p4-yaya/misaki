from django.shortcuts import render

def login(request):
    return render(request, "misaki/login.html")

def inicial(request):
    return render(request, "misaki/inicial.html")

# --- SUA FUNÇÃO PRODUTOS ATUALIZADA ---
def produtos(request):
    # 1. Lista com o caminho das suas 3 imagens dentro de 'static'
    fotos = [
        'misaki/img/produtos/pd1.png',
        'misaki/img/produtos/pd1_1.png',
        'misaki/img/produtos/pd1_2.png',
    ]
    
    # 2. Captura o parâmetro ?foto= da URL. Se não existir, começa na primeira (0)
    foto_id = int(request.GET.get('foto', 0))
    
    # 3. Proteção: garante que o ID não quebre se for menor que 0 ou maior que a lista
    if foto_id >= len(fotos):
        foto_id = 0
    elif foto_id < 0:
        foto_id = len(fotos) - 1

    # 4. Lógica para fazer as setinhas darem a "volta" no carrossel
    proximo_id = foto_id + 1 if foto_id + 1 < len(fotos) else 0
    anterior_id = foto_id - 1 if foto_id - 1 >= 0 else len(fotos) - 1

    # 5. Dicionário com os dados que o seu HTML (produtos.html) vai usar
    contexto = {
        'foto_atual': fotos[foto_id],      # Caminho da imagem que ficará grande
        'foto_id_atual': foto_id,          # ID da foto ativa para acender a bordinha
        'proximo_id': proximo_id,          # ID usado pela seta da direita
        'anterior_id': anterior_id,        # ID usado pela seta da esquerda
    }

    return render(request, "misaki/produtos.html", contexto)


def produtos2(request):
    fotos = [
        'misaki/img/produtos/pd3.png',
        'misaki/img/produtos/pd3_1.png',
        'misaki/img/produtos/pd3_2.png',
    ]
    
    foto_id = int(request.GET.get('foto', 0))
    
    if foto_id >= len(fotos):
        foto_id = 0
    elif foto_id < 0:
        foto_id = len(fotos) - 1

    proximo_id = foto_id + 1 if foto_id + 1 < len(fotos) else 0
    anterior_id = foto_id - 1 if foto_id - 1 >= 0 else len(fotos) - 1

    contexto = {
        'foto_atual': fotos[foto_id],      # Caminho da imagem que ficará grande
        'foto_id_atual': foto_id,          # ID da foto ativa para acender a bordinha
        'proximo_id': proximo_id,          # ID usado pela seta da direita
        'anterior_id': anterior_id,        # ID usado pela seta da esquerda
    }

    return render(request, "misaki/produtos2.html", contexto)

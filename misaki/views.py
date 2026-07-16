from django.shortcuts import render, redirect
from django.http import Http404

#Dicionario de produtos
PRODUTOS_DB = [
    {
        "id": 1,
        "titulo": "Bastidor 16cm - Fairy Tail",
        "preco": "130,00",
        "imagem": "misaki/img/produtos/pd1.png",
        "foto_principal": "misaki/img/produtos/pd1.png",
        "miniaturas": [
            "misaki/img/produtos/pd1.png",
            "misaki/img/produtos/pd1_1.png",
            "misaki/img/produtos/pd1_2.png",
        ],
        "introducao": "✨ O bastidor bordado Fairy Tail é uma peça artesanal feita com carinho para fãs. ✨",
        "tamanho": "16 cm de diâmetro",
        "cuidados": [
            "Evite contato com água e umidade excessiva;",
            "Não utilizar produtos químicos na limpeza."
        ],
        "rodape": "Perfeito para presentear ou decorar seu espaço com a magia de Fairy Tail! 💜"
    },
    {
        "id": 2,
        "titulo": "Bastidor Porta alianças",
        "preco": " 100,00",
        "imagem": "misaki/img/produtos/pd3.png",
        "foto_principal": "misaki/img/produtos/pd3.png",
        "miniaturas": [
            "misaki/img/produtos/pd3.png",
            "misaki/img/produtos/pd3_1.png",
            "misaki/img/produtos/pd3_2.png",
        ],
        "introducao": "✨ O bastidor bordado para portar aliança, uma peça artesanal feita com carinho para eternizar e simbolizar as alianças de noivado ✨",
        "tamanho": "Vários diâmetros (8cm a 30cm)",
        "cuidados": [
            "Evite quedas para não danificar o fecho regulador.",
            "Evite contato com água e umidade excessiva.",
            "Não utilizar produtos químicos ou abrasivos na limpeza."
        ],
        "rodape": "Perfeito para decorar e eternizar seu a magia de seu noivado! 💜"
    },

    {
        "id": 3,
        "titulo": "Chaveiro Bordado de Personagem",
        "preco": "40,00",
        "imagem": "misaki/img/produtos/pd2.png",
        "foto_principal": "misaki/img/produtos/pd2.png", 
        "miniaturas": [
            "misaki/img/produtos/pd2.png",   
            "misaki/img/produtos/pd2_1.png",   
            "misaki/img/produtos/pd2_2.png",       
        ],
        "introducao": "✨ Leve seu personagem favorito sempre com você! Nossos chaveiros são bordados artesanalmente à mão, super detalhados e cheios de personalidade. Ideais para decorar mochilas, chaves ou para presentear quem você ama com uma peça única do universo geek, animes e cultura pop. ✨",
        "tamanho": "Aproximadamente 8cm de altura",
        "cuidados": [
            "Evite molhar ou deixar o chaveiro exposto à umidade excessiva.",
            "Mantenha longe de superfícies que possam puxar ou desfiar os pontos do bordado.",
            "Se necessário, limpe delicadamente com um pano seco ou escovinha de cerdas muito macias."
        ],
        "rodape": "Escolha o seu modelo favorito e carregue essa arte com você! 💜"
    },

    {
        "id": 4,
        "titulo": "Chaveiro Mini Bastidor de Madeira",
        "preco": "15,00",
        "imagem": "misaki/img/produtos/pd4.png",       
        "foto_principal": "misaki/img/produtos/pd4.png",
        "miniaturas": [
            "misaki/img/produtos/pd4.png",             
            "misaki/img/produtos/pd4_1.png",           
        ],
        "introducao": "✨ Adicione um toque minimalista e super afetivo ao seu dia a dia! Nossos mini chaveiros são bordados à mão em tecido e delicadamente emoldurados em bases de madeira. Com ilustrações super fofas que vão de patinhas e gatinhos até referências de Harry Potter, Frida Kahlo e Totoro. ✨",
        "tamanho": "Formatos disponíveis: Quadrado (4cm x 4cm) e Oval (5cm de altura)",
        "cuidados": [
            "Por conter base de madeira (MDF) e tecido, evite qualquer contato com água ou umidade.",
            "Para limpeza de poeira, utilize apenas um pano seco e macio.",
            "Evite quedas ou fortes impactos para preservar a integridade da moldura de madeira."
        ],
        "rodape": "Escolha o formato que mais combina com você e carregue esse amor em forma de bordado! 💜"
    }
]

def login(request):
    return render(request, "misaki/login.html")

def inicial(request):
    # Pega o texto enviado pelo formulário (se não houver nada, retorna vazio)
    termo_busca = request.GET.get('q', '').strip()

    # Começamos com todos os produtos da base
    produtos_filtrados = PRODUTOS_DB

    # Se o usuário digitou alguma coisa, filtramos a lista
    if termo_busca:
        produtos_filtrados = []
        for prod in PRODUTOS_DB:
            # Compara o título do produto com o termo digitado (ambos em letras minúsculas)
            if termo_busca.lower() in prod["titulo"].lower():
                produtos_filtrados.append(prod)

    context = {
        "produtos": produtos_filtrados
    }
    
    return render(request, "misaki/inicial.html", context)

# A função agora recebe o "id" que veio lá do clique do usuário
def produtos(request, id):
    # Procuramos na nossa base o produto que tem o ID igual ao clicado
    produto_selecionado = None
    for prod in PRODUTOS_DB:
        if prod["id"] == id:
            produto_selecionado = prod
            break
            
    # Se o ID não existir (ex: o usuário digitou produtos/999/ direto no navegador)
    if produto_selecionado is None:
        raise Http404("Produto não encontrado")

    # Enviamos apenas o produto encontrado para o template de detalhes
    context = {
        "produto": produto_selecionado
    }
    return render(request, "misaki/produtos.html", context)

def sobre(request):
    return render(request, "misaki/sobre.html")
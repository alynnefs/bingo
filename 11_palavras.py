import os
import random
from PIL import ImageFont, ImageDraw, Image, ImageOps

cor = (108, 49, 14, 255)


def selecionar_numeros():
    lista = ["C. de facas", "C. de sobremesa", "C. de taças", "C. de talheres", "Desc. de panela", "Fôrma de bolo", "Frigideira", "Jarra", "J. de café", "J. de chá", "J. de copos", "J. de jantar", "J. de mesa posta", "J. de panelas", "Lixeira", "Luva térmica", "Panos de prato", "Peneiras", "Porta-guard.", "Potes", "Ralador", "Tábua de cortes", "Tábua de frios", "Tigelas", "Toalha de mesa", "Almofadas", "Travesseiros", "Cobertor", "Jogo de cama", "Lençol", "Tábua de passar", "Ferro de passar", "rede", "toalha", "tapetes", "kit de banheiro", "balde retrátil", "capacho", "vassoura", "pá", "MOP", "Rodo", "Extensão elétrica", "ferramentas", "Pix"]
    tabela = [
        random.sample(range(0, 9), 5),
        random.sample(range(0, 18), 5),
        random.sample(range(18, 27), 4),
        random.sample(range(27, 36), 5),
        random.sample(range(3, 45), 5),
    ]

    for coluna in tabela:
        for linha in coluna:
            coluna[coluna.index(linha)] = lista[linha]

    return tabela


def desenhar_rodape(desenho, pagina=1):
    fonte = ImageFont.truetype("assets/Dunkin.otf", 40)
    xcor = 750
    ycor = 1015

    desenho.text((xcor, ycor), str(pagina), font=fonte, fill=(108, 49, 14, 255))
    return desenho


def desenhar_numeros(cartela, numeros_cartela, pagina=1):
    # o resultado fica [[b], [i], [n], [g], [o]]
    # a 'linha' é relativa à letra, por isso é de cima para baixo
    f = ImageFont.truetype("assets/Dunkin.otf", 17)
    delta = 160
    x = -10
    
    for indice_c, coluna in enumerate(numeros_cartela):
        x += delta
        y = -25
        for indice_l, linha in enumerate(coluna):
            if indice_c == indice_l == 2:
                # também soma aqui por causa do quadrado do meio
                y += delta

            txt=Image.new('L', (500,50))
            d = ImageDraw.Draw(txt)
            d.text( (0, 0), str(linha),  font=f, fill=255)
            w=txt.rotate(45,  expand=1)
            print(x,y, linha)
            cartela.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (x,y),  w)
            #desenho.text((x, y), str(linha), font=fonte, fill=cor)
            y += delta


def gerar_cartelas(quantidade=1, numero_inicial=1):
    for i in range(numero_inicial, quantidade + numero_inicial):
        cartela = Image.open("assets/cartela.png")
        desenho = ImageDraw.Draw(cartela)

        numeros_cartela = selecionar_numeros()
        desenhar_numeros(cartela, numeros_cartela, pagina=i)
        desenhar_rodape(desenho, pagina=i)
        cartela.save(f"assets/cartelas_geradas/cartela_{i}.png")


def juntar_as_cartelas():
    os.chdir("assets/cartelas_geradas/")
    cartelas = os.listdir()

    indice_gitkeep = cartelas.index(".gitkeep")
    cartelas.pop(indice_gitkeep)
    imagens = [Image.open(x) for x in cartelas]

    delta = 240  # tamanho da cartela
    largura = delta
    altura = delta
    x = 0
    y = 0

    # tamanho da folha A4
    nova_imagem = Image.new("RGB", (585, 841), (250, 250, 250))
    indice = 0
    while indice < len(imagens):
        if indice % 6 == 0 and indice != 0:
            # salva o PDF atual, com 6 cartelas
            nova_imagem.save(f"para_pdf_{indice}.jpg", "JPEG")

            # reinicia os valores
            nova_imagem = Image.new("RGB", (585, 841), (250, 250, 250))
            largura = delta
            altura = delta
            x = 0
            y = 0

        elif indice % 2 == 0 and indice != 0:
            # vai para a linha de baixo
            x = 0
            y += delta

        i = imagens[indice].resize((largura, altura))
        nova_imagem.paste(i, (x, y))

        # vai para a coluna da direita
        x += delta
        indice += 1

    # salva a última folha
    nova_imagem.save(f"para_pdf_{indice}.jpg", "JPEG")


gerar_cartelas(quantidade=1, numero_inicial=1)
juntar_as_cartelas()
os.system("convert para_pdf_* imprimir.pdf")

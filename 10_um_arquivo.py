import os
import random
from PIL import ImageFont, ImageDraw, Image

cor = (108, 49, 14, 255)


def selecionar_numeros():
    return [
        random.sample(range(1, 16), 5),
        random.sample(range(16, 31), 5),
        random.sample(range(31, 46), 4),
        random.sample(range(46, 61), 5),
        random.sample(range(61, 76), 5),
    ]


def desenhar_rodape(desenho, pagina=1):
    fonte = ImageFont.truetype("assets/Dunkin.otf", 40)
    xcor = 750
    ycor = 1015

    desenho.text((xcor, ycor), str(pagina), font=fonte, fill=(108, 49, 14, 255))
    return desenho


def desenhar_numeros(desenho, numeros_cartela, pagina=1):
    # o resultado fica [[b], [i], [n], [g], [o]]
    # a 'linha' é relativa à letra, por isso é de cima para baixo
    fonte = ImageFont.truetype("assets/Dunkin.otf", 80)
    delta = 160
    x = 10
    for indice_c, coluna in enumerate(numeros_cartela):
        x += delta
        y = 225
        for indice_l, linha in enumerate(coluna):
            if indice_c == indice_l == 2:
                # também soma aqui por causa do quadrado do meio
                y += delta
            desenho.text((x, y), str(linha), font=fonte, fill=cor)
            y += delta


def gerar_cartelas(quantidade=1, numero_inicial=1):
    for i in range(numero_inicial, quantidade + numero_inicial):
        cartela = Image.open("assets/cartela.png")
        desenho = ImageDraw.Draw(cartela)

        numeros_cartela = selecionar_numeros()
        desenhar_numeros(desenho, numeros_cartela, pagina=i)
        desenhar_rodape(desenho, pagina=i)
        cartela.save(f"assets/cartelas_geradas/cartela_{i}.png")


def juntar_em_pdf():
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


gerar_cartelas(quantidade=7, numero_inicial=3)
juntar_em_pdf()
os.system("convert para_pdf_* imprimir.pdf")

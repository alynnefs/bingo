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


def gerar_cartelas(quantidade=1):
    for i in range(1, quantidade + 1):
        cartela = Image.open("assets/cartela.png")
        desenho = ImageDraw.Draw(cartela)

        numeros_cartela = selecionar_numeros()
        desenhar_numeros(desenho, numeros_cartela, pagina=i)
        desenhar_rodape(desenho, pagina=i)
        cartela.save(f"assets/cartelas_geradas/cartela_{i}.png")


gerar_cartelas(quantidade=3)

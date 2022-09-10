import random
from PIL import ImageFont, ImageDraw, Image


cor = (108, 49, 14, 255)
cartela = Image.open("assets/cartela.png")
desenho = ImageDraw.Draw(cartela)


def selecionar_numeros():
    return [
        random.sample(range(1, 16), 5),
        random.sample(range(16, 31), 5),
        random.sample(range(31, 46), 4),
        random.sample(range(46, 61), 5),
        random.sample(range(61, 76), 5),
    ]


def desenhar_rodape():
    fonte = ImageFont.truetype("assets/Dunkin.otf", 40)
    xcor = 750
    ycor = 1015

    desenho.text((xcor, ycor), str(0), font=fonte, fill=(108, 49, 14, 255))
    return desenho


def desenhar_numeros(numeros_cartela):
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
            desenhar_rodape()  # LINHA ADICIONADA
            desenho.text((x, y), str(linha), font=fonte, fill=cor)
            y += delta

    cartela.save(f"assets/cartelas_geradas/cartela_resultante.png")


numeros_cartela = selecionar_numeros()
desenhar_numeros(numeros_cartela)

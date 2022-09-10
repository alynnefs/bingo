import random
from PIL import ImageFont, ImageDraw, Image


fonte = ImageFont.truetype("assets/Dunkin.otf", 80)


def selecionar_numeros():
    return [
        random.sample(range(1, 16), 5),
        random.sample(range(16, 31), 5),
        random.sample(range(31, 46), 4),
        random.sample(range(46, 61), 5),
        random.sample(range(61, 76), 5),
    ]


def desenhar_numeros(numeros_cartela):
    cartela = Image.open("assets/cartela.png")
    desenho = ImageDraw.Draw(cartela)

    # o resultado fica [[b], [i], [n], [g], [o]]
    # a 'linha' é relativa à letra, por isso é de cima para baixo
    delta = 160
    x = 10

    for indice_c, coluna in enumerate(numeros_cartela):
        x += delta
        y = 225
        for indice_l, linha in enumerate(coluna):
            print(indice_c, indice_l)
            if indice_c == indice_l == 2:
                # também soma aqui por causa do quadrado do meio
                y += delta
            desenho.text((x, y), str(linha), font=fonte, fill=(0, 0, 0, 255))
            y += delta

    cartela.save(f"assets/cartelas_geradas/cartela_resultante.png")


numeros_cartela = selecionar_numeros()
desenhar_numeros(numeros_cartela)

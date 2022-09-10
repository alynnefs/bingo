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

    desenho.text((0, 0), "meu texto", font=fonte, fill=(0, 0, 0, 255))

    cartela.save(f"assets/cartelas_geradas/cartela_resultante.png")


numeros_cartela = selecionar_numeros()
desenhar_numeros(numeros_cartela)

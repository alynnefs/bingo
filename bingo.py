import random
from PIL import ImageFont,ImageDraw,Image


# TODO: refatorar absolutamente tudo
def gerar_cartelas(quantidade_cartelas=1, numero_inicial=1):
    def desenhar_rodape(desenho, numero_inicial):
        xcor = 750
        ycor = 1015
        fonte=ImageFont.truetype("Dunkin.otf",40)
        desenho.text((xcor,ycor),str(numero_inicial),font=fonte,fill=(0,0,0,255))
        return desenho

    def desenhar(valores_bingo, numero_inicial):
        cartela = Image.open("cartela.png")
        desenho = ImageDraw.Draw(cartela)
        fonte=ImageFont.truetype("Dunkin.otf",80)

        # o resultado fica [[b], [i], [n], [g], [o]]
        delta = 160
        x = 10
        y = 25
        # TODO: pegar o índice sem usar range
        for coluna in valores_bingo:
            x += delta
            y = 225
            for linha in coluna:
                # TODO: verificar se é [2,2]. Se sim, soma delta no y
                desenho.text((x,y),str(linha),font=fonte,fill=(0,0,0,255))
                y += delta

        desenhar_rodape(desenho, numero_inicial)
        cartela.save(f"cartelas/{numero_inicial}.png")

    def embaralhar(quantidade_cartelas, numero_inicial):
        while quantidade_cartelas:
            print(numero_inicial)
            valores_bingo = [
                random.sample(range(1, 16), 5),
                random.sample(range(16, 31), 5),
                random.sample(range(31, 46), 4),
                random.sample(range(46, 61), 5),
                random.sample(range(61, 76), 5)
            ]
            quantidade_cartelas -= 1
            desenhar(valores_bingo, numero_inicial)
            numero_inicial += 1 # pode começar com valor diferente de 1
                
    embaralhar(quantidade_cartelas=quantidade_cartelas, numero_inicial=numero_inicial)

gerar_cartelas(3, 4)

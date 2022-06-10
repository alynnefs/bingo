#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
from PIL import ImageFont,ImageDraw,Image


# TODO: refatorar absolutamente tudo
def gerar_cartelas(quantidade_cartelas=1, numero_inicial=1):
    def desenhar_rodape(desenho, numero_inicial):
        xcor = 750
        ycor = 1015
        fonte=ImageFont.truetype("assets/Dunkin.otf",40)
        desenho.text((xcor,ycor), str(numero_inicial), font=fonte,fill=(108,49,14,255))
        return desenho

    def desenhar(valores_bingo, numero_inicial):
        cartela = Image.open("assets/cartela.png")
        desenho = ImageDraw.Draw(cartela)
        fonte=ImageFont.truetype("assets/Dunkin.otf",80)

        # o resultado fica [[b], [i], [n], [g], [o]]
        # a 'linha' é relativa à letra, por isso é de cima para baixo
        delta = 160
        x = 10

        for indice_c, coluna in enumerate(valores_bingo):
            x += delta
            y = 225
            for indice_l, linha in enumerate(coluna):
                if indice_c == indice_l == 2:
                    # também soma aqui por causa do quadrado do meio
                    y += delta 
                desenho.text((x,y),str(linha),font=fonte,fill=(108,49,14,255))
                y += delta

        desenhar_rodape(desenho, numero_inicial)
        cartela.save(f"assets/cartelas_geradas/{numero_inicial}.png")

    def embaralhar(quantidade_cartelas, numero_inicial):
        while quantidade_cartelas:
            #print(numero_inicial)
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


def juntar_em_pdf():
    os.chdir("assets/cartelas_geradas/")
    cartelas = os.listdir()

    indice_gitkeep = cartelas.index(".gitkeep")
    cartelas.pop(indice_gitkeep)
    imagens = [Image.open(x) for x in cartelas]

    delta = 240
    largura = delta
    altura = delta
    x = 0
    y = 0

    # tamanho da folha A4
    new_image = Image.new('RGB',(585, 841), (250,250,250))
    for indice, imagem in enumerate(imagens):
        if indice % 6 == 0 and indice != 0:
            # salva o PDF atual, com 6 cartelas
            new_image.save(f"para_pdf_{indice}.jpg", "JPEG")

            # reinicia os valores
            new_image = Image.new('RGB',(585, 841), (250,250,250))
            largura = delta
            altura = delta
            x = 0
            y = 0

        elif indice % 2 == 0 and indice != 0:
            # vai para a linha de baixo
            x = 0
            y += delta

        i = imagem.resize((largura, altura))
        new_image.paste(i,(x,y))
        # vai para a coluna da direita
        x += delta

    # salva a última folha
    new_image.save(f"para_pdf_{indice}.jpg", "JPEG")
    new_image.show()

    # junta os PDFs
    os.system('convert para_pdf_* imprimir.pdf')


gerar_cartelas(10, 1)
juntar_em_pdf()


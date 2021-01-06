#!/bin/python3

import sys
from PIL import Image, ImageDraw, ImageFont

class Texto:
    def __init__(self, fileFonte, frase, tamanho, color):
        self.sizeW = None
        self.sizeH = None
        self.color = color
        self.frase = frase
        self.tamanho = tamanho
        self.fileFonte = fileFonte
        self.fonte = ImageFont.truetype(self.fileFonte, size = tamanho)


class Picture(object):

    def __init__(self, fonte, file, frase, color):
        # Criando o texto
        self.texto = Texto(fonte, frase, 800, color)

        # Salvando as caminho da imagem
        self.file = file

        # Abrindo e desenhando o canvas
        self.imagem = Image.open(file)
        self.pintura = ImageDraw.Draw(self.imagem)

        # Processando informacoes da imagem
        self.nome = self.file.split('/')[-1]
        self.sizeW, self.sizeH = self.imagem.size


    def drawTextInCanvas(self):
        #Calcula do tamanho do texto na imagem
        self.texto.sizeH, self.texto.sizeW = self.pintura.textsize(self.texto.frase, self.texto.fonte)

        #Calculando o meio da imagem
        middleW = (self.sizeW/2 - self.texto.sizeW/2)
        middleH = (self.sizeH/2 - self.texto.sizeH/2)

        # Pintar o texto no meio da imagem
        self.pintura.text((middleH, middleW), self.texto.frase, fill = self.texto.color, font = self.texto.fonte, align='center')

    def save(self):
        self.imagem.save("New_" + self.nome)

    def show(self):
        self.imagem.show()


def main():
    wall = Picture("data/font/Pirata_One/PirataOne-Regular.ttf", "data/calling-of-saint-matthew.jpeg", "Calling of\nSt. Matthew", 'rgb(255, 255, 255)')
    wall.drawTextInCanvas()
    wall.save()

if __name__ == "__main__":
    main()

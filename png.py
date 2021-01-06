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

    def __init__(self, fonte, file, titulo, autor, color):
        # Criando o texto
        self.title = Texto(fonte, titulo, 800, color)
        self.author = Texto(fonte, autor, 350, color)

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
        self.title.sizeH, self.title.sizeW = self.pintura.textsize(self.title.frase, self.title.fonte)
        self.author.sizeH, self.author.sizeW = self.pintura.textsize(self.author.frase, self.author.fonte)

        #Calculando o meio da imagemv para texto
        middleW = (self.sizeW/2 - (self.title.sizeW + self.author.sizeW)/2)
        middleH = (self.sizeH/2 - self.title.sizeH/2)

        #Calculando o meio da imagemv para author
        middleAuthorH = (self.sizeH/2 - self.author.sizeH/2)
        middleAuthorW = (self.sizeW/2 + self.title.sizeW/2)

        # Pintar o texto no meio da imagem
        self.pintura.text((middleH, middleW), self.title.frase, fill = self.title.color, font = self.title.fonte, align='center')
        self.pintura.text((middleAuthorH, middleAuthorW), self.author.frase, fill = self.author.color, font = self.author.fonte, align='center')

    def save(self):
        self.imagem.save("New_" + self.nome)

    def show(self):
        self.imagem.show()


def main():
    wall = Picture("data/font/Pirata_One/PirataOne-Regular.ttf", "data/calling-of-saint-matthew.jpeg", "Calling of\nSt. Matthew","Danielli dos Reis Costa", 'rgb(255, 255, 255)')
    wall.drawTextInCanvas()
    wall.save()

if __name__ == "__main__":
    main()

#!/bin/python3

import sys
import argparse
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
        # Salvando as caminho da imagem
        self.file = file

        # Abrindo e desenhando o canvas
        self.imagem = Image.open(file)
        self.pintura = ImageDraw.Draw(self.imagem)

        # Processando informacoes da imagem
        self.nome = self.file.split('/')[-1]
        self.sizeW, self.sizeH = self.imagem.size

        # Criando o texto
        self.title = Texto(fonte, titulo, int(self.sizeH/6.5), color)
        self.author = Texto(fonte, autor, int(self.sizeH/14.2), color)


    def drawTextInCanvas(self):
        #Calcula do tamanho do texto na imagem
        self.title.sizeW, self.title.sizeH = self.pintura.textsize(self.title.frase, self.title.fonte)
        self.author.sizeW, self.author.sizeH  = self.pintura.textsize(self.author.frase, self.author.fonte)

        #Calculando o meio da imagem para texto
        middleW = (self.sizeW/2 - (self.title.sizeW)/2)
        middleH = (self.sizeH/2 - (self.title.sizeH + self.author.sizeH)/2)

        #Calculando o meio da imagem para author
        middleAuthorW = (self.sizeW/2 - (self.author.sizeW)/2)
        middleAuthorH = (self.sizeH/2 + (self.title.sizeH)/4 )

        # Pintar o texto no meio da imagem
        self.pintura.text((middleW, middleH, ), self.title.frase, fill = self.title.color, font = self.title.fonte, align='center')
        self.pintura.text((middleAuthorW, middleAuthorH ), self.author.frase, fill = self.author.color, font = self.author.fonte, align='center')

    def save(self):
        self.imagem.save("New_" + self.nome)

    def show(self):
        self.imagem.show()


def main():

    parser = argparse.ArgumentParser(
        description="Welcome to the PNG. An app created inspired after the NerdWriter1 art thumbnails",
        usage="%(prog)s [-p] [-t] [-a] [-c]",
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        metavar="",
        help="The path to the image that will be modified",
    )
    parser.add_argument(
        "-t",
        "--title",
        type=str,
        metavar="",
        help="The main text printed in the image between \" ",
    )
    parser.add_argument(
        "-a",
        "--author",
        type=str,
        metavar="",
        help="The secondary text printed in the image between \" ",
    )
    parser.add_argument(
        "-c",
        "--color",
        type=str,
        metavar="",
        help="The hex of the color used in the text. Default is #FFFFFF (do not need the charactere #)",
    )

    args = parser.parse_args()

    path = ""
    title = ""
    author = ""
    color = "#FFFFFF"

    if not (args.path):
        parser.error("The path to the image need to be passed with --path")
        exit()
    else:
        if args.path:
            path = args.path
        if args.title:
            title = args.title
        if args.author:
            author = args.author
        if args.color:
            color = "#"+args.color

    print(path)
    wall = Picture("data/font/Pirata_One/PirataOne-Regular.ttf", path,  title, author, color)
    # wall = Picture("data/font/Pirata_One/PirataOne-Regular.ttf", "data/calling-of-saint-matthew.jpeg", "Calling of\nSt. Matthew","Danielli dos Reis Costa", 'rgb(255, 255, 255)')
    wall.drawTextInCanvas()
    wall.save()

if __name__ == "__main__":
    main()

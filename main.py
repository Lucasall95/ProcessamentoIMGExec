import numpy as np
import cv2


def showImage(img):
    from matplotlib import pyplot as plt
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def sizeImageByte(img):
    from PIL import Image
    img = Image.open("imgs/Tiringa.jpg")
    print("Tamanho da Imagem em Bytes: ", str(len(img.fp.read())), "bytes")

def getColor(img,y,x):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def setColor(img , y, x, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)
    return img


def main():
    obj_img = cv2.imread("imgs/Tiringa.jpg")
    altura, largura, canais_de_cor = obj_img.shape
    print("Dimensões da Imagem : ", largura, ",", altura)
    print("Canais de Cor: ", canais_de_cor)
    sizeImageByte(obj_img)

    for y in range(0, altura):
        for x in range(0, largura):
         verde, azul, vermelho = getColor(obj_img,y,x)
         #obj_img = setColor(obj_img, y, x, 0, 0,0)
         #eye_img = obj_img[54:54 + 40, 67: 67 + 40]

    #eye_img = obj_img[54:54 + 40, 67: 67 + 40]
    retangulo = cv2.rectangle(obj_img,(107,128),(149,169),0,-1)

    #cv2.imwrite("TiringaModificado.png",obj_img)
    showImage(retangulo)
    #obj_img[128 : 128 + retangulo.shape[0], 107 : 107 + retangulo.shape[1]] = retangulo
    cv2.imwrite("TiringaModificado.png", obj_img)
    #showImage(obj_img)



main()

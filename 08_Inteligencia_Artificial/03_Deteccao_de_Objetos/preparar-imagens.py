import cv2
import os
import numpy as np
from PIL import Image
import pathlib

pasta = 'positivas_manual'
pasta_destino = 'positivas_final'

def salvarImagensTreinamento(pasta_atual, pasta_destino):

    caminhosImagens = [os.path.join(pasta_atual, file) for file in os.listdir(pasta_atual)]
    num_imagem = 1
    for imagem in caminhosImagens:
        nome_imagem = os.path.split(imagem)[1].split("/")[0]
        sem_extensao = os.path.split(nome_imagem)[1].split(".")[0]

        nome_padrao = "caneca" # mudar se for preciso
        nome_salvo = nome_padrao + "_" + str(num_imagem)
        print(nome_imagem)

        try:
            diretorio_salvo = pasta_destino + "/"

            # carrega a imagem e converte para escala de cinza
            img = Image.open(pasta_atual + "/" + nome_imagem).convert('L')
            # converte a imagem (PIL) para numpy array
            imgNp = np.array(img,'uint8')
            # descomentar caso as imagens não estejam do mesmo tamanho
            imgNp = cv2.resize(imgNp, (100, 100))

            # Cria a pasta positivas_final e salva as imagens
            pathlib.Path(diretorio_salvo).mkdir(parents=True, exist_ok=True)
            cv2.imwrite(diretorio_salvo + nome_salvo + ".png", imgNp)

            cv2.imshow('Imagem', imgNp)
            cv2.waitKey(100)
            num_imagem += 1

        except ValueError:
            print('.')


salvarImagensTreinamento(pasta, pasta_destino)
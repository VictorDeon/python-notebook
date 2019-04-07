import os

largura = 50
altura = 50
pasta = 'positivas_final'
arquivo = 'positivas.lst'

for img in os.listdir(pasta):
    # 1 Indica a quantidade de objetos na imagem
    # 0 e 0 indica respectivamente a posição X e Y do objeto na imagem.
    linha = img + ' 1 0 0 ' + str(largura) + ' ' + str(altura) + '\n'

    with open(arquivo, 'a') as file:
        file.write(linha)
        print(linha)

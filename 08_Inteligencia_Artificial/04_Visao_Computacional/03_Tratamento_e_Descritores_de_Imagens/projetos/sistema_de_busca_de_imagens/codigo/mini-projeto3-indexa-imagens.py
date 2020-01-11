# Extrai recursos das imagens e gera índice a ser usado na pesquisa

# python mini-projeto3-indexa-imagens.py --dataset ukbench --index index.csv

# Imports
import cv2
import argparse
# pip install progressbar33
import progressbar
from imutils import paths
from tools.hsvdescriptor import HSVDescriptor

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help = "Caminho para o diretório que contém as imagens a indexar")
ap.add_argument("-i", "--index", required=True, help = "Caminho para onde o índice de características será armazenado")
args = vars(ap.parse_args())

# Inicializa o descritor de cores e abre o arquivo de índice de saída para escrita
desc = HSVDescriptor((4, 6, 3))
output = open(args["index"], "w")

# Obtém a lista de caminhos de imagem e inicializa a barra de progresso
imagePaths = list(paths.list_images(args["dataset"]))
widgets = ["Indexando: ", progressbar.Percentage(), " ", progressbar.Bar(), " ", progressbar.ETA()]
pbar = progressbar.ProgressBar(maxval=len(imagePaths), widgets=widgets)
pbar.start()

# Loop sobre os caminhos das imagem no diretório do conjunto de dados
for (i, imagePath) in enumerate(imagePaths):
	# Extrai o nome da imagem (ou seja, a ID da imagem única) do caminho da imagem e carrega a própria imagem
	filename = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	# Descreve a imagem
	features = desc.describe(image)

	# Grava os recursos no nosso arquivo de índice
	features = [str(x) for x in features]
	output.write("{},{}\n".format(filename, ",".join(features)))
	pbar.update(i)

# Fecha o arquivo de índice de saída
pbar.finish()
print("Total de {} imagens indexadas".format(len(imagePaths)))
output.close()
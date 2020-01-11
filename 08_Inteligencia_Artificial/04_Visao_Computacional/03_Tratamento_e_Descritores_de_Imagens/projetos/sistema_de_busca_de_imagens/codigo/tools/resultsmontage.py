# Apresenta o resultado em formato de montagem das imagens mais significativas

# Imports
import cv2
import numpy as np

class ResultsMontage:
	def __init__(self, imageSize, imagesPerRow, numResults):
		# Armazena o tamanho da imagem alvo e o número de imagens por linha
		self.imageW = imageSize[0]
		self.imageH = imageSize[1]
		self.imagesPerRow = imagesPerRow

		# Alocar memória para a imagem de saída
		numCols = numResults // imagesPerRow
		self.montage = np.zeros((numCols * self.imageW, imagesPerRow * self.imageH, 3), dtype="uint8")

		# Inicializa o contador para a imagem atual juntamente com o número da linha e da coluna
		self.counter = 0
		self.row = 0
		self.col = 0

	def addResult(self, image, text=None, highlight=False):
		# Verifica se o número de imagens por linha foi cumprido e, em caso afirmativo, redefine o contador de colunas e incremente a linha
		if self.counter != 0 and self.counter % self.imagesPerRow == 0:
			self.col = 0
			self.row += 1

		# Redimensiona a imagem para a largura e a altura fixas e configure-a na montagem
		image = cv2.resize(image, (self.imageH, self.imageW))
		(startY, endY) = (self.row * self.imageW, (self.row + 1) * self.imageW)
		(startX, endX) = (self.col * self.imageH, (self.col + 1) * self.imageH)
		self.montage[startY:endY, startX:endX] = image

		# Se o texto não for Nenhum, desenhe
		if text is not None:
			cv2.putText(self.montage, text, (startX + 10, startY + 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 3)

		# Verifique se o resultado deve ser destacado
		if highlight:
			cv2.rectangle(self.montage, (startX + 3, startY + 3), (endX - 3, endY - 3), (0, 255, 0), 4)

		# Incrementa o contador de colunas e o contador de imagens
		self.col += 1
		self.counter += 1
# Passo 1 - Definindo o Descritor de Imagem

# Imports
import cv2
import numpy as np

class HSVDescriptor:
	def __init__(self, bins):
		# Armazena o número de caixas para o histograma
		self.bins = bins

	def describe(self, image):
		# Converte a imagem para o espaço de cores HSV e inicializa os recursos usados para quantificar a imagem
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		# Obtém as dimensões e calcula o centro da imagem
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))

		# Divide a imagem em quatro retângulos / segmentos (superior esquerda, superior direita, inferior direita, inferior esquerda)
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h), (0, cX, cY, h)]

		# Constrói uma máscara elíptica que representa o centro da imagem
		(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
		ellipMask = np.zeros(image.shape[:2], dtype="uint8")
		cv2.ellipse(ellipMask, (int(cX), int(cY)), (int(axesX), int(axesY)), 0, 0, 360, 255, -1)

		# Loop sobre todos os segmentos
		for (startX, endX, startY, endY) in segments:
			# Constrói uma máscara para cada canto da imagem, subtraindo o centro elíptico dele
			cornerMask = np.zeros(image.shape[:2], dtype="uint8")
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
			cornerMask = cv2.subtract(cornerMask, ellipMask)

			# Extrai um histograma de cores da imagem, depois atualiza o vetor de características
			hist = self.histogram(image, cornerMask)
			features.extend(hist)

		# Extrai um histograma de cores da região elíptica e atualiza o vetor de características
		hist = self.histogram(image, ellipMask)
		features.extend(hist)

		# Retorna o vetor de características
		return np.array(features)

	def histogram(self, image, mask=None):
		# Extrai um histograma de cores 3D da região mascarada da imagem, usando o número fornecido de caixas por canal; então normaliza o histograma
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])
		hist = cv2.normalize(hist, hist).flatten()

		# Retorna o histograma
		return hist
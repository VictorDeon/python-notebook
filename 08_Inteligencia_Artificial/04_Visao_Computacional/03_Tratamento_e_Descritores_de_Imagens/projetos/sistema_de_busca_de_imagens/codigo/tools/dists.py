# Função auxiliar para calcular a distância qui-quadrado

# Imports
import numpy as np

def chi2_distance(histA, histB, eps=1e-10):
	# Calcula a distância qui-quadrado
	d = 0.5 * np.sum(((histA - histB) ** 2) / (histA + histB + eps))

	# Retorna o valor calculado
	return d
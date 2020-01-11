# Buscador

# Imports
import csv
from . import dists

class Searcher:
	def __init__(self, dbPath):
		# Armazena o caminho para o banco de dados
		self.dbPath = dbPath

	def search(self, queryFeatures, numResults=10):
		# Inicializa o dicionário de resultados
		results = {}

		# Abre o banco de dados para leitura
		with open(self.dbPath) as f:
			# Inicializa o CSV reader
			reader = csv.reader(f)

			# Loop por todas as linhas do índice
			for row in reader:
				# Analisa a identificação da imagem e os recursos, depois calcula a distância do qui-quadrado entre os recursos 
				# em nosso banco de dados e os recursos de consulta
				features = [float(x) for x in row[1:]]
				d = dists.chi2_distance(features, queryFeatures)

				# Agora que temos a distância entre os dois vetores de recursos, podemos atualizar o dicionário de resultados: 
				# A chave é o ID de imagem atual no banco de dados e o valor é a distância que acabamos de calcular, 
				# representando como "similar" a imagem no banco de dados e a nossa consulta
				results[row[0]] = d

			# Fecha o reader
			f.close()

		# Classifica nossos resultados, de modo que as distâncias menores (ou seja, as imagens mais relevantes) estejam na frente da lista)
		results = sorted([(v, k) for (k, v) in results.items()])

		# Retorna os resultados
		return results[:numResults]
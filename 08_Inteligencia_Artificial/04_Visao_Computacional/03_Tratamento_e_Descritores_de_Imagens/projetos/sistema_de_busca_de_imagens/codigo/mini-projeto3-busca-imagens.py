# Busca de Imagens

# python mini-projeto3-busca-imagens.py --index index.csv --dataset ukbench --relevant relevant.json --query ukbench/ukbench00980.jpg

# Imports
import cv2
import json
import imutils
import argparse
from tools.resultsmontage import ResultsMontage
from tools.hsvdescriptor import HSVDescriptor
from tools.searcher import Searcher

# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True, help="Caminho para onde o índice de características está armazenado")
ap.add_argument("-q", "--query", required=True, help="Caminho para a imagem da consulta")
ap.add_argument("-d", "--dataset", required=True, help="Caminho para o diretório de conjunto de dados original")
ap.add_argument("-r", "--relevant", required=True, help = "Caminho para o dicionário relevante")
args = vars(ap.parse_args())

# Inicializa o descritor de imagem e a montagem de resultados
desc = HSVDescriptor((4, 6, 3))
montage = ResultsMontage((240, 320), 5, 20)
relevant = json.loads(open(args["relevant"]).read())

# Carrega o dicionário de consultas relevantes e procura os resultados relevantes para a imagem da consulta
queryFilename = args["query"][args["query"].rfind("/") + 1:]
queryRelevant = relevant[queryFilename]

# Carrega a imagem da consulta, exibe, descreve
print("Descrevendo imagem de consulta...")
query = cv2.imread(args["query"])
cv2.imshow("Query", imutils.resize(query, width=320))
features = desc.describe(query)

# Realiza a busca
print("Pesquisa em andamento...")
searcher = Searcher(args["index"])
results = searcher.search(features, numResults=20)

# Loop pelos resultados
for (i, (score, resultID)) in enumerate(results):
	# Carrega a imagem do resultado e exibe
	print("[Imagem similar encontrada no banco de imagens] {result_num}. {result} - {score:.2f}".format(result_num=i + 1, result=resultID, score=score))
	result = cv2.imread("{}/{}".format(args["dataset"], resultID))
	montage.addResult(result, text="#{}".format(i + 1), highlight=resultID in queryRelevant)

# Mostra a imagem de saída dos resultados
cv2.imshow("Resultados", imutils.resize(montage.montage, height=700))
cv2.waitKey(0)


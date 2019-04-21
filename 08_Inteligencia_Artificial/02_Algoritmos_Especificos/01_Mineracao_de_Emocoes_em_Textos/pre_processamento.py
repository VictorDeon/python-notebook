from base import base, stopwords
from base_completa import base_treinamento, base_teste
import nltk


def extrair_radicais(frase):
    """
    Extrair os radicais de uma frase.
    """
    
    # Pega os stopwords
    stopwords = nltk.corpus.stopwords.words("portuguese")
    
    # Pegar o stemmer especifico para a lingua portuguesa
    stemmer = nltk.stem.RSLPStemmer()
    
    stemming = [str(stemmer.stem(palavra)) for palavra in frase.split() if palavra not in stopwords]
        
    return stemming


def aplicar_stemming(texto):
    """
    Pega os radicais do texto base
    """
    
    stopwords = nltk.corpus.stopwords.words("portuguese")
    
    # Pegar o stemmer especifico para a lingua portuguesa
    stemmer = nltk.stem.RSLPStemmer()
    frases = []
    
    for (palavras, emocao) in texto:
        # stem() retira o radical da palavra
        stemming = [str(stemmer.stem(palavra)) for palavra in palavras.split() if palavra not in stopwords]
        frases.append((stemming, emocao))
        
    return frases


stemming_treinamento = aplicar_stemming(base_treinamento)
stemming_teste = aplicar_stemming(base_teste)


def busca_palavras():
    """
    Pega a stemming e retira as emoções, pegando só as palavras.
    """
    
    so_palavras = []
    
    for (palavras, emocao) in stemming_treinamento:
        # extend: Pega os elementos da lista e joga 1 por 1 dentro da outra lista
        so_palavras.extend(palavras)
        
    # pega a frequencia de vezes que uma palavra aparece.
    qtd_palavras = nltk.FreqDist(so_palavras)
    
    # Retira as palavras repetidas
    sem_repeticao = qtd_palavras.keys()
    
    return list(sem_repeticao), qtd_palavras.most_common()


def inseri_tabela(novas_palavras):
    """
    Recebe uma nova frase (lista de radicais) e verifica quais palavras tem
    e quais não tem de acordo com a tabela de palavras unicas (radicais).
    Monta uma linha da tabela.
    """
    
    frase = set(novas_palavras)
    
    linha_tabela = {}
    
    palavras_unicas, qtd_palavras = busca_palavras()
    
    for palavra in palavras_unicas:
        linha_tabela["%s" % palavra] = (palavra in frase)
        
    return linha_tabela
        
    
base_completa_treinamento = nltk.classify.apply_features(inseri_tabela, stemming_treinamento)
base_completa_teste = nltk.classify.apply_features(inseri_tabela, stemming_teste)
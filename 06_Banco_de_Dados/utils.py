import random
import rstr
import datetime


def gerar_idade():
    """
    Pega uma idade entre 15 e 99.
    """
    
    return random.randint(15, 99)


def gerar_cpf():
    """
    Pega uma string com 11 caracteres númericos para
    representar o CPF de forma aleatória.
    """
    
    return rstr.rstr('1234567890', 11)


def gerar_telefone():
    """
    Pega um telefone aleatório no formato (xx) xxxxx-xxxx
    """
    
    return '({0} {1}-{2})'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 5),
        rstr.rstr('1234567890', 4)
    )


def gerar_data():
    """
    Pega uma data e hora aleatório no formato
    yyyy-mm-dd hh:mm:ss
    """
    
    ano = random.randint(1980, 2018)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)
    hora = random.randint(1, 23)
    minuto = random.randint(1, 59)
    segundo = random.randint(1, 59)
    microsegundos = random.randint(1, 999999)
    data = datetime.datetime(
        ano, mes, dia, hora, minuto, segundo, microsegundo
    ).isoformat(" ")
    
    return data


def gerar_cidade():
    """
    Pega uma cidade aleatório da lista criada.
    """
    
    cidades = [
        [u'São Paulo', 'SP'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return random.choice(cidades)
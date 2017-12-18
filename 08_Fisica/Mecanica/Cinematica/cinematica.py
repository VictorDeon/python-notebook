from math import (fabs)


class Cinematica(object):
    """
    Métodos para resolução de tópicos de física: Cinemática
    Obs: Utilize parâmetros nomeados
    """

    DESLOCAMENTO_ESCALAR = 1
    DISTANCIA_PERCORRIDA = 2
    INTERVALO_DE_TEMPO = 3
    VELOCIDADE_MEDIA = 4

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    def calcular(self, operacao, **kwargs):
        """
        Calcular operações.
        """

        resultado = None

        if operacao == 1:
            resultado = self.deslocamento_escalar(kwargs)
        elif operacao == 2:
            resultado = self.distancia_percorrida(kwargs)
        elif operacao == 3:
            resultado = self.intervalo_de_tempo(kwargs)
        elif operacao == 4:
            resultado = self.velocidade_media(kwargs)
        else:
            print("Operação invalida!")

        return resultado

    def deslocamento_escalar(self, kwargs):
        """
        Deslocamento escalar (DS) é o deslocamento entre o destino (S)
        e o ponto de partida (So) ou é a velocidade média (Vm) vezes
        o intervalo de tempo (DT) + tempo de parada (TP) caso tiver

        Possiveis parâmetros:

            S = Destino
            So = Ponto de partida

        OU

            Vm = Velocidade média
            DT = Intervalo de tempo
            TP = Tempo de parada

        Retorno

            DS = Deslocamento escalar
        """

        S = kwargs.get('S', None)
        So = kwargs.get('So', None)
        Vm = kwargs.get('Vm', None)
        DT = kwargs.get('DT', None)
        TP = kwargs.get('TP', 0)

        if S and So:
            DS = S - So
        elif Vm and DT:
            DS = Vm * (DT + TP)
        else:
            return self.ERROR

        return DS

    def distancia_percorrida(self, kwargs):
        """
        Distância percorrida (D)

        Parâmetros:

            S = Destino
            So = Ponto de partida

        Retorno

            D = Distância percorrida
        """

        S = kwargs.get('S', None)
        So = kwargs.get('So', None)

        if S is None or So is None:
            return self.ERROR

        if fabs(S) > fabs(So):
            D = fabs(S) - fabs(So)
        else:
            D = fabs(So) - fabs(S)

        return D

    def intervalo_de_tempo(self, kwargs):
        """
        Intervalo de tempo (DT)

        Parâmetros:

            T = Tempo final
            To = Tempo inicial

        OU

            DS = Deslocamento escalar
            Vm = Velocidade média
            TP = Tempo de parada


        Retorno

            DT = Intervalo de tempo
        """

        T = kwargs.get('T', None)
        To = kwargs.get('To', None)
        Vm = kwargs.get('Vm', None)
        DS = kwargs.get('DS', None)
        TP = kwargs.get('TP', 0)

        if T and To:
            DT = T - To
        elif Vm and DS:
            DT = DS/Vm
        else:
            return self.ERROR

        return DT + TP

    def velocidade_media(self, kwargs):
        """
        Velocidade escalar média (Vm)

        Parâmetros:

            V = Velocidade final
            Vo = Velocidade inicial

        OU

            DT = Intervalo de tempo
            DS = Deslocamento escalar
            TP = Tempo de parada

        Retorno

            V = Velocidade
        """

        V = kwargs.get('V', None)
        Vo = kwargs.get('Vo', None)
        DS = kwargs.get('DS', None)
        DT = kwargs.get('DT', None)
        TP = kwargs.get('TP', 0)

        if V or Vo:
            Vm = V - Vo
        elif DS and DT:
            Vm = DS/(DT + TP)
        else:
            return self.ERROR

        return Vm


class Ultrapassagem(object):
    """
    Classe de métodos responsavel por ultrapassagens de corpos.
    """

    def velocidade_relativa(self, V1, V2, sentidos_opostos=False):
        """
        Velocidade de ultrapassagem relativa depende do sentido de
        ultrapassagem, se o tiver o mesmo sentido que no caso é o padrão,
        (sentido_contrario=False) vai subtrair as velocidade, caso contrario
        irá somar.

        Parâmetros:

            - V1 = Velocidade do objeto ultrapassando
            - V2 = Velocidade do objeto ultrapassado
            - sentidos_opostos = Sentido da ultrapassagem, False se for no
            mesmo sentido (padrão) e True em sentidos contrarios

        Retorno

            - Vr = Velocidade relativa
        """

        if sentidos_opostos:
            Vr = V1 + V2
        else:
            Vr = V1 - V2

        return Vr

    def calcular(self, Vu=None, DS=None, DT=None):
        """
        Velocidade de ultrapassagem (Vu) entre dois corpos extensos passando o
        comprimento dos corpos (DS) e o intervalo de tempo de duração da
        ultrapassagem.

        Parâmetros:

            - Vu = Velocidade de ultrapassagem,
            - DS = Comprimento dos corpos,
            - DT = Intervalo de duração da ultrapassagem

        Retorno:

            - Vu = Velocidade de ultrapassagem, caso passe o DS e o DT
            - DS = Comprimento dos corpos, caso passe a Vu e o DT
            - DT = Intervalo de duração da ultrapassagem, caso passe o Vu e DS
        """

        if DS is None:
            DS = Vu * DT
            return DS

        if DT is None:
            DT = DS/Vu
            return DT

        Vu = DS/DT
        return Vu


class MU(object):
    """
    Classe de métodos para movimentos uniformes (MU)
    """

    def calcular(self, S=None, So=None, V=None, T=None):
        """
        Calcular a função horária do movimento uniforme MU.

        Parâmetros:

            - S = Posição final
            - So = Posição inicial
            - V = Velocidade
            - T = Tempo

        Retorno

            - S = Caso tenha passado So, V e T
            - So = Caso tenha passado S, V e T
            - V = Caso tenha passado S, So, T
            - T = Caso tenha passado S, So, V
        """

        if So is None:
            So = S - V*T
            return So

        if V is None:
            V = (S - So)/T
            return V

        if T is None:
            T = (S - So)/V
            return T

        S = So + V*T
        return fabs(S)

    def tempo_de_encontro(self, So1, V1, So2, V2):
        """
        Tempo de encontre entre dois objetos.

        Parâmetros:

            - So1 = Posição inicial do primeiro objeto.
            - V1 = Velocidade do primeiro objeto
            - So2 = Posição inicial do segundo objeto
            - V2 = Velocidade do segundo objeto

        Retorno:

            - T = Momento do encontro entre o objeto 1 e o objeto 2
        """

        T = (So2 - So1)/(V1 - V2)

        return fabs(T)

    def instante_de_encontro(self, So1, V1, So2, V2):
        """
        Instante do encontro.

        Parâmetros:

            - So1 = Posição inicial do primeiro objeto.
            - V1 = Velocidade do primeiro objeto
            - So2 = Posição inicial do segundo objeto
            - V2 = Velocidade do segundo objeto

        Retorno:

            - Instante de encontro de S1 e S2, chamado de S
        """

        T = self.tempo_de_encontro(So1, V1, So2, V2)

        # Para calcular o instante de encontro só usar o tempo
        # em qualquer uma das equações, no caso foi de S1
        S = self.calcular(
            So=So1,
            V=V1,
            T=T
        )

        return S

from math import fabs


class Basico(object):
    """
    Métodos básicos para resolução de tópicos de cinemática como
    deslocamento escalar, distância percorrida, intervalo de tempo e
    velocidade média.

    Obs: Utilize parâmetros nomeados
    """

    DESLOCAMENTO_ESCALAR = 1
    DISTANCIA_PERCORRIDA = 2
    INTERVALO_DE_TEMPO = 3
    VELOCIDADE_MEDIA = 4

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    def calcular(self, operacao, kwargs):
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

        if (S is not None and
            So is not None):

            DS = S - So

        elif (Vm is not None and
              DT is not None):

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

        if (T is not None and
            To is not None):

            DT = T - To

        elif (Vm is not None and
              DS is not None):

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

        if (V is not None or
            Vo is not None):

            Vm = V - Vo

        elif (DS is not None and
              DT is not None):

            Vm = DS/(DT + TP)

        else:
            return self.ERROR

        return Vm

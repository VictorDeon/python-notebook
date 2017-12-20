from math import fabs


class MU(object):
    """
    Métodos para resolução de tópicos de física: MU
    Obs: Utilize parâmetros nomeados
    """

    POSICAO = 1
    POSICAO_DE_ENCONTRO = 2
    TEMPO_DE_ENCONTRO = 3

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    def calcular(self, operacao, kwargs):
        """
        Calcular operações.
        """

        resultado = None

        if operacao == 1:
            resultado = self.posicao(kwargs)
        elif operacao == 2:
            resultado = self.instante_de_encontro(kwargs)
        elif operacao == 3:
            resultado = self.tempo_de_encontro(kwargs)
        else:
            print("Operação invalida!")

        return resultado

    def posicao(self, kwargs):
        """
        Calcular a função horária do movimento uniforme MU.

        Parâmetros:

            S = Posição final
            So = Posição inicial
            V = Velocidade
            T = Tempo

        Retorno = {
            'S': Posição final,
            'So': Posição inicial,
            'V': Velocidade,
            'T': Tempo
        }

        """

        S = kwargs.get('S', None)
        So = kwargs.get('So', None)
        V = kwargs.get('V', None)
        T = kwargs.get('T', None)

        if (S is None and
            So is not None and
            V is not None and
            T is not None):

            S = So + V*T

        elif (So is None and
              S is not None and
              V is not None and
              T is not None):

            So = S - V*T

        elif (V is None and
              S is not None and
              So is not None and
              T is not None):

            V = (S - So)/T

        elif (V is None and
              S is not None and
              So is not None and
              T is not None):

            T = (S - So)/V

        else:
            return self.ERROR

        resultado = {
            'S': S,
            'So': So,
            'V': V,
            'T': T
        }

        return resultado

    def tempo_de_encontro(self, kwargs):
        """
        Tempo de encontre entre dois objetos.

        Parâmetros:

            So1 = Posição inicial do primeiro objeto.
            V1 = Velocidade do primeiro objeto
            So2 = Posição inicial do segundo objeto
            V2 = Velocidade do segundo objeto

        Retorno:

            T = Momento do encontro entre o objeto 1 e o objeto 2
        """

        So1 = kwargs.get('So1', None)
        V1 = kwargs.get('V1', None)
        So2 = kwargs.get('So2', None)
        V2 = kwargs.get('V2', None)

        if (So1 is None or
            V1 is None or
            So2 is None or
            V2 is None):
            return self.ERROR

        T = (So2 - So1)/(V1 - V2)

        return fabs(T)

    def instante_de_encontro(self, kwargs):
        """
        Instante ou posição do encontro.

        Parâmetros:

            So1 = Posição inicial do primeiro objeto.
            V1 = Velocidade do primeiro objeto
            So2 = Posição inicial do segundo objeto
            V2 = Velocidade do segundo objeto

        Retorno:

            S = Posição de encontro de S1 e S2
        """

        T = self.tempo_de_encontro(kwargs)


        So1 = kwargs.get('So1', None)
        V1 = kwargs.get('V1', None)

        kwargs = {
            'So': So1,
            'V': V1,
            'T': T
        }

        # Para calcular o instante de encontro só usar o tempo
        # em qualquer uma das equações, no caso foi do objeto 01
        resultado = self.calcular(self.POSICAO, kwargs)

        return resultado['S']

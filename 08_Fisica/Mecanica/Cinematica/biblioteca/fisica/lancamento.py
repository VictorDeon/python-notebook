from math import pow, sqrt


class LancamentoVertical(object):
    """
    Lançamento vertical para cima.
    """

    TEMPO_DE_SUBIDA = 1
    ALTURA_MAXIMA = 2

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    def calcular(self, operacao, kwargs):
        """
        Calcular operações.
        """

        if operacao == 1:
            resultado = self.tempo_de_subida(kwargs)
        elif operacao == 2:
            resultado = self.altura_maxima(kwargs)
        else:
            raise NameError(self.ERROR)

        return resultado

    def tempo_de_subida(self, kwargs):
        """
        Tempo de subida.
        """

        Ts = kwargs.get("Ts")
        Vo = kwargs.get("Vo")
        g = kwargs.get("g")

        if (Ts is None and
            Vo is not None and
            g is not None):

            Ts = Vo/g

        elif (Vo is None and
              Ts is not None and
              g is not None):

            Vo = Ts * g

        elif (g is None and
              Vo is not None and
              Ts is not None):

            g = Vo/Ts

        else:

            return self.Error

        resultado = {
            'Ts': Ts,
            'Vo': Vo,
            'g': g
        }

        return resultado

    def altura_maxima(self, kwargs):
        """
        Altura máxima.
        """

        Hm = kwargs.get("Hm")
        Vo = kwargs.get("Vo")
        g = kwargs.get("g")

        if (Hm is None and
            Vo is not None and
            g is not None):

            Hm = pow(Vo, 2)/(2*g)

        elif (Vo is None and
              Hm is not None and
              g is not None):

            Vo = sqrt(2*g*Hm)

        elif (g is None and
              Vo is not None and
              Hm is not None):

            g = pow(Vo, 2)/(2*Hm)

        else:

            return self.Error

        resultado = {
            'Hm': Hm,
            'Vo': Vo,
            'g': g
        }

        return resultado

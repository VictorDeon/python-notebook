from math import pow, sqrt


class MUV(object):
    """
    Métodos para resolução de tópicos de física: MUV
    Obs: Utilize parâmetros nomeados
    """

    VELOCIDADE = 1
    ACELERACAO = 2
    VELOCIDADE_MEDIA = 3
    POSICAO = 4
    TORRICELLI = 5

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    def calcular(self, operacao, kwargs):
        """
        Calcular operações.
        """

        resultado = None

        if operacao == 1:
            resultado = self.velocidade(kwargs)
        elif operacao == 2:
            resultado = self.aceleracao(kwargs)
        elif operacao == 3:
            resultado = self.velocidade_media(kwargs)
        elif operacao == 4:
            resultado = self.posicao(kwargs)
        elif operacao == 5:
            resultado = self.torricelli(kwargs)
        else:
            raise NameError(self.ERROR)

        return resultado

    def velocidade(self, kwargs):
        """
        Equação horaria da velocidade do MUV.
        """

        V = kwargs.get('V', None)
        Vo = kwargs.get('Vo', None)
        a = kwargs.get('a', None)
        t = kwargs.get('t', None)

        if (V is None and
            a is not None and
            t is not None and
            Vo is not None):

            V = Vo + a*t

        elif (Vo is None and
              V is not None and
              a is not None and
              t is not None):

            Vo = V - a*t

        elif (a is None and
              V is not None and
              Vo is not None and
              t is not None):

            a = (V - Vo)/t

        elif (t is None and
              V is not None and
              Vo is not None and
              a is not None):

            t = (V - Vo)/a

        else:
            return self.ERROR

        resultado = {
            'V': V,
            'Vo': Vo,
            'a': a,
            't': t
        }

        if a > 0:
            if V > 0:
                resultado['movimento'] = "Acelerado e Progressivo"
            else:
                resultado['movimento'] = "Retardado e Retrógrado"
        elif a < 0:
            if V > 0:
                resultado['movimento'] = "Retardado e Progressivo"
            else:
                resultado['movimento'] = "Acelerado e Retrógrado"

        return resultado

    def aceleracao(self, kwargs):
        """
        Aceleração ou coeficiente angular da reta ou declividade da reta (a)
        o quanto sua velocidade varia na unidade de tempo.
        """

        a = kwargs.get('a', None)
        DV = kwargs.get('DV', None)
        DT = kwargs.get('DT', None)

        if (a is None and
            DV is not None and
            DT is not None):

            a = DV/DT

        elif (DV is None and
              a is not None and
              DT is not None):

            DV = a * DT

        elif (DT is None and
              DV is not None and
              a is not None):

            DT = DV/a

        else:
            return self.ERROR

        resultado = {
            'a': a,
            'DV': DV,
            'DT': DT
        }

        if a > 0:
            resultado['angulo'] = "Agudo"
        elif a < 0:
            resultado['angulo'] = "Obtuso"

        return resultado

    def velocidade_media(self, kwargs):
        """
        A velocidade média do MUV é a média aritmetica das velocidades nos
        instantes extremos de dois intervalos de tempo quaisquer.
        """

        V = kwargs.get('V', None)
        Vo = kwargs.get('Vo', None)
        Vm = kwargs.get('Vm', None)

        if (V is None and
            Vo is not None and
            Vm is not None):

            V = 2*Vm - Vo

        elif (Vo is None and
              V is not None and
              Vm is not None):

            Vo = 2*Vm - V

        elif (Vm is None and
              V is not None and
              Vo is not None):

            Vm = (V + Vo)/2

        else:
            return self.ERROR

        resultado = {
            'Vm': Vm,
            'V': V,
            'Vo': Vo
        }

        return resultado

    def posicao(self, kwargs):
        """
        Função horária do espaço (posição) de um móvel em MUV e Torricelli.
        """

        S = kwargs.get('S', None)
        So = kwargs.get('So', None)
        Vo = kwargs.get('Vo', None)
        t = kwargs.get('t', None)
        a = kwargs.get('a', None)

        if (S is None and
            So is not None and
            Vo is not None and
            t is not None and
            a is not None):

            S = So + Vo*t + (a*pow(t, 2))/2

        elif (So is None and
              S is not None and
              Vo is not None and
              t is not None and
              a is not None):

            So = S - Vo*t - (a*pow(t, 2))/2

        elif (Vo is None and
              S is not None and
              So is not None and
              t is not None and
              a is not None):

            Vo = (2*S - 2*So - a*pow(t, 2))/(2*t)

        elif (t is None and
              S is not None and
              So is not None and
              Vo is not None and
              a is not None):

            resultado = self.torricelli(kwargs)
            V = resultado['V']
            t = (2*(S - So))/(Vo + V)

        elif (a is None and
              S is not None and
              So is not None and
              Vo is not None and
              t is not None):

            a = (2*(S - So - Vo*t))/(pow(t, 2))

        else:
            return self.ERROR

        resultado = {
            'S': S,
            'So': So,
            'Vo': Vo,
            't': t,
            'a': a
        }

        return resultado

    def torricelli(self, kwargs):
        """
        Esquação de Torricelli, utilizada quando não aparece a variável tempo.
        """

        V = kwargs.get('V', None)
        S = kwargs.get('S', None)
        So = kwargs.get('So', None)
        DS = kwargs.get('DS', None)
        Vo = kwargs.get('Vo', None)
        a = kwargs.get('a', None)

        if (S is not None and
            So is not None and
            DS is None):

            DS = S - So

        if (V is None and
            DS is not None and
            Vo is not None and
            a is not None):

            V = sqrt(pow(Vo, 2) + 2*a*(DS))

        elif (DS is None and
              V is not None and
              Vo is not None and
              a is not None):

            DS = (pow(V, 2) - pow(Vo, 2))/(2*a)

        elif (Vo is None and
              V is not None and
              DS is not None and
              a is not None):

            Vo = sqrt(pow(V, 2) - 2*a*DS)

        elif (a is None and
              V is not None and
              DS is not None and
              Vo is not None):

            a = (pow(V, 2) - pow(Vo, 2))/(2*DS)

        else:
            return self.ERROR

        resultado = {
            'V': V,
            'S': S,
            'So': So,
            'DS': DS,
            'Vo': Vo,
            'a': a
        }

        return resultado

class Ultrapassagem(object):
    """
    Métodos para resolução de tópicos de física: Ultrapassagem

    Obs: Utilize parâmetros nomeados
    """

    VELOCIDADE_RELATIVA = 1
    VELOCIDADE_DE_ULTRAPASSAGEM = 2
    COMPRIMENTO_DOS_CORPOS = 3
    DURACAO_DA_ULTRAPASSAGEM = 4

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    def calcular(self, operacao, kwargs):
        """
        Calcular operações.
        """

        resultado = None

        if operacao == 1:
            resultado = self.velocidade_relativa(kwargs)
        elif operacao == 2:
            resultado = self.velocidade_de_ultrapassagem(kwargs)
        elif operacao == 3:
            resultado = self.comprimento_dos_corpos(kwargs)
        elif operacao == 4:
            resultado = self.tempo_de_ultrapassagem(kwargs)
        else:
            print("Operação invalida!")

        return resultado

    def velocidade_relativa(self, kwargs):
        """
        Velocidade de ultrapassagem relativa depende do sentido de
        ultrapassagem, se o tiver o mesmo sentido que no caso é o padrão,
        (sentido_contrario=False) vai subtrair as velocidade, caso contrario
        irá somar.

        Parâmetros:

            V1 = Velocidade do objeto ultrapassando
            V2 = Velocidade do objeto ultrapassado
            sentidos_opostos = Sentido da ultrapassagem, False se for no
                               mesmo sentido (padrão) e True em sentidos
                               contrarios

        Retorno

            Vr = Velocidade relativa
        """

        V1 = kwargs.get('V1', None)
        V2 = kwargs.get('V2', None)
        sentidos_opostos = kwargs.get('sentidos_opostos', False)

        if V1 is None or V2 is None:
            return self.ERROR

        if sentidos_opostos:
            Vr = V1 + V2
        else:
            Vr = V1 - V2

        return Vr

    def velocidade_de_ultrapassagem(self, kwargs):
        """
        Velocidade de ultrapassagem (Vu)

        Parâmetros:

            DS = Comprimento dos corpos,
            DT = Intervalo de duração da ultrapassagem

        Retorno:

            Vu = Velocidade de ultrapassagem, caso passe o DS e o DT
        """

        DS = kwargs.get('DS', None)
        DT = kwargs.get('DT', None)

        if DS is None or DT is None:
            return self.ERROR

        Vu = DS/DT

        return Vu

    def comprimento_dos_corpos(self, kwargs):
        """
        Comprimento do corpo (DS) ultrapassado

        Parâmetros:

            Vu = Velocidade de ultrapassagem,
            DT = Intervalo de duração da ultrapassagem

        Retorno:

            DS = Comprimento do corpo ultrapassado
        """

        Vu = kwargs.get('Vu', None)
        DT = kwargs.get('DT', None)

        if Vu is None or DT is None:
            return self.ERROR

        DS = Vu * DT

        return DS

    def tempo_de_ultrapassagem(self, kwargs):
        """
        Intervalo de duração da ultrapassagem (DT)

        Parâmetros:

            DS = Comprimento dos corpos,
            Vu = Velocidade de ultrapassagem

        Retorno:

            DT = Intervalo de duração da ultrapassagem
        """

        DS = kwargs.get('DS', None)
        Vu = kwargs.get('Vu', None)

        if DS is None or Vu is None:
            return self.ERROR

        DT = DS/Vu

        return DT

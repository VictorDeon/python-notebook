from http import HTTPStatus


class CustomException(Exception):
    """
    Quando são passado parâmetros invalidos no corpo da requisição.
    """

    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None, payload=None):
        """
        Construtor
        """

        Exception.__init__(self)
        self.message = message

        if status_code is not None:
            self.status_code = status_code

        self.payload = payload

    def to_dict(self):
        """
        Retorna a resposta como dicionário.
        """

        response = dict(self.payload or ())
        response['message'] = self.message
        response['status_code'] = self.status_code
        return response
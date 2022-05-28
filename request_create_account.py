from flask import Request


class RequestCreateAccount:

    def __init__(self, request: Request):
        input_json = request.get_json()
        
        self.login = input_json['login']
        self.password = input_json['password']
        self.cpf = input_json['cpf']
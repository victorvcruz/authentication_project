import uuid
import cryptocode
import jwt
from validate_docbr import CPF


class Account:

    def __init__(self, login, password, cpf):
        self.id = uuid.uuid4()
        self.login = login
        self.password = cryptocode.encrypt(password, "secret")

        cpf = str(cpf)
        if self.cpf_is_valid(cpf):
            self.cpf = self.format_cpf(cpf)
        else:
            raise ValueError("invalid cpf")

    def __eq__(self, other, true=None, false=None):
        return self.login == other.login and self.password == other.password


    def cpf_is_valid(self, cpf):
        if len(cpf) == 11:
            validate = CPF()
            return validate.validate(cpf)

    def json(self):
        return {
            'id': self.id,
            'login': self.login,
            'password': self.password,
            'cpf': str(jwt.encode({"jwt": "{}".format(self.cpf)}, "secret",
                                  algorithm="HS256")).replace("b'", "").replace("'", '')
        }

    def format_cpf(self, cpf):
        one = cpf[:3]
        two = cpf[3:6]
        three = cpf[6:9]
        four = cpf[9:]
        return (
            "{}.{}.{}-{}".format(
                one,
                two,
                three,
                four
            )
        )
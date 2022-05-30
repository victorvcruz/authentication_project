from flask import Flask, request, jsonify

from account import Account
from database import insertAccount, findAccountByLogin, authenticateAccount
from request_create_account import RequestCreateAccount

from request_get_cpf import RequestGetCpfAccount

key = "secret"

app = Flask(__name__)


@app.route('/accounts', methods=["POST"])
def createAccount():
    request_account = RequestCreateAccount(request)

    try:
        account = insertAccount(Account(request_account.login, request_account.password, request_account.cpf))

        return jsonify(account.json())

    except NameError:
        return jsonify({'message': "login already exists"}), 409

    except ValueError:
        return jsonify({'message': "invalid cpf"}), 400


@app.route('/accounts', methods=["GET"])
def findCpfByAccount():
    request_get_account = RequestGetCpfAccount(request)

    try:
        account = findAccountByLogin(request_get_account.login)

        if authenticateAccount(account, request_get_account.password):
            return jsonify(account.json())
    except Exception:
        return jsonify({'message': "Not Found"}), 404

    return jsonify({'message': "password incorrect"}), 401

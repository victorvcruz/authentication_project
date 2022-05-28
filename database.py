import cryptocode

list_of_account = []


def findAccountByLogin(login):
    for account in list_of_account:
        if account.login == login:
            return account

    raise Exception("not found")


def authenticateAccount(account, password):
    if cryptocode.decrypt(account.password, "secret") == password:
        return True

    return False


def insertAccount(account):
    try:
        findAccountByLogin(account.login)
        raise NameError("already exists")

    except NameError:
        raise NameError("already exists")
    except Exception:
        list_of_account.append(account)
        return account

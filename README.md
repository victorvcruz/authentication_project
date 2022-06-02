# How to run project
1. run pip install -r requirements.txt in root directory
2. in http://localhost:5000/accounts insert your request

### Application of the requisition
it's just of json parameter

* POST
```
{
 "login": (your login),
 "password": (your password),
 "cpf": (your cpf)
}
```
* GET
```
{
 "login": (your login),
 "password": (your password)
}
```

at the end, you will have the return of the account

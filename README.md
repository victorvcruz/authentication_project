# How to run project
1. install missing dependencies of python
2. install package of Pypi [validate-docbr](https://pypi.org/project/validate-docbr/)
3. in http://localhost:5000/accounts insert your request

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

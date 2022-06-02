# How to run project
1. run `pip install -r requirements.txt` in root directory
2. run main.py
3. in http://localhost:5000/accounts insert your request

### Application of the requisition
it's just of json parameter

* POST
```
{
 "login": "luisa234",
 "password": "23451",
 "cpf": "90325508020"
}
```
* GET
```
{
 "login": (luisa234),
 "password": (23451)
}
```

at the end, you will have the return of the account

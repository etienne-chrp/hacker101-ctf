# Micro CMS v2

## Login

In login username field you can inject SQL code

python
```
if cur.execute('SELECT password FROM admins WHERE username=\'%s\'' % request.form['username'].replace('%', '%%')) == 0:
```

## FLAGS

### Flag0

In username field you can inject a password via `' UNION SELECT 'test' -- `. Then you can use the injectetd password in the password field. Onec logged in you can access the page number 3 wich contains the flag.

### Flag1

When not authenticated you can send a POST request to `/page/edit/$PAGE_ID` which resulst in a HTTP 200 and conatins a FLAG.

```bash
curl -X POST --data "title=toto&body=toto" http://35.227.24.107/34da1c76ad/page/edit/1
```

### Flag2

#### Detection mechnism

When you inject in the login username field the following `' or 1=1 -- `, the error message changes from `Unknown user` to `Invalid password`.

#### Fields length

With the following we can find the length of the field `' OR LENGTH(password)=8;`

#### Fields content

Via Frontend testing framework (Selenium) we can use the following SQL syntax to guess the username and password `' OR password LIKE BINARY '________'`. By knowing the length and using the MySQL wildcard character `_` we can make a dictionarry attack character per character.

#### Flag

Once you have both login and password you can fill up the fields and you will receive the flag.

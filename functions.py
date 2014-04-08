# -*- Coding: utf-8 -*-

# rank in the alphabet for encoding
def char_to_int(c) :
    return ord(c)-97

# inverse operation of char_to_int but in upper case
def int_to_char(nb) :
    return chr(nb + 65)

# convert the message into a good form (erase spaces)
def mes_to_gf(message) :
    plaintext = ""
    for i in range(len(message)) :
        if message[i] != ' ' and message[i]!= '\n':
            plaintext += message[i]
    return plaintext
        
# Hill Cipher Function
def Hill(plaintext, mat):
    for i in range(len(mat)) :
            ciphertext += char_to_int(plaintext[i]) * char_to_int(mat[i]) % 26     

# Matrix file reader
def reader(mat_file):
    mat = file(mat_file, 'U').read().replace('\n', ';')
    if mat[-1] == ';' :
        mat = mat[:-1]
    return mat 

# Matrix to ciphertext
def mat_to_ctxt(mat):
    mat = str(mat).strip('[]')
    if mat[-1] != ' ' :
        mat += ' '
    ciphertext = ''
    number = ''
    for i in range(len(mat)) :
        if mat[i] != ' ' :
            number += mat[i]
        if mat[i] == ' ' :
            number = int(number)
            ciphertext += int_to_char(number)
            number = ''
    return ciphertext


# -*- coding: utf-8 -*-
#################
# Cipher        #
#               #
# Antoine CHAUX #
# 08/04/2014    #
#################

print("\nThis software accept only english characters without numbers and specials symbols: be careful when you type your messages !\n")

import classes as c
from functions import *
#from numpy import *
from random import *

crypto = 0
right_key = False
right_file = False
ciphertext = ""
a = 0
opt_mes = 0
opt_key = 0
size = 0
 
# Cryptosystems Menu
c.input.choice = 0
while c.input.choice <= 0 or c.input.choice > 4 :
    if c.input.choice == 5 :
        print("\nThe Hill Cipher is not finished yet")
    print("\nChoose what cryptosystem you want to use:\n1 - The Shift Cipher\n2 - The Substitution Cipher\n3 - The Affine Cipher\n4 - The Vigenère Cipher\n5 - The Hill Cipher")
    c.input.choice = eval(input())

    
# Message Input
print("Choose your option :\n1 - Enter the message you want to encode in lower case\n2 - Read a file")
opt = eval(input())
if opt == 1 :
    print("Enter your message :")
    c.input.message = input()
    c.input.plaintext = mes_to_gf(c.input.message)
    len_ptxt = len(c.input.plaintext)
else :
    print("Enter your file's name")
    c.input.file = open(input(),'r')
    while right_file == False :
        try :
            c.input.plaintext = mes_to_gf(c.input.file.read())
            right_file = True
            len_ptxt = len(c.input.plaintext)
        except IOError :
            print("Enter a valid file's name")

             
# Shift Cipher Encoding (shift letter's index number of the key)
if c.input.choice == 1 :
    while right_key == False :
        try :
            print("\nEnter your key")
            c.input.key = eval(input())
            right_key = True
        except NameError :
            print("Your key must be a number")
        except SyntaxError :
            print("Your key must be a number")
                        
    for i in range(len_ptxt) :
        ciphertext += int_to_char((char_to_int(c.input.plaintext[i]) +c.input.key)%26)
                    
    print("\nThe ciphertext is :",ciphertext,"\n")

    
# Substitution Cipher Encoding (substitute a letter with another)
if c.input.choice == 2 :
    print("You want to :\n1 - Enter a key\n2 - Use a key from a text file")
    opt_key = eval(input())
    
    if opt_key == 1 :
        print("Enter your substitution, ie : bdefrg... means that a->b, b->d, c->e,etc...")
        c.input.key = input()
        
    if opt_key == 2 :
        print("Enter your file's name (written such as with bdefrg... means that a->b, b->d, c->e,etc...)")
        c.input.key_file = open(input(),'r')
        c.input.key = mes_to_gf(c.input.key_file.read()).upper()
        
    for i in range(len_ptxt) :
        ciphertext += c.input.key[char_to_int(c.input.plaintext[i])]
        
    print("\nThe ciphertext is :",ciphertext,"\n")

# Affine Cipher Encoding (use a affine expression to cipher the letters)
if c.input.choice == 3 :
    while a%26 == 0 or 26%a == 0 :
        print("Enter your key (a,b), with gcd(a,26) = 1")
        c.input.key = eval(input())
        a =c.input.key[0]%26
        b =c.input.key[1]%26
    
    # cipher_letter = a*original_letter + b for each letter 
    for i in range(len_ptxt) :
        ciphertext += int_to_char((a*char_to_int(c.input.plaintext[i]) + b)%26)

    print("\nThe ciphertext is :",ciphertext,"\n")

    
# Vigenere Cipher Encoding
if c.input.choice == 4 :
    print("You want to :\n1 - Enter a key\n2 - Use a key from a text file")
    opt_key = eval(input())
    
    if opt_key == 1 :
        print("Enter your key")
        c.input.key = mes_to_gf(input())
        
    else :
        print("Enter the name of the file")
        c.input.key_file = open(input(),'r')
        c.input.key = mes_to_gf(c.input.key_file.read())
        
    for i in range(len_ptxt) :
        ciphertext += int_to_char((char_to_int(c.input.plaintext[i]) + char_to_int(c.input.key[i%len(c.input.key)]))%26)

    print("\n The ciphertext is :",ciphertext,"\n")

    
# Hill Cipher Encoding
"""if c.input.choice == 5 :
    print("Enter a mxm invertible matrix a key (where m is the length of your message) :\n1 - Directly\n2 - Using a text file")
    opt_key = eval(input())
    
    if opt_key == 1 :
        print("Enter your matrix by row (using space between two number and ; to separate two row)")
        mat = matrix(input())
        # not finished
        
    if opt_key == 2 :
        print("Enter your matrix file")
        mat_file = input()
        mat = matrix(reader(mat_file))
        print(mat)
        
    num_c.input.plaintext = ''
    for i in range(len_ptxt%len(mat)) :
        c.input.plaintext += chr(97 + randint(0,25))
        
    for k in range(len_ptxt//len(mat) + 1) :
        for i in range(len(mat)) :
            num_c.input.plaintext += str(char_to_int(c.input.plaintext[i])) + ' '
        num_c.input.plaintext = matrix(num_c.input.plaintext)
        print(num_c.input.plaintext)
        
        num_ciphertext = num_c.input.plaintext * mat
        ciphertext = mat_to_ctxt(num_ciphertext)
        
    print("\n The ciphertext is :",ciphertext,"\n")"""

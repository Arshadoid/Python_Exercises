# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:45:47 2022

@author: Arshad Mehtiyev
"""

def encoder(text,key):
    encodedText=''
    for char in text:
        encodedText=encodedText+chr(ord(char)+key)
    return encodedText

def decoder(text,key):
    decodedText=''
    for char in text:
        decodedText=decodedText+chr(ord(char)-key)
    return decodedText


def main():
    print("Type below the text to be ciphered:")
    orgText=str(input())
    key=int(input("What is the key value? "))
    print(" ")
    print("Encoded text is: ")
    print(encoder(orgText,key),end='\n')
    print(" ")
    print("To decode the text type the text below:")
    encodedText=str(input())
    key=int(input("Type the key to decode: "))
    print(" ")
    print("Decoded text is:") 
    print(decoder(encodedText,key)) 

main()    
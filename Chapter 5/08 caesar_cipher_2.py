# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:23:44 2022

@author: Arshad Mehtiyev
"""

alphabet = 'abcdefghijklmnopqrstyvwxyz'

def encoder(text,key):
    wordList=text.split()  #make a list out of text words
    newWordList=[]         #new list for encoded words
    
    for word in wordList:  #iterating over each word
        newWord=""
        for char in word:  #iterating over each character of the word
            index=alphabet.find(char)  
            newIndex=index+key
            newWord=newWord+alphabet[newIndex%26]
        newWordList.append(newWord) 
        
    encodedText = ' '.join(newWordList)
    return encodedText  
    

def decoder(text,key):

    wordList=text.split()  #make a list out of text words
    newWordList=[]         #new list for decoded words
    
    for word in wordList:  #iterating over each word
        newWord=""
        for char in word:  #iterating over each character of the word
            
            index=alphabet.find(char)  
            newIndex=index-key
            
            newWord=newWord+alphabet[newIndex%26]
        newWordList.append(newWord) 
        
    encodedText=' '.join(newWordList)
    return encodedText  
    

def main():
    print("Type below the text to be ciphered:")
    orgText=str(input()).lower()
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
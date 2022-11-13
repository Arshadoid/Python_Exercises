# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:09:35 2022

@author: Arshad Mehtiyev
"""
from random import randint, choice

class Card:
    def __init__(self, rank, suit):
        self.rank=int(rank)
        self.suit=str(suit)
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def value(self):
        if self.rank in [11,12,13]:
            return 10
        else:
            return self.rank
    
    def __str__(self):
        rankList = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                    'Eight', 'Nine', 'Ten','Jack', 'Queen', 'King']
        suitDict={'d':'Diamond','c':'Club', 'h':'Hearts', 's':'Spades'}
        
        cardName=rankList[self.rank-1]+' of '+ suitDict[self.suit]
        
        return cardName
    
def main():
    n = int(input('How many cards to generate? '))
    
    suits=['d','c','h','s']
    for i in range(n):
        rank=randint(1, 13)
        suit=choice(suits)
        card=Card(rank, suit)
        print('{0}, Blackjack valuse is {1}'.format(card,card.value()))
        

if __name__ == '__main__':
    main()


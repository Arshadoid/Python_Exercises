# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:09:35 2022

@author: Arshad Mehtiyev
"""
from random import randint, choice
from graphics import *

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
    
    def draw(self, win, center):
        fileName=str(self.rank)+self.suit.upper()+'.ppm'
        cardImage=Image(center, 'cardimages/'+fileName)
        cardImage.draw(win)
        
    
    
    
def main():
    
    win=GraphWin('Random Cards',750,300)
       
    cards=[]
    suits=['d','c','h','s']
    for i in range(5):
        rank=randint(1, 13)
        suit=choice(suits)
        card=Card(rank, suit)
        print('{0}, Blackjack valuse is {1}'.format(card,card.value()))
        cards.append(card)
    
    
    centerX=90
    for c in cards:
        
        c.draw(win, Point(centerX,100))
        cardName=Text(Point(centerX,200), c.__str__())
        cardName.draw(win)
        centerX+=130
                
    win.getMouse()
    win.close()
    

if __name__ == '__main__':
    main()


# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:37:18 2022

@author: Arshad Mehtiyev
"""
#  event_loop2.py  ---  color-changing  window
from  graphics  import  *

def  handleKey(k,  win):
    if  k==    "r":
        win.setBackground("pink")
    elif  k==    "w":
        win.setBackground("white")
    elif  k==    "g":
        win.setBackground("lightgray")
    elif  k==    "b":
        win.setBackground("lightblue")
def  handleClick(pt,  win):
    # create an ENtry for user to type in
    entry=Entry(pt,10)
    entry.draw(win)
    key=''
    # Go modal: loop until user types <Enter> key
    while  key != "Escape" :
        key = win.getKey()
        if key == "Return":
            # undraw the entry and create and draw TExt()
            entry.undraw()
            typed = entry.getText()
            Text(pt, typed).draw(win)            
            break
        
    entry.undraw() 
    # clear(ignore) any mouse click that occured during text entry
    win.checkMouse()
    
def  main():
    win=    GraphWin("Click  and  Type",   500,   500)
    #  Event  Loop:   handle  key  presses  and  mouse  clicks  until  the  user
    #       presses  the  "q"   key.
    
        
    while  True:
        key = win.checkKey()
        if  key== "q":         #  loop  exit break
            break
        if  key:
            handleKey(key,  win)
        pt = win.checkMouse()
        if  pt:
            handleClick(pt,  win)
    win.close()
main()


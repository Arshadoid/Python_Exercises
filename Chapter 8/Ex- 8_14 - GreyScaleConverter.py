# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:27:06 2022

@author: Arshad Mehtiyev
"""
#importing tkinter askopenfilename dialog window
from tkinter.filedialog import askopenfilename, asksaveasfilename
#this part hides the Tkinter rood window
from tkinter import Tk
from graphics import *



# function to open the file
def processFileName(win,mode):
    root = Tk()
    root.withdraw()
    
    types=[('PPM images(*.ppm)','*.ppm'),
           ('GIF images(*.gif)','*.gif')]
    
    if mode=='open':
        fileName = askopenfilename(title='Select the image',
                               filetypes=types)
    elif mode=='save':
        fileName = asksaveasfilename(title='Save the image',
                               filetypes=types)
    
    return fileName
    
    
# function to display the image
def displayImage(clickPoint,fileName,win):
    
    image=Image(clickPoint,fileName)
    image.draw(win)
    return image
    


# function to convert the image to grayscale
def convertImage(image, win):
    imageW=image.getWidth()
    imageH=image.getHeight()
    cntr=0
    for y in range(imageH):
        cntr+=1
        if cntr/imageH>=0.2:
            image.undraw()
            image.draw(win)
            cntr=0
        for x in range(imageW):
            R, G, B = image.getPixel(x,y)
            brightness=int(round(0.299*R+0.587*G + 0.114*B))
            image.setPixel(x,y,color_rgb(brightness,brightness,brightness))
    return image 
   
def saveImage(image,fileName):
    image.save(fileName)             
            
# main function

def main():
    
    win= GraphWin("Image to GrayScale Converter", 400,500)
    clickPoint = win.getMouse()
    fileName= processFileName(win,'open')
    
    image=displayImage(clickPoint,fileName,win)
    
    win.getMouse()
    updatedImage=convertImage(image, win)
    
    win.getMouse()
    fileName= processFileName(win,'save')
    saveImage(updatedImage,fileName)
    
    win.close()
    
if __name__ == '__main__':
    main()
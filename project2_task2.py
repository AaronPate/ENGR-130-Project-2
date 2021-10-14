# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:28:41 2021

@author: TheOn
"""
from matplotlib import pyplot as mat
import math as m

def main():
    
    image = input("Enter the name of a color image file: ")
    img = mat.imread(image)
    mat.imshow(img)
    pixel = []
    print(f"{len(img[0])} x {len(img)}")
    for i in range(0, len(img)):
        temp = []
        for j in range(0, len(img[0])):
            pr = int(img[i,j,0] * 255)
            pg = int(img[i,j,1] * 255)
            pb = int(img[i,j,2] * 255)
            temp.append([pr,pg,pb])
        pixel.append(temp)
    #print(pixel)
    rows = len(img[0])
    col = len(img)
    decryptedImg = task2Helper(rows,col,pixel)
    mat.imshow(decryptedImg)
    return

def task2Helper(rows,cols,img):
    keyString = input("Enter the initial key string: ")
    keyLength = len(keyString)
    keyArray = KeyGen(rows,cols,keyLength)
    print(keyArray)
    decryptedImg = XorCypher(rows,cols,img,keyArray)
    return decryptedImg
    
    
def KeyGen(rows,cols,keyLength):
    key = []
    for i in range(0,rows):
        temp = []
        for j in range(0,cols):
            a = (i * j) % keyLength
            temp.append(m.pow(a,m.pow(2,8) // keyLength))
        key.append(temp)
    return key

def XorCypher(rows,col,img,key):
    decrypted = []
    for i in range(0,rows):
        temp = []
        for j in range(0,col):
            dr = int(img[i][j][0]) ^ int(key[i][j])
            dg = int(img[i][j][1]) ^ int(key[i][j])
            db = int(img[i][j][2]) ^ int(key[i][j])
            temp.append([dr,dg,db])
        decrypted.append(temp)
    return decrypted
    
if __name__ == '__main__':
    main()
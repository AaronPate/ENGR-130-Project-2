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
    pixel = []
    print(f"{len(img[0])} x {len(img)}")
    for i in range(0, len(img)):
        temp = []
        for j in range(0, len(img[0])):
            pr = int(img[j,i,0] * 255)
            pg = int(img[j,i,1] * 255)
            pb = int(img[j,i,2] * 255)
            temp.append([pr,pg,pb])
        pixel.append(temp)
    print(pixel)
    rows = len(img[0])
    col = len(img)
    decryptedImg = task2Helper(rows,col,img)
    
def task2Helper(rows,cols,img):
    keyString = input("Enter the initial key string: ")
    keyLength = len(keyString)
    keyArray = KeyGen(rows,cols,keyLength)
    print(keyArray)
    decryptedImg = XorCypher(rows,cols,img,keyArray)
    return decryptedImg
    
    
def KeyGen(rows,cols,keyLength):
    key = [rows][cols]
    for i in len(0,rows):
        for j in len(0,cols):
            a = (i * j) % keyLength
            key[i][j] = m.pow(a,m.pow(2,8) / keyLength)
    return key

def XorCypher(rows,col,img,key):
    decrypted = [rows][col][2]
    for i in len(0,rows):
        for j in len(0,col):
            decrypted[i][j][0] = img[i][j][0] ^ key[i][j]
            decrypted[i][j][1] = img[i][j][1] ^ key[i][j]
            decrypted[i][j][2] = img[i][j][2] ^ key[i][j]
    return decrypted
    
if __name__ == '__main__':
    main()
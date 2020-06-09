import cv2 as cv
import os
import numpy as np
   

path='where you save the png file which download by scrape.py '
allfi=os.listdir(path)
os.chdir('where you want to save step1 file')
for one in allfi:
    if one=='.DS_Store': continue
    thisfi=path+'/'+one
    src = cv.imread(thisfi) 
    
    img1 = np.zeros((80,215,1), np.uint8) 
    img = np.zeros((80,215,1), np.uint8) 
    gray1 = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    img=gray

    for t in range(3):
        for x in range(80):
            for y in range(215): 
                if x>=6 and x<=74 and y<= 213: 
                    if img[x][y]==112:
                        if  (img[x+1][y]==140 and img[x+2][y]==140 ) or (img[x-1][y]==140 and img[x-2][y]==140) and img[x+1][y]!=255 and img[x-1][y]!=255 and img[x+4][y]!=255:
                            img[x][y]=(140)
    for t in range(5):
        for x in range(80):
            for y in range(215): 
                if x<=76 and y>=3 and y<=200: 
                    if img[x][y]==112:
                        if  (img[x][y-1]==140 and (img[x][y-2]==140 or img[x][y+5]==140 ) and img[x-1][y]!=255 and img[x-1][y]!=112 and img[x +3][y]!=255):
                            img[x][y]=(140)                        
    ##for t in range(8):
    for x in range(80):
        for y in range(215):
            img1[x][y]=(img[x][y])
            if x>=3 and x<=75 and y>=2 and y<=212:
                if img[x][y]==112 or img[x][y]==117:
                    countt=0
                    if img[x+1][y]==140:
                        countt+=1
                    if img[x-1][y]==140:
                        countt+=1
                    if img[x][y+1]==140:
                        countt+=1
                    if img[x][y-1]==140:
                        countt+=1
                    if img[x+1][y+1]==140:
                        countt+=1
                    if img[x-1][y-1]==140:
                        countt+=1
                    if img[x+1][y-1]==140:
                        countt+=1
                    if img[x-1][y+1]==140:
                        countt+=1
                    if countt>=5:
                        img1[x][y]=(140)
    
    a=np.array(140)
    
    mask=cv.inRange(img1,a,a)
    cv.bitwise_not(mask, mask)

    
    ret, binary = cv.threshold(mask, 0, 255, cv.THRESH_BINARY_INV or cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
    binl = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    
    
    
    cv.bitwise_not(binl, binl)

    ##切
    xrec=0
    yrec=0
    for x in range(80):
        county = 0 
        for y in range(215):
            if binl[x][y]==0:
                county+=1
        if county>=20:
            yrec=x
            break

    for y in range(215):
        countx=0
        for x in range(80): 
            if binl[x][y]==0:
                countx+=1
        if countx>=8:
            xrec=y
            break
    

    binl = binl[yrec-5:yrec+32, xrec-4:xrec+96] 
    for t in range(2):
        for x in range(35):
            for y in range(92):
                if x>=1 and x<=32:
                    if binl[x][y]==255:
                        if (binl[x+1][y]==0 or binl[x+2][y]==0) and binl[x-1][y]==0:
                            binl[x][y]=(0)
    for x in range(35):
        for y in range(92):
            if y>=1 and y<=94:
                if binl[x][y]==0:
                    if (binl[x][y+1]==255 and binl[x][y-1]==255):
                        binl[x][y]=(255)
        
    ##寫
    cv.imwrite(one, binl)
    '''
    cv.imshow("as",img1)
    cv.waitKey(0)
    '''
   
    

   
    
    
    
    

    

    
    
    
    

import numpy as np
from PIL import Image
import cv2 as cv
import tensorflow as tf

def split_digits_in_img(img_array):
    x_list = list()
    img1 = np.zeros((80,215,1), np.uint8) 
    img = np.zeros((80,215,1), np.uint8) 
    gray1 = img_array
    gray2 = img_array
    img=gray2
    for t in range(2):
        for x in range(80):
            for y in range(215): 
                if x>=6 and x<=74 and y<= 213: 
                    if img[x][y]==112:
                        if  (img[x+1][y]==140 and img[x+2][y]==140 ) or (img[x-1][y]==140 and img[x-2][y]==140) and img[x+1][y]!=255 and img[x-1][y]!=255 and img[x+4][y]!=255:
                            img[x][y]=(140)
    for t in range(2):
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
    ##for t in range(2):
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
    gray=binl
    li=[]
    j=5
    while j<97 :
        count=0
        countleft=0
        countright=0
        countright1=0
        count1=0
        countup=0
        countmid=0
        countlow=0
        for i in range(36):
            if gray[i][j]==255:
                count+=1
            if gray[i][j+1]==255:
                countright+=1
            if gray[i][j+3]==255:
                countright1+=1
            if i>=0 and i<=12:
                if gray[i][j]==255:
                    countup+=1
            if i>12 and i<=24:
                if gray[i][j]==0:
                    countmid+=1
            if i>24 and i<=37:
                if gray[i][j]==255:
                    countlow+=1
        if count>=35 and countright1>35:
            li.append(j+2)
            j+=18
            count1+=1
        elif count>25 and countright>35 and countup>8 and countlow<3:
            li.append(j+1)
            j+=18
            count1+=1
        elif countup>8 and countmid>6 and countlow>8 and count1>0:
            li.append(j+1)
            j+=18
            count1+=1
        elif count>=33:
            li.append(j+1)
            j+=18
            count1+=1
        elif count==36:
            li.append(j+2)
            j+=18
            count1+=1
        else:
            j+=1
        if count1==2:
            break
    tmp=0
    ttmp=li[0]
    cc=0
    ccc=0
    for w in range(4):
        a=gray[0:36,tmp:ttmp+1]
        if len(a[0])>=38:
            mid=int(len(a[0])/2)
            a1=a[0:36,0:mid]
            a2=a[0:36,mid:(mid*2)-1]
            size=a1.shape
            wet=size[1]
            wet1=int(int(40-wet)/2)
            wett=wet1
            if wet+wet1*2<40:
                wett=wett+1
            img_patch = cv.copyMakeBorder(a1, 0, 0, wet1, wett, cv.BORDER_CONSTANT, value=255)
            
            x_list.append(tf.expand_dims(img_patch/255.0,2))
            if(w>=3): break
            size1=a2.shape
            wet2=size1[1]
            wet3=int(int(40-wet2)/2)
            wettt=wet3
            if wet2+wet3*2<40:
                wettt=wettt+1
            img_patch2 = cv.copyMakeBorder(a2, 0, 0, wet3, wettt, cv.BORDER_CONSTANT, value=255)
            x_list.append(tf.expand_dims(img_patch2/255.0,2))
            if(cc>=2):break 
            tmp=li[cc]
            if(cc<2):
                ttmp=li[cc+1]-2
            else:
                ttmp=94
            cc+=1
        else: 
            size=a.shape
            wet0=size[1]
            wet11=int(int(40-wet0)/2)
            wett1=wet11
            if wet0+wet11*2<40:
                wett1=wett1+1
            img_patch3 = cv.copyMakeBorder(a, 0, 0, wet11, wett1, cv.BORDER_CONSTANT, value=255)
            x_list.append(tf.expand_dims(img_patch3/255.0,2))
            if(cc>2):break 
            tmp=li[cc]
            if(cc<2):
                ttmp=li[cc+1]-2
            else:
                ttmp=95
            cc+=1 
    return x_list
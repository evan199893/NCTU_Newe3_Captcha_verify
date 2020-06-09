import cv2 as cv
import os
import numpy as np

path='where you save step2 png file'
allfile=os.listdir(path)
os.chdir('where you want to save final stage png file')
for one in allfile:
    if one=='.DS_Store': continue
    thisfi=path+'/'+one
    src = cv.imread(thisfi) 
    size=src.shape
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    size=gray.shape
    wet=size[1]
    wet1=int(int(40-wet)/2)
    wett=wet1
    if wet+wet1*2<40:
        wett=wett+1
    img_patch = cv.copyMakeBorder(gray, 0, 0, wet1, wett, cv.BORDER_CONSTANT, value=255)
    cv.imwrite(one,img_patch)

    

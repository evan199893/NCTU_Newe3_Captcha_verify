import cv2 as cv
import os
import numpy as np

path='where you save the step1 png file  '
allfile=os.listdir(path)
os.chdir('where save step2 png file')
for one in allfile:
    print(one)
    if one=='.DS_Store': continue
    thisfi=path+'/'+one
    src = cv.imread(thisfi)     
    ori=src
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
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
            print("1")
        elif count>25 and countright>35 and countup>8 and countlow<3:
            li.append(j+1)
            j+=18
            count1+=1
            print("2")
        elif countup>8 and countmid>6 and countlow>8 and count1>0:
            li.append(j+1)
            j+=18
            count1+=1
            print("3")
        elif count>=33:
            li.append(j+1)
            j+=18
            count1+=1
            print("4")
        elif count==36:
            li.append(j+2)
            j+=18
            count1+=1
            print("5")
        else:
            j+=1
        if count1==2:
            break
    print(li[:3])
    tmp=0
    ttmp=li[0]
    cc=0
    for w in range(4):
        a=ori[0:36,tmp:ttmp+1]
        if len(a[0])>=38:
            mid=int(len(a[0])/2)
            a1=a[0:36,0:mid]
            a2=a[0:36,mid:(mid*2)-1]
            st1=one+"_"+str(cc)+".png"
            st2=one+"_"+str(cc+1)+".png"
            cv.imwrite(st1,a1)
            if(w>=3): break
            if(cc>=2):break 
            cv.imwrite(st2,a2)
            if(cc>=2):break 
            tmp=li[cc]
            if(cc<2):
                ttmp=li[cc+1]-2
            else:
                ttmp=94
            cc+=1
        else: 
            strr=one+"_"+str(cc)+".png"
            cv.imwrite(strr,a)
            if(cc>2):break 
            tmp=li[cc]
            if(cc<2):
                ttmp=li[cc+1]-2
            else:
                ttmp=95
            cc+=1 
        
            
        
             
        



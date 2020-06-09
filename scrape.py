import requests
import os
import time

photolimit = 100000

folder_path ='./photo/'

if (os.path.exists(folder_path) == False): #判斷資料夾是否存在

    os.makedirs(folder_path) #Create folder

url = 'http://e3new.nctu.edu.tw/theme/dcpc/securimage/securimage_show.php'
headers = {'User-Agent': 'Mozilla/5.0'}

for i in range(photolimit):
    response = requests.get(url, headers = headers, stream=True) #使用header避免訪問受到限制
    img_name = folder_path + str(i+1) + ".png"
    with open(img_name, 'wb') as out_file:
        out_file.write(response.content)
    del response
    time.sleep(1)
    print(i)

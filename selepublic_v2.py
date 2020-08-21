from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import numpy as np
import os
import sys
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import cv2 as cv
import tensorflow as tf
from PIL import Image
import time
import split_digits_in_img
import threading
tStart = time.time()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

def loadm():
    global model 
    if os.path.isfile('cnn_model.h5'):
        print("Model found.")
        model = models.load_model('cnn_model.h5')
    else:
        print('No trained model found.')
        exit(-1)
def login():
    global Browser
    Browser = webdriver.Chrome()
    LoginUrl= ('https://e3new.nctu.edu.tw')
    Browser.set_window_size(1280,1024) 
    Browser.get(LoginUrl)
    global x_list
    with open('captcha1.png', 'wb') as file:
        file.write(Browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/form[1]/img').screenshot_as_png)
    img_rows = None
    img_cols = None
    digits_in_img=4
    model = None
    np.set_printoptions(suppress=True, linewidth=150, precision=9, formatter={'float': '{: 0.9f}'.format})
    img_filename = 'captcha1.png'
    img_array=cv.imread(img_filename,cv.IMREAD_GRAYSCALE)
    os.remove('captcha1.png')
    x_list = split_digits_in_img.split_digits_in_img(img_array)
    
def pred():
    global model
    global x_list
    global Browser
##Setting Student ID and password below 
    UserName= ('xxxxxx')
    UserPass= ('xxxxxx')
    varification_code = list()
    digits_in_img=4
    for i in range(digits_in_img):
        confidences = model.predict(np.array([x_list[i]]), verbose=1)
        result_class = model.predict_classes(np.array([x_list[i]]), verbose=1)
        varification_code.append(result_class[0])
    final=''
    print(varification_code)
    for i in range(4):
        final+=str(varification_code[i])
    Browser.find_element_by_id('username').send_keys(UserName)
    Browser.find_element_by_id('password').send_keys(UserPass)
    Browser.find_element_by_name('captcha_code').send_keys(final)
    Browser.find_element_by_id('password').send_keys(Keys.ENTER)
    sys.exit()
    ##Browser.quit()
thread_1=threading.Thread(target=loadm)
thread_2=threading.Thread(target=login)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
thread_3=threading.Thread(target=pred)
thread_3.start()
thread_3.join()
tEnd = time.time()
print (tEnd - tStart)
get_title = Browser.find_element_by_name('captcha_code').size
if get_title :
    thread_2_1=threading.Thread(target=login)
    thread_3_1=threading.Thread(target=pred)
    thread_2_1.start()
    thread_2_1.join()
    thread_3_1.start()
    thread_3_1.join()
else:
    print("Setting Fault.")

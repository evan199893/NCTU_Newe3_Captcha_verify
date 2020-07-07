import numpy as np
import os
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import matplotlib.pyplot as plt
epochs = 10      
img_rows = None   
img_cols = None  
x_list = list()   
y_list = list()   
x_train = list()  
y_train = list()  
x_test = list()   
y_test = list() 
os.chdir("/Users/evan/Desktop/BIML_project") 
pat="/Users/evan/Desktop/BIML_project/traning1/"
img_filenames = os.listdir("/Users/evan/Desktop/BIML_project/traning1")
 
for img_filename in img_filenames:
    if '.png' not in img_filename:
        continue
    position=img_filename.find('.')
    img = load_img(format(pat+img_filename), color_mode='grayscale')
    img_array = img_to_array(img)
    img_rows, img_cols, _ = img_array.shape
    print(img_array.shape)
    x_list.append(img_array[:,:]/255.0)
    y_list.append(img_filename[position-1])


y_list = keras.utils.to_categorical(y_list, num_classes=10)
x_train, x_test, y_train, y_test = train_test_split(x_list, y_list,test_size=0.25)
print(len(x_train), len(x_test))
print(len(y_train), len(y_test))
mopath = "/Users/evan/Desktop/BIML_project/cnn_model2.h5"

if os.path.isfile(mopath):
    model = models.load_model('/Users/evan/Desktop/BIML_project/cnn_model2.h5')
    print('Model loaded from file.')
else:
    model = models.Sequential()
    model.add(layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(36, 40, 1)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(rate=0.25))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(rate=0.5))
    model.add(layers.Dense(10, activation='softmax'))
    print('New model created.')
     
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])

history=model.fit(np.array(x_train), np.array(y_train), batch_size=1, epochs=epochs, verbose=2, validation_data=(np.array(x_test), np.array(y_test)))
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left') 
plt.show()
# summarize history for loss plt.plot(history.history['loss']) plt.plot(history.history['val_loss']) plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left') 
plt.show()
loss, accuracy = model.evaluate(np.array(x_test), np.array(y_test), verbose=0)
print('Test loss:', loss)
print('Test accuracy:', accuracy)
model.save('/Users/evan/Desktop/BIML_project/cnn_model2.h5')  

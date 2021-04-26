
import cv2 as cv
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


mnist = tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train,axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)



model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Adam(),
              metrics=['accuracy'])

model.fit(x_train,y_train, epochs=3)

loss,accuracy = model.evaluate(x_test,y_test)
print(loss)
print(accuracy)

model.save('predictors.model')
'''


model = tf.keras.models.load_model('predictors.model')



for x in range(2,7):
    img = cv.imread(f'{x}.png')[:,:,0]
    img = np.invert(np.array([img]))
   

    prediction = model.predict(img)
    print(f'The predicted number is {np.argmax(prediction)}')
    plt.imshow(img[0],cmap=plt.cm.binary)
    plt.show()
 '''
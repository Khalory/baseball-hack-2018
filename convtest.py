import keras
keras.__version__

from keras.preprocessing.image import load_img, img_to_array

import requests
from io import BytesIO
from PIL import Image
import numpy as np
from keras.applications import vgg19
from keras import backend as K, layers, Sequential

from scipy.optimize import fmin_l_bfgs_b
from scipy.misc import imsave
import time

from matplotlib import pyplot as plt


url = 'https://101clipart.com/wp-content/uploads/07/Baseball%20Seams%20Clipart%2013.jpg'
response = requests.get(url)


# This is the path to the image you want to transform.
target_image_path = BytesIO(response.content)

target_image = [Image.open(target_image_path)]
image_size = target_image[0].size
print(image_size)

model = Sequential()
model.add(layers.Conv2D(None, 3, strides=1, padding='same', data_format=None,
    dilation_rate=1, activation='linear', use_bias=True, kernel_initializer='glorot_uniform', 
    input_shape=(image_size[0], image_size[1], 1)))

input = target_image
output = target_image

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01),
              metrics=['accuracy'])

model.fit(input, output,
          batch_size=1,
          epochs=10,
          verbose=1,
          validation_data=(input, output),
          callbacks=[None])
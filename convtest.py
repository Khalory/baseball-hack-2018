import keras
keras.__version__

from keras.preprocessing.image import load_img, img_to_array

import requests
from io import BytesIO
from PIL import Image
import numpy as np
from keras.applications import vgg19
from keras import backend as K, layers

from scipy.optimize import fmin_l_bfgs_b
from scipy.misc import imsave
import time

from matplotlib import pyplot as plt


url = 'https://101clipart.com/wp-content/uploads/07/Baseball%20Seams%20Clipart%2013.jpg'
response = requests.get(url)


# This is the path to the image you want to transform.
target_image_path = BytesIO(response.content)

layers.Conv2D(None, 3, strides=1, padding='same', data_format=None, dilation_rate=1, activation='linear', use_bias=True, kernel_initializer='glorot_uniform', 
bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
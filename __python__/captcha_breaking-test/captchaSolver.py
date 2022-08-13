from claptcha import Claptcha
import pandas as pd
import os
import numpy as np
import cv2
import keras
from keras.models import Sequential,Model
from keras.layers import Dropout, Activation, Convolution2D, GlobalAveragePooling2D, merge,MaxPooling2D,Conv2D,Flatten,Dense,Input
from keras import backend as K
from keras.optimizers import Adam
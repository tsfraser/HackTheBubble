#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:01:41 2019

@author: tristanfraser
"""

from keras.datasets import...
# USING THEANO+ KERAS

import keras.utils as ku
import keras.backend as K
import keras.models as km, keras.layers as k1


# where galdata is an image with RGB values/fluxes
(x_train,y_train), (x_test,y_test) = galdata

y_train  = ku.to_categorical(y_train, 2)  # Onehot output: red,blue, misc (green)
y_test = ku.to_categorical(y_test,2)

x_train = x_train.reshape(N,20,20,M) # reshaping the data
x_test = x_test.shape(N/10, 20,20,M) 


N = 1000 # number of galaxies
M = 3 # rgb values
#P = 3 # interpolated flux values in the filters
#O = 2 # colortype - blue or red


    def get_mod(numfm,numnodes, inputshape = (20,20, 3)):
        
        model = km.Sequential()
        model.add(k1.Conv2D(numfm, kernel_size = (5,5)), in_shape =inputshape,  activation  = 'relu')
        
        model.add(k1.MaxPooling2D(pool_size  = (2,2),  strides = (2,2))
        
        model.add(k1.Flatten())
        model.add(k1.Dense(numnodes,activation  = 'tanh'))
        model.add(k1.Dense(10,activation = 'softmax'))
        
        return model
    
modelled = get_mod(20,100)


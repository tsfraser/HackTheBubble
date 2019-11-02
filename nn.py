#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:08:09 2019
Network
@author: tristanfraser
"""
import numpy as np
import numpy.random as npr
import time as time

# Sigmoid function.


def sigma(z):
  return 1. / (1. + np.exp(-z))
# Sigmoid prime function.
def sigmaprime(z):
  return sigma(z) * (1. - sigma(z))
# Returns just the predicted values.
def predict(x, model):
  _, _, _, a2 = forward(x, model)
  return np.argmax(a2, axis = 0)


# second network.py, continued
# Predict the output value, given the model
# and the positions.
  
def forward(x, model):
  # Hidden layer.
  z1 = model['w1'].dot(x.T) + model['b1']
  a1 = sigma(z1)
  # Output layer.
  z2 = model['w2'].dot(a1) + model['b2']
  a2 = sigma(z2)
  return z1, z2, a1, a2



def build_model(numnodes, x, v, eta, output_dim, num_steps = 10000, print_best = True): 
  input_dim = np.shape(x)[1]
  model = {'w1': npr.randn(numnodes, input_dim), 'b1': np.zeros([numnodes, 1]), \
           'w2': npr.randn(output_dim, numnodes), 'b2': np.zeros([output_dim, 1]) }

  z1, z2, a1, a2  = forward(x, model)

  start = time.time()
  for i in range(num_steps):
      if i // int(0.1*num_steps) == 0:
          print(1000*i/num_steps,'%')
      delta2 = a2; 
      #print( type(delta2), 'type')
      #print( type(v), 'type')
      #print(np.shape(delta2))
      #print(np.where(v == 3))
      
     # print(delta2[v])
      delta2[v.flatten(), range(len(v))] -= 1  
      #print(type(delta2), 'type')
      delta1 = (model['w2'].T).dot(delta2) * sigmaprime(z1)
      dCdb2 = np.sum(delta2, axis = 1, keepdims = True)
      dCdb1 = np.sum(delta1, axis = 1, keepdims = True)
      dCdw2 = delta2.dot(a1.T); dCdw1 = delta1.dot(x)
      print(dCdb2, dCdb1, dCdw2, dCdw1, 'partial derivatives of cost functions')
      model['w1'] -= eta * dCdw1; model['w2'] -= eta * dCdw2;
      model['b1'] -= eta * dCdb1; model['b2'] -= eta * dCdb2
      print(model['w1'],model['w2'],model['b1'],model['b2'] ,'model params')
      #print(type(model))
  #print(type(model))   
  stop =  time.time()


  print('Runtime: ', stop-start)      


    
    


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:24:37 2019

@author: tristanfraser
"""

import sklearn as sklearn
import sklearn.datasets as skd
import sklearn.model_selection as skms

# second network.py
import numpy as np
import numpy.random as npr
import pandas as pd
import nn as nn
import matplotlib.pyplot as plt
import plotting_routines as pr

#vals = np.genfromtxt('result.txt', skiprows = 1, usecols = (2,3,4,5,6) )
df  =  pd.read_csv('result.txt')
x = df.iloc[:,2:5]
#x = x.iloc[:,2:5]
y = df.iloc[:,7]
N = np.size(y)

u = x['u']
g = x['g']
r = x['r']
ug = u-g
gr = g

Xd = {'u-g': ug, 'g-r' : g }
X = pd.DataFrame(data= Xd)



x_data = X.to_numpy()
y_data = np.zeros(N, dtype = int)

y = y.tolist()


for i in range(len(y)):
    if y[i] == 'GALAXY':
        y_data[i] = 0
    elif y[i] == 'STAR':
        y_data[i] = 1

    #print('SOMETHING')







N = 500000
M = 100000

x_train,y_train  = x_data[:20000], y_data[:20000]




x_test,y_test = x_data[20000:40000], y_data[20000:40000]



#model = nn.build_model(10, x_train, y_train, eta = 0.01, output_dim = 2)
#pr.plot_decision_boundary(x_train, y_train, model, nn.predict)




# half baked attempt at implementing Kmeans clustering method
# aim was to reproduce a plot of color vs magnitude

from sklearn.cluster import  KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.datasets.samples_generator import make_blobs


#X = x_train
k_means = KMeans(init='k-means++',n_clusters=3, random_state=0).fit(X)



n_clusters = 2
fig = plt.figure(figsize=(8, 3))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)
colors = ['#4EACC5', '#FF9C34', '#4E9A06']

# We want to have the same colors for the same cluster from the
# MiniBatchKMeans and the KMeans algorithm. Let's pair the cluster centers per
# closest one.
k_means_cluster_centers = np.sort(k_means.cluster_centers_, axis=0)

k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)


# KMeans
ax = fig.add_subplot(1, 3, 1)
for k, col in zip(range(n_clusters), colors):
    my_members = k_means_labels == k
    cluster_center = k_means_cluster_centers[k]
    ax.plot(X[my_members, 0], X[my_members, 1], 'w',
            markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
            markeredgecolor='k', markersize=6)
ax.set_title('KMeans')
ax.set_xticks(())
ax.set_yticks(())
#plt.text(-3.5, 1.8,  'train time: %.2fs\ninertia: %f' % (t_batch, k_means.inertia_))


# Then check for best fit, and rerun the forward pass through the model.

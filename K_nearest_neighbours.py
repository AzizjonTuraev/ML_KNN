# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 23:45:39 2022

@author: Azizjon Turaev

UNSUPERVISED LEARNING: K-nearest Neighbours
"""

# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import seaborn; 


# Number of neighbours
K = 3

# Creating a random data
lower_level = 0
upper_level = 50
data_volume = 100

rand = np.random.RandomState(42)
X=rand.randint(lower_level,upper_level, (data_volume,2))


# Calculations of distances from each point

dist_sq = np.sum((X[:,np.newaxis,:] - X[np.newaxis,:,:]) ** 2, axis=-1)
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)


# =============================================================================

#######  RUN GRAPHS ONE BY ONE TO GET BETTER VISUALIZATION  #######

# =============================================================================
#graph_1

#plt.subplot(221)
seaborn.set() 
plt.scatter(X[:, 0], X[:, 1], s=100);

# =============================================================================



# =============================================================================
#graph_2

plt.scatter(X[:, 0], X[:, 1], s=100)

for i in range(X.shape[0]):
  for j in nearest_partition[i, :K+1]:
      plt.plot(*zip(X[j], X[i]), color='black')

# =============================================================================



# Enter which positioned points's neighbours you want to get
 
point_position = 55




# Finding each neighbour's location

neighbours = []

for i in range(K+1):
    if np.any(X[point_position]!=X[nearest_partition[point_position,i]]):
        neighbours.append(X[nearest_partition[point_position,i]])
    else:
        next
        
print(f"The {point_position}-point's {K} nearest neighbours are:\n")
for i in range(K):
    print(f'{i+1}-neighbour: [{neighbours[i][0]}:{neighbours[i][1]}]')        




# =============================================================================
#graph_3


plt.scatter(X[:, 0], X[:, 1], s=100)
      
for j in nearest_partition[point_position, :K+1]:
    plt.plot(*zip(X[j], X[point_position]), color='black')

plt.scatter(X[point_position][0], X[point_position][1], edgecolors='red')

# =============================================================================
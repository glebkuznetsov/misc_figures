#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Set higher dpi
mpl.rcParams['figure.dpi'] = 300


# First we search for one that looks good by trying different random seed.

# In[2]:


DIM = (12, 10)

NUM_FILLED = 8


def generate_random_matrix(seed):
    np.random.seed(seed)

    random_sparse_matrix = np.zeros(DIM, dtype=bool)

    for _ in range(NUM_FILLED):
        rand_row = np.random.randint(DIM[0])
        rand_col = np.random.randint(DIM[1])
        random_sparse_matrix[rand_row][rand_col] = True
        
    return random_sparse_matrix


def draw_grid(ax, data):
    
    heatmap = ax.pcolor(data, cmap='binary', edgecolor='black', linewidths=1)

    # Make squares
    ax.set_aspect('equal')

    # Turn off axis labels
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    

fig, axes = plt.subplots(5, 5, figsize=(20, 20))
for seed in range(25):
    # Generate matrix
    random_sparse_matrix = generate_random_matrix(seed)

    
    # draw it
    subplot_row = seed // 5
    subplot_col = seed % 5
    ax = axes[subplot_row, subplot_col]
    draw_grid(ax, random_sparse_matrix)
    ax.set_title('Seed %d' % seed)
    

plt.show()


# Now we'll use seed 18

# In[3]:


random_sparse_matrix = generate_random_matrix(18)
fig, ax = plt.subplots(figsize=(10, 10))
draw_grid(ax, random_sparse_matrix)


import matplotlib.pyplot as plt
import random as rd
import sys
from datetime import datetime

'''
    The objective of this code is to generate and display (or maybe even save as a picture) a labyrinth.
    I plan on making it so that you can make rectangle labyrinths, circular ones and maybe even 3D ones (either as a sort of cube, a cylinder and maybe someday a sphere).
'''

### Rectangle
''' Important variables definition '''

dir = {(1, 0): 'r', (-1, 0):'l', (0, 1):'u', (0, -1):'d'}

''' Grid setup'''
def r_grid(n:int, m:int):
    r = []
    for i in range(m):
        for j in range(n):
            r.append((j+1, i+1))
    return r

''' Adjacencies setup '''
def adjacencies(n:int, m:int):
    adj = {}
    nodes = r_grid(n, m)
    for i in nodes:
        for j in dir:
            if (i[0]+j[0], i[1]+j[1]) in nodes:
                if i in adj:
                    adj[i].append((i[0]+j[0], i[1]+j[1]))
                else:
                    adj[i] = [(i[0]+j[0], i[1]+j[1])]
    return adj

''' Plotting '''
def grid_plot(n:int, m:int):
    nodes = r_grid(n, m)
    fig = plt.figure()
    fig.set_facecolor('black')
    plt.axis('off')
    for i in nodes:
        plt.plot(i[1], -i[0], color = 'cyan', linestyle = 'None', marker = 'o')
    plt.show()

grid_plot(4, 5)
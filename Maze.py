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

dir = {(1, 0): 'r', (-1, 0):'l', (0, 1):'u', (0, -1):'d', (0, 0):'n'}
coor = {'r':(1, 0), 'l':(-1, 0), 'u':(0, 1), 'd':(0, -1), 'n':(0, 0)}
cell = 9

''' Grid setup'''
def r_grid(n:int, m:int) -> list:
    r = []
    for i in range(m):
        for j in range(n):
            r.append((j+1, i+1))
    return r

''' Adjacencies setup '''
def adjacencies(n:int, m:int) -> dict:
    adj = dict()
    nodes = r_grid(n, m)
    for i in nodes:
        for j in dir:
            if (i[0]+j[0], i[1]+j[1]) in nodes:
                if i in adj:
                    adj[i].append(dir[j])
                else:
                    adj[i] = [dir[j]]
    return adj

''' Initial configuration '''
def config_init(n:int, m:int) -> dict:
    adj = adjacencies(n, m)
    config = {}
    for i in adj:
        if 'r' in adj[i]:
            config[i] = 'r'
        elif 'd' in adj[i]:
            config[i] = 'd'
        else:
            config[i] = 'n'
    return config

''' Transformation '''
def transformation(config:dict, adj:dict) -> dict:
    config_f = config
    for i in config_f:
        if config_f[i] == 'n':
            config_f[i] = rd.choice(adj[i])
            config_f[(i[0]+coor[config_f[i]][0], i[1]+coor[config_f[i]][1])]='n'
    return config_f

''' Plotting '''
def path_plot(n:int, m:int, k:int):
    nodes = config_init(n, m)
    adj = adjacencies(n, m)
    for i in range(k):
        print("   ", i+1, "/", k, "   ", end = '\r')
        nodes = transformation(nodes, adj)
    fig = plt.figure()
    fig.set_facecolor('black')
    plt.axis('off')
    for i in nodes:
        plt.plot(i[0], i[1], color = 'cyan', linestyle = 'None', marker = 'o')
        plt.arrow(i[0], i[1], coor[nodes[i]][0], coor[nodes[i]][1], width = 0.05, color = 'cyan', length_includes_head = True)
    plt.show()


path_plot(15, 15, 100000)
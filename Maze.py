import matplotlib.pyplot as plt
import numpy as np
import random as rd
import time


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
            if ((i[0]+j[0], i[1]+j[1]) in nodes) and (dir[j]!='n'):
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

def o_config_init(n:int, m:int) -> tuple[dict, tuple]:
    adj = adjacencies(n, m)
    config = {}
    for i in adj:
        if 'r' in adj[i]:
            config[i] = 'r'
        elif 'd' in adj[i]:
            config[i] = 'd'
        else:
            config[i] = 'n'
            origin = i
    return config, origin

''' Transformation '''
def transformation(config:dict, adj:dict) -> dict:
    config_f = config
    for i in config_f:
        if config_f[i] == 'n':
            config_f[i] = rd.choice(adj[i])
            config_f[(i[0]+coor[config_f[i]][0], i[1]+coor[config_f[i]][1])]='n'
    return config_f

def o_transformation(config : dict, adj : dict, core : tuple) -> tuple[dict, tuple]:
    config[core] = rd.choice(adj[core])
    core = (core[0]+coor[config[core]][0], core[1]+coor[config[core]][1])
    config[core] = 'n'
    return config, core

''' Plotting path '''
def path_plot(n:int, m:int, k:int):
    start_time = time.time()
    nodes = config_init(n, m)
    adj = adjacencies(n, m)
    if k>0:
        for i in range(k):
            print("   ", i+1, "/", k, "   ", end = '\r')
            nodes = transformation(nodes, adj)
    fig = plt.figure()
    fig.set_facecolor('black')
    plt.axis('off')
    for i in nodes:
        plt.plot(i[0], i[1], color = 'white', linestyle = 'None', marker = 'o')
        plt.arrow(i[0], i[1], coor[nodes[i]][0], coor[nodes[i]][1], width = 0.05, color = 'cyan', length_includes_head = True)
    print("Path plotting : %ss" % (time.time() - start_time))
    plt.show()
    
''' Image generation '''
def canvas(n:int, m:int) -> list:
    r = []
    for i in range(9*n+2):
        r.append([])
        for j in range(9*m+2):
            if (j%9 == 0 or j%9 == 1) or (i%9 == 0 or i%9 == 1):
                r[-1].append((255, 255, 255))
            else:
                r[-1].append((0, 0, 0))
    return r

def im_nodes(n:int, m:int) -> list:
    c = canvas(n, m)
    for i in range(n):
        for j in range(m):
            c[9*i+5][9*j+5] = (255, 0, 255)
    return c

def im_path(n:int, m:int, k:bool = True) -> list:
    start_time = time.time()
    p = im_nodes(n, m)
    nodes = config_init(n, m)
    adj = adjacencies(n, m)
    N = n*m*10
    if k:
        for i in range(N):
            print("   ", i+1, "/", N, "   ", end = '\r')
            nodes = transformation(nodes, adj)
    for i in nodes:
        for j in range(9):
            if coor[nodes[i]][0] == 0:
                for k in range(7):
                    p[9*i[0]-k-1][9*i[1]-4+j*coor[nodes[i]][1]] = (0, 0, 0)
            else:
                for k in range(7):
                    p[9*i[0]-4+j*coor[nodes[i]][0]][9*i[1]-k-1] = (0, 0, 0)
    print("Image generation : %ss" % (time.time() - start_time))
    return p

def o_im_path(n:int, m:int, k:bool = True) -> list:
    start_time = time.time()
    p = im_nodes(n, m)
    nodes, core = o_config_init(n, m)
    adj = adjacencies(n, m)
    N = n*m*25
    if k:
        for i in range(N):
            print("   ", i+1, "/", N, "   ", end = '\r')
            nodes, core = o_transformation(nodes, adj, core)
    for i in nodes:
        for j in range(9):
            if coor[nodes[i]][0] == 0:
                for k in range(7):
                    p[9*i[0]-k-1][9*i[1]-4+j*coor[nodes[i]][1]] = (0, 0, 0)
            else:
                for k in range(7):
                    p[9*i[0]-4+j*coor[nodes[i]][0]][9*i[1]-k-1] = (0, 0, 0)
    timing = time.time() - start_time
    print("Image generation : %ss" % timing)
    return p, timing


''' Image plotting '''
def im_plot(pic:list):
    start_time = time.time()
    fig = plt.figure()
    fig.set_facecolor('black')
    plt.axis('off')
    plt.imshow(pic)
    print("Image Display : %ss" % (time.time() - start_time))
    plt.show()
    
''' Testing '''
def time_test(k:int) -> dict:
    test_start = time.time()
    sizes = [10*(i+1) for i in range(k)]
    times = dict()
    complexities = list()
    res = 0
    for i in sizes:
        for j in sizes:
            if j <= i:
                print('i :', i, '; j :', j, '    ')
                t = o_im_path(i, j)[1]
                times[(i, j)] = t
    print('\n', time.time() - test_start)
    for i in times:
        complexities.append(times[i]/(i[0]*i[1]))
    for j in complexities:
        res+=i
    res /= len(complexities)
    return res
times = time_test(10)
print(time)

''' Calling functions to make the maze '''
# im_plot(im_path(50, 70))
# im_plot(o_im_path(24, 92)[0])
# path_plot(15, 15, 1650)

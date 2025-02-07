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
opposites = {'r':'l', 'l':'r', 'u':'d', 'd':'u'}
cell = 9


''' Comfort functions '''
def add_vect(a, b):
    return (a[0]+b[0], a[1]+b[1])

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
            if ((i[0]+j[0], i[1]+j[1]) in nodes) and (dir[(j)]!='n'):
                if i in adj:
                    adj[i].append(dir[(j)])
                else:
                    adj[i] = [dir[(j)]]
    return adj

def o_adjacencies(n:int, m:int) -> dict:
    adj = dict()
    nodes = r_grid(n, m)
    for i in nodes:
        if i[0] == 1:
            if i[1] == 1:
                adj[i] = ['r', 'u']
            elif i[1] == m:
                adj[i] = ['r', 'd']
            else:
                adj[i] = ['r', 'u', 'd']
        elif i[0] == n:
            if i[1] == 1:
                adj[i] = ['l', 'u']
            elif i[1] == m:
                adj[i] = ['l', 'd']
            else:
                adj[i] = ['l', 'u', 'd']
        elif i[1] == 1:
            adj[i] = ['r', 'l', 'u']
        elif i[1] == m:
            adj[i] = ['r', 'l', 'd']
        else:
            adj[i] = ['r', 'l', 'u', 'd']
    return adj

''' Initial configuration '''
def o_config_init(n:int, m:int) -> tuple[dict, tuple]:
    adj = o_adjacencies(n, m)
    config = {}
    for i in adj:
        if 'r' in adj[i]:
            config[i] = 'r'
        elif 'd' in adj[i]:
            config[i] = 'd'
        else:
            config[i] = 'n'
            origin = i
    return config, origin, adj

''' Transformation '''
def o_transformation(config : dict, adj : dict, core : tuple) -> tuple[dict, tuple]:
    config[core] = rd.choice(adj[core])
    core = (core[0]+coor[config[core]][0], core[1]+coor[config[core]][1])
    config[core] = 'n'
    return config, core

def origin_switch(config : dict, adj : dict, core : tuple, coref : tuple) -> tuple[dict, tuple]:
    return config, core


''' Origin switch try'''
def origin_switch(maze:dict, init_core:tuple, final_core:tuple) -> tuple:
    cache = list()
    core_temp = final_core
    while core_temp != init_core:
        cache.append((add_vect(core_temp, coor[maze[core_temp]]), opposites[maze[core_temp]]))
        core_temp = (core_temp[0]+coor[maze[core_temp]][0], core_temp[1]+coor[maze[core_temp]][1])
    for i, j in cache:
        maze[i] = j
    maze[final_core] = 'n'
    return maze, final_core

''' Plotting path '''
def path_plot(n:int, m:int, k:int):
    start_time = time.time()
    nodes, core, adj = o_config_init(n, m)
    if k>0:
        for i in range(k):
            percentage = str(100*(i+1)/k)+'%'
            print("   ", i+1, "/", k, "   ", percentage, end = '\r')
            nodes, core = o_transformation(nodes, adj, core)
    fig = plt.figure()
    fig.set_facecolor('black')
    plt.axis('off')
    for i in nodes:
        if nodes[i]!='n':
            plt.plot(i[0], i[1], color = 'white', linestyle = 'None', marker = 'o')
            plt.arrow(i[0], i[1], coor[nodes[i]][0], coor[nodes[i]][1], width = 0.05, color = 'Blue', length_includes_head = True)
        else:
            plt.plot(i[0], i[1], color = 'red', linestyle = 'None', marker = 'o')
    print("Path plotting : %ss" % (time.time() - start_time))
    plt.show()
    return nodes

def path_edit(maze:dict, core:tuple, adj:dict, k:int=1):
    start_time = time.time()
    nodes = maze
    if k>0:
        for _ in range(k):
            nodes, core = o_transformation(nodes, adj, core)
    fig = plt.figure()
    fig.set_facecolor('black')
    plt.axis('off')
    for i in nodes:
        if nodes[i]!='n':
            plt.plot(i[0], i[1], color = 'white', linestyle = 'None', marker = 'o')
            plt.arrow(i[0], i[1], coor[nodes[i]][0], coor[nodes[i]][1], width = 0.05, color = 'Blue', length_includes_head = True)
        else:
            plt.plot(i[0], i[1], color = 'red', linestyle = 'None', marker = 'o')
    print("Path plotting : %ss" % (time.time() - start_time))
    plt.show()
    return nodes, core

def solved_path(maze:dict, core:tuple, adj:dict, k:int=1):
    start_time = time.time()
    nodes = maze
    if k>0:
        for _ in range(k):
            nodes, core = o_transformation(nodes, adj, core)
    fig = plt.figure()
    fig.set_facecolor('black')
    plt.axis('off')
    cache = list()
    node = (1, 1)
    iteration = 1
    while node!=core:
        cache.append(node)
        ax, ay = coor[nodes[node]]
        plt.plot(node[0], node[1], color = 'Green', linestyle = 'None', marker = 'o')
        plt.arrow(node[0], node[1], ax, ay, width = 0.05, color = 'Green', length_includes_head = True)
        node = add_vect(node, (ax, ay))
        iteration += 1
    print('   ', iteration, ' COMPLETE')
    for i in nodes:
        if nodes[i]!='n' and i not in cache:
            plt.plot(i[0], i[1], color = 'white', linestyle = 'None', marker = 'o')
            plt.arrow(i[0], i[1], coor[nodes[i]][0], coor[nodes[i]][1], width = 0.05, color = 'Blue', length_includes_head = True)
        elif nodes[i]=='n':
            plt.plot(i[0], i[1], color = 'red', linestyle = 'None', marker = 'o')
    print("Path plotting : %ss" % (time.time() - start_time))
    plt.show()
    return nodes, core
    
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
    for o in range(7):
        r[9*(m-1)+2+o][1] = (0, 0, 0)
        r[o+2][9*n] = (0, 0, 0)
        r[9*(m-1)+2+o][0] = (0, 0, 0)
        r[o+2][9*n+1] = (0, 0, 0)
    return r

def o_im_path(n:int, m:int, k:bool = True) -> list:
    start_time = time.time()
    p = canvas(n, m)
    print("Initial configuration generation...", end='\r')
    nodes, core, adj = o_config_init(n, m)
    print("Initial configuration generation   DONE")
    N = n*m*30
    if k:
        for _ in range(N):
            nodes, core = o_transformation(nodes, adj, core)
    timing = time.time() - start_time
    print("Path generation : %ss" % timing)
    start_time = time.time()
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
    return p


''' Image plotting '''
def im_plot(pic:list):
    start_time = time.time()
    fig = plt.figure()
    fig.set_facecolor('black')
    plt.axis('off')
    plt.imshow(pic)
    print("Image Display : %ss" % (time.time() - start_time))
    plt.show()

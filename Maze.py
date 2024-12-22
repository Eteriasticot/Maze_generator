import matplotlib.pyplot as plt
import random as rd
import sys
from datetime import datetime

'''
    The objective of this code is to generate and display (or maybe even save as a picture) a labyrinth.
    I plan on making it so that you can make rectangle labyrinths, circular ones and maybe even 3D ones (either as a sort of cube, a cylinder and maybe someday a sphere).
'''

### Rectangle

''' Grid setup'''
def r_grid(n:int, m:int):
    r = []
    for i in range(m):
        for j in range(n):
            r.append((j, i))
    return r

def vertices(n:int, m:int):
    gr = r_grid(n, m)
    adj = []
    for i in gr:
        for j in gr:
            if ((i[0]-j[0])**2+(i[1]-j[1])**2)==1 and ((j, i) not in adj):
                adj.append((i, j))
    return adj

def adjacency(n:int, m:int):
    vert = vertices(n,m)
    adj = {}
    for i in vert:
        if i[0] in adj:
            adj[i[0]].append(i[1])
        else : 
            adj[i[0]] = [i[1]]
        if i[1] in adj:
            adj[i[1]].append(i[0])
        else :
            adj[i[1]] = [i[0]]
    return adj


''' Initial configuration '''
def start_config(n:int, m:int):
    ad = vertices(n, m)
    path = []
    vert_start, vert_end = [], [] 
    for i in ad:
        if i[0][1] == i[1][1] and i[0]!=i[1]:
            path.append(i)
        elif i[0][0]==n-1 and i[0]!=i[1]:
            path.append(i)
    for i in path:
        vert_start.append(i[0])
        vert_end.append(i[1])
    return path, vert_start, vert_end

def core_init(n:int, m:int):
    p, vstart, vend = start_config(n, m)
    roots = [i for i in vstart if i not in vend]
    core = [j for j in vend if j not in vstart][0]
    roots = list(dict.fromkeys(roots))
    return roots, core, p



''' Transformation of previous configuration '''
def transformation(corei:tuple, path:list, n:int, m:int, adj:dict, corec:tuple):
    moves = adjacency(n, m)[corei]
    if corei==corec:
        coref = rd.choice(moves)
    else:
        moves.remove(corec)
        coref = rd.choice(moves)
    path.append((corei,coref))
    for i in adj[coref]:
        try:
            path.remove((coref, i))
        except:
            pass
    return coref, path, corei
    
def final_config(n:int, m:int, K:int):
    adj = adjacency(n, m)
    path = start_config(n,m)[0]
    core = core_init(n, m)[1]
    cache = tuple([i for i in core])
    for i in range(K):
        print("    "+str(i+1)+"/"+str(K)+"    ", end='\r')
        sys.stdout.flush()
        core, path, cache = transformation(core, path, n, m, adj, cache)
    print("    "+str(K)+"/"+str(K)+"    ")
    return core, path


''' Some optimization '''
def path_reformat(path:list, core:tuple):
    vend, vstart = [i[1] for i in path], [i[0]for i in path]
    roots = [i for i in vstart if i not in vend]
    plot_paths = {}
    for i in range(len(roots)):
        print("    "+str(i+1)+"/"+str(len(roots))+"    ", end='\r')
        adc = True
        while roots[i]!=core:
            if i in plot_paths:
                plot_paths[i].append(roots[i])
            else:
                plot_paths[i] = [roots[i]]
            for k in path:
                if k[0]==roots[i]:
                    roots[i]=k[1]
                    break
            for j in range(i):
                if roots[i] in plot_paths[j]:
                    plot_paths[i].append(roots[i])
                    adc = False
                    break
            else:
                continue
            break
        if adc:
            plot_paths[i].append(core)
    print("    "+str(len(roots))+"/"+str(len(roots))+"    ")
    return plot_paths


''' Plotting labyrinth '''
def plot_path_result(n:int, m:int, K:int):
    print("Calculating path . . .")
    core, path = final_config(n, m, K)
    print("Optimizing path plotting . . .")
    plot_path = path_reformat(path, core)
    grid = r_grid(n, m)
    x = [i[0] for i in grid]
    y = [i[1] for i in grid]
    print("Plotting . . .")
    
    f = plt.figure()
    f.patch.set_facecolor('black')
    plt.axis('off')
    for i in plot_path:
        xi, yi = [], []
        for j in plot_path[i]:
            xi.append(j[0])
            yi.append(j[1])
        plt.plot(xi, yi, color = 'cyan')
    plt.plot(x, y, linestyle = '', marker = 'o')
    plt.plot(core[0], core[1], linestyle = '', marker = 'o', color = 'red')
    print("Exec time :", datetime.now()-Start_time)
    plt.show()
    

Start_time = datetime.now()

plot_path_result(17, 20, 2000)

# I need to add a function to plot the walls
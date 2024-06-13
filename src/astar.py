import math
from ursina import *
from queue import PriorityQueue
from location import list_of_coords
from location import start, end, x_max, y_max, z_max

WALL = 2
BARRIER = 1
FREE = 0

UNFINDED = 0
FIND = 1

neighbors = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

#Manhattan distance 
def get_priority(tmp):
    x = abs(end[0] - tmp[0])
    y = abs(end[1] - tmp[1])
    z = abs(end[2] - tmp[2])
    priority = x + y + z
    return priority

#Euklidian distance
def get_priority2(tmp):
    x = pow((end[0] - tmp[0]), 2)
    y = pow((end[1] - tmp[1]), 2)
    z = pow((end[2] - tmp[2]), 2)
    priority = math.sqrt(x + y + z)
    return priority

#chack if next step is safe
def checkNeighbors(check_pos):
    for neib in neighbors:
        tmp = (check_pos[0] - neib[0], check_pos[1] - neib[1], check_pos[2] - neib[2])
        if(list_of_coords[tmp][2] == BARRIER):
            return False
    
    return True

def A_star():
    our_queue = PriorityQueue()
    our_queue.put((0,start))
    
    list_of_coords[tuple(start)][1] = FIND
    list_of_coords[tuple(start)][3] = 0
    find_path = False
    
    while(our_queue.empty() == False):
        tm = tuple(our_queue.get())
        curent_point = [-1,-1,-1]
        curent_point[0] = tm[1][0]
        curent_point[1] = tm[1][1]
        curent_point[2] = tm[1][2]
            
        if(tuple(curent_point) == end):
            find_path = True
            break
            
        for neib in neighbors:
            tmp = (curent_point[0] - neib[0], curent_point[1] - neib[1], curent_point[2] - neib[2])
            
            
            new_dist = 1 + list_of_coords[tuple(curent_point)][3]
            new_dist += get_priority(tmp)
            
            if((tmp[0] > 0) and (tmp[1] > 0) and (tmp[0] < x_max) and (tmp[1] < y_max) and (tmp[2] > 0) and (tmp[2] < z_max) and (checkNeighbors(tmp) == True)):
                if(((list_of_coords[tmp][1] == UNFINDED) and (list_of_coords[tmp][2] == FREE)) or ((new_dist < list_of_coords[tmp][3]) and (list_of_coords[tmp][2] == FREE))):
                    prior = new_dist
                    our_queue.put((prior, tmp))
                    list_of_coords[tmp][0][0] = curent_point[0]
                    list_of_coords[tmp][0][1] = curent_point[1]
                    list_of_coords[tmp][0][2] = curent_point[2]
                    list_of_coords[tmp][1] = FIND
                    list_of_coords[tmp][3] = list_of_coords[tuple(curent_point)][3] + 1
    
    return find_path


#path backtracking 
def get_path():
    path = []
    turn = tuple(end)
    while(turn != tuple(start)):
        path.append(list_of_coords[turn][0])
        turn = tuple(list_of_coords[turn][0])
    return path


#print path on the map
def PrintPath():
    path = get_path()
    for pos in path:
        Entity(model="cube", color=color.green, position=pos, 
            parent=scene, 
            collider="box", 
            texture="white_cube", 
            origin_y=0.5,
            ignore=True
        )
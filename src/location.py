from ursina import *
import random

WALL = 2
BARRIER = 1
FREE = 0

UNFINDED = 0
FIND = 1

BARRIER_COUNT = 500

list_of_coords = {}
start = (9,4,1)
end = (12,11,28)
x_max = 19
y_max = 14
z_max = 29

#init blank map
def init_map():
    for x in range(20):
        for y in range(15):
            for z in range(30):
                list_of_coords[(x,y,z)] = [[-1,-1,-1], UNFINDED, FREE, 99999999] #1.prev, 2.Find/unfind, 3.Free/Barrier, 4.len from start

#create map for robot
def CreateLocation():
    init_map()
    #create roof and floor
    for z in range(30):
        for x in range(20):
            Entity(model="cube", color=color.dark_gray, position=(x,0,z), 
                parent=scene, 
                collider="box", 
                texture="white_cube", 
                origin_y=0.5,
                ignore=True
            )
            list_of_coords[(x,0,z)] = [[-1,-1,-1], UNFINDED, WALL, 99999999]
        
            Entity(model="cube", color=color.dark_gray, position=(x,14,z), 
                parent=scene, 
                collider="box", 
                texture="white_cube", 
                origin_y=0.5,
                ignore=True
            )
            list_of_coords[(x,14,z)] = [[-1,-1,-1], UNFINDED, WALL, 99999999]
    
    #create walls   
    for y in range(15):
        for x in range(20):
            Entity(model="cube", color=color.dark_gray, position=(x,y,0), 
                parent=scene, 
                collider="box", 
                texture="white_cube", 
                origin_y=0.5,
                ignore=True
            )
            list_of_coords[(x,y,0)] = [[-1,-1,-1], UNFINDED, WALL, 99999999]
        
            Entity(model="cube", color=color.dark_gray, position=(x,y,29), 
                parent=scene, 
                collider="box", 
                texture="white_cube", 
                origin_y=0.5,
                ignore=True
            )
            list_of_coords[(x,y,29)] = [[-1,-1,-1], UNFINDED, WALL, 99999999]
    
    #create walls 
    for y in range(15):
        for z in range(30):
            Entity(model="cube", color=color.dark_gray, position=(0,y,z), 
               parent=scene, 
               collider="box", 
               texture="white_cube", 
               origin_y=0.5,
               ignore=True
            )
            list_of_coords[(0,y,z)] = [[-1,-1,-1], UNFINDED, WALL, 99999999]
        
            Entity(model="cube", color=color.dark_gray, position=(19,y,z), 
               parent=scene, 
               collider="box", 
               texture="white_cube", 
               origin_y=0.5,
               ignore=True
            )
            list_of_coords[(19,y,z)] = [[-1,-1,-1], UNFINDED, WALL, 99999999]
    
    #create bariers
    for i in range(BARRIER_COUNT):
        randX = random.randint(1,(x_max-1))
        randY = random.randint(1,(y_max-1))
        randZ = random.randint(1,(z_max-1))
        Entity(model="cube", color=color.red, position=(randX,randY,randZ), 
            parent=scene, 
            collider="box", 
            texture="white_cube", 
            origin_y=0.5,
            ignore=True
        )
        list_of_coords[(randX,randY,randZ)] = [[-1,-1,-1], UNFINDED, BARRIER, 99999999]
        
    #create start
    Entity(model="cube", color=color.blue, position=start, 
        parent=scene, 
        collider="box", 
        texture="white_cube", 
        origin_y=0.5,
        ignore=True
    )

    #create end
    Entity(model="cube", color=color.blue, position=end, 
        parent=scene, 
        collider="box", 
        texture="white_cube", 
        origin_y=0.5,
        ignore=True
    )
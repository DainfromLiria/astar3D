from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from location import CreateLocation
from astar import A_star, PrintPath
from colorama import Fore 

app = Ursina(size=(1440,800))
CreateLocation()

    
def input(key):
    if(key == 'escape'):
        quit()
    elif(key == 'enter'):
        if(A_star() == False):
            print(Fore.RED + "Save path not found", end='')
            quit()
        PrintPath()

player = FirstPersonController(position = (10, 10, 10))
app.run()
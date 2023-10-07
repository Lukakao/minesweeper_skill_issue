import pyautogui
import time
import random 
from grid import Grid
from grid import Celda
pyautogui.FAILSAFE = True

def isDead():
    pixel = pyautogui.pixel(pS[0]-4,pS[1]+6)
    if pixel[0] == 0:
        print("Se murio")
        return True
    else:
        return False

def rPos():
    return (random.randint(1,size_w-1),random.randint(1,size_h-1))


pL = pyautogui.center(pyautogui.locateOnScreen("izq.PNG"))
pL = (pL[0]+6, pL[1]-2, 0, 0)
pyautogui.moveTo(pL)

pR = pyautogui.center(pyautogui.locateOnScreen("der.PNG"))
pR = (pR[0]-4, pR[1]-3, 0, 0)
pyautogui.moveTo(pR)

pA = pyautogui.center(pyautogui.locateOnScreen("arriba.PNG"))
pA = (pA[0]+6+9, pA[1]+6+4, 0, 0)
pyautogui.moveTo(pA)

pS = pyautogui.center(pyautogui.locateOnScreen("smiley.PNG"))
pyautogui.click(pS[0]-4,pS[1]+6)
pyautogui.click()


def click(x,y):
    pyautogui.click(pA[0]+x*16,pA[1]+y*16)
def color(x,y):
    c = pyautogui.pixel(pA[0]+x*16,pA[1]+y*16)
    return c

# tile size 16px
size_h = int((pL[1]-pA[1]+4)/16)
size_w = int((pR[0]-pL[0])/16)

# (192,192,192) -> 0 y si 2 pixeles arriba es (255,255,255) -> sin clickear (9)
# (0,0,255)     -> 1
# (0,128,0)     -> 2
# (255,0,0)     -> 3
# (0, 0, 128)   -> 4
# (128, 0, 0)   -> 5
# (160, 0, 0)   -> 6
# (0, 0, 0)     -> 7 revisar si se murio primero
# (0, 0, 0) -> mina

grid = Grid(size_w,size_h)



def see_num_celda(x, y):
    color = pyautogui.pixel(pA[0]+x*16,pA[1]+y*16)
    if color == (192,192,192):
        if pyautogui.pixel(pA[0]+x*16,pA[1]+y*16-2) == (255,255,255):
            return 9 # sin clickear
        else:
            return 0 # vacio
    elif color == (0,0,255):
        return 1
    elif color == (0,128,0):
        return 2
    elif color == (255,0,0):
        return 3
    elif color == (0, 0, 128):
        return 4
    elif color == (128, 0, 0):
        return 5
    elif color == (0, 0, 0):
        return 7
    elif color == (128, 128, 128):
        return 5

def flood_fill(x,y):
    if x < 0 or x >= size_w or y < 0 or y >= size_h:
        return
    if grid.get_simcelda(x,y) == 1:
        return
    celda_actual_color = see_num_celda(x,y)
    if celda_actual_color == 9:
        return
    grid.set_simcelda(x,y)
    grid.set_celda(x, y, celda_actual_color)
    flood_fill(x+1, y)
    flood_fill(x-1, y)
    flood_fill(x, y+1)
    flood_fill(x, y-1)

for a in range(0,10):
    x,y = rPos()
    click(x,y)
    if isDead(): break
    print("pos ", x, y)
    celda_num = see_num_celda(x, y)
    print("num ", celda_num)
    grid.set_celda(x,y,celda_num)

    flood_fill(x,y)

grid.mostrar()
print("----------------------------")

grid.mostrar_sim()


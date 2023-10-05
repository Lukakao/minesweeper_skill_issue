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

print(size_h)
print(size_w)


# (192,192,192) -> 0 y si 6 pixeles arriba es (255,255,255) -> sin clickear (9)
# (0,0,255)     -> 1
# (0,128,0)     -> 2
# (255,0,0)     -> 3
# (0, 0, 128)   -> 4
# (128, 0, 0)   -> 5
# (160, 0, 0)   -> 6
# (0, 0, 0)     -> 7 revisar si se murio primero
# (0, 0, 0) -> mina


grid = Grid(size_w,size_h)

def actualizar_grid(gr, color, x, y):
    if color == (192,192,192):
        if pyautogui.pixel(x*16,y*16+6) == (255,255,255):
            gr.set_celda(x,y,9)
        else:
            gr.set_celda(x,y,0)
    elif color == (0,0,255):
        gr.set_celda(x,y,1)

    elif color == (0,128,0):
        gr.set_celda(x,y,2)

    elif color == (255,0,0):
        gr.set_celda(x,y,3)

    elif color == (0, 0, 128):
        gr.set_celda(x,y,4)


for a in range(0,10):
    x,y = rPos()
    print("rpos ", x,y)
    click(x,y)
    if isDead(): break
    c = color(x,y)
    print(c)
    actualizar_grid(grid,c, x, y)


grid.mostrar()
print("aa")
#for x in range(0,16,2):
 #   for y in range(0,16,2):
   #     pyautogui.moveTo(pA[0]+x,pA[1]+y)
   #     print(pyautogui.pixel(pA[0]+x,pA[1]+y))



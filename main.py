import sys
import pyautogui
import time
import random 
from grid import Grid
from grid import Celda

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0
# (192,192,192) -> 0 y si 2 pixeles arriba es (255,255,255) -> sin clickear (9)
# (0,0,255)     -> 1
# (0,128,0)     -> 2
# (255,0,0)     -> 3
# (0, 0, 128)   -> 4
# (128, 0, 0)   -> 5
# (160, 0, 0)   -> 6
# (0, 0, 0)     -> 7 revisar si se murio primero
# (0, 0, 0) -> mina


alive = True
ganado = False
offsets = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

def isDead(img):
    pixel = img.getpixel((4,3))
    if pixel[0] == 0:
        global alive
        alive = False
        print("Se murio")
        return True
    else:
        return False
    
def isGanado(img):
    pixel = img.getpixel((1,7))
    if pixel[0] == 0:
        global ganado
        ganado = True
    return False

def rPos():
    while True:
        x = random.randint(1,size_w-1)
        y = random.randint(1,size_h-1)
        if (x,y) in pos_used:
            continue
        #if grid.get_simcelda(x,y) == 0:
        pos_used.append((x,y))
        return (x,y)
        

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

# tile size 16px
size_h = int((pL[1]-pA[1]+4)/16)
size_w = int((pR[0]-pL[0])/16)

reg=(pA[0]-9, pA[1]-3, size_w*16, size_h*16)
grid = Grid(size_w,size_h)


def mover(x,y):
    pyautogui.moveTo(pA[0]+x*16,pA[1]+y*16)

def click(x,y):
    cel = grid.get_celda(x,y)
    if cel.isResuelta():
        return
    if cel.getNum() != -1:
        return
    pyautogui.click(pA[0]+x*16,pA[1]+y*16)
    im = pyautogui.screenshot(region=reg)
    imstate = pyautogui.screenshot(region=(pS[0]-8,pS[1]+3,6,10))
    if isDead(imstate):
        return
    if isGanado(imstate):
        return
    grid.eliminar_celda_bordes(x,y)
    # temp lista bordes []
    flood_fill(im, x,y)
    # agregar lista bordes a bordes
    grid.eliminar_repetidos_bordes()
    bordes = grid.get_bordes() # iterar en la ultima lista de bordes
    for pos in bordes:
        resolver_celda(pos[0],pos[1])


def flagear(x,y):
    if grid.get_celda(x,y).isResuelta():
        return
    pyautogui.click(pA[0]+x*16,pA[1]+y*16, button='right')
    grid.eliminar_celda_bordes(x,y)
    grid.get_celda(x,y).set_resuelta()
    grid.set_celda(x,y,10)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
def see_num_celda(img, x, y):
    color = img.getpixel( (x*16+9,y*16+3))

    if color == (192,192,192):
        if img.getpixel((x*16+9,y*16-2+3)) == (255,255,255):
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
        return 8

def flood_fill(img, x,y):
    if x < 0 or x >= size_w or y < 0 or y >= size_h:
        return
    if grid.get_simcelda(x,y) == 1:
        return
    cel = grid.get_celda(x,y)
    if cel.getNum() == 0:
        cel.set_resuelta()

    celda_actual_color = see_num_celda(img,x,y)
    if celda_actual_color == 9:
        grid.add_borde((x,y))
        return
    grid.set_simcelda(x,y)
    grid.set_celda(x, y, celda_actual_color)
    flood_fill(img,x+1, y)
    flood_fill(img,x-1, y)
    flood_fill(img,x, y+1)
    flood_fill(img,x, y-1)

def cantidad_disponibles(x,y): # esto es un numero adyacente a una celda no explorada
    posiciones = []
    flag_posiciones = []
    for of in offsets:
        x1 = x + of[0]
        y1 = y + of[1]
        if x1 < 0 or x1 >= size_w or y1 < 0 or y1 >= size_h:
            continue
        num = grid.get_celda(x1,y1).getNum()
        p = (x1, y1)
        if num == 10:
            flag_posiciones.append(p)
        elif num == -1:
            posiciones.append(p)
    #print(" Cantidad disponible: ", len(posiciones), "Cantidad flags: ", len(flag_posiciones))
    return posiciones, flag_posiciones

def resolver_celda(x,y): # resolviendo una celda no explorada (borde)
    # ver celdas adyacentes
    sn = grid.get_simcelda(x,y)
    if sn == 1:
        grid.eliminar_celda_bordes(x,y)
        return
    for of in offsets:
        x1 = x + of[0]
        y1 = y + of[1]
        if x1 < 0 or x1 >= size_w or y1 < 0 or y1 >= size_h:
            continue
        actual = grid.get_celda(x1,y1)
        num = actual.getNum()
        if num == -1:
            continue
        available, flags = cantidad_disponibles(x1,y1)
    
        if len(available)+len(flags) == num:
            for pos in available:
                flagear(pos[0],pos[1])
            grid.eliminar_celda_bordes(x,y)
        elif num == len(flags):
            for pos in available:
                click(pos[0],pos[1])
                grid.eliminar_celda_bordes(pos[0],pos[1])
            grid.eliminar_celda_bordes(x,y)

pos_used = []


click(0,0)
click(0,size_h-1)
click(size_w-1,0)
click(size_w-1,size_h-1)
while alive and not ganado:
    x,y = rPos()
    click(x,y)
    # por cada borde resolver

    

grid.mostrar()
print("-"*(2*size_w+size_w))
grid.mostrar_sim()


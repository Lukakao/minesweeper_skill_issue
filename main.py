import pyautogui
import time
import random 
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
pR = pyautogui.center(pyautogui.locateOnScreen("der.PNG"))
pA = pyautogui.center(pyautogui.locateOnScreen("arriba.PNG"))
pA = (pA[0]+6+9, pA[1]+6+4, 0, 0)
pS = pyautogui.center(pyautogui.locateOnScreen("smiley.PNG"))
pyautogui.click(pS[0]-4,pS[1]+6)
pyautogui.click()


def click(x,y):
    pyautogui.click(pA[0]+x*16,pA[1]+y*16)
def color(x,y):
    c = pyautogui.pixel(pA[0]+x*16,pA[1]+y*16)
    return c

# tile size 16px
size_h = int((pL[1]-pA[1])/16)
size_w = int((pR[0]-pL[0])/16)

print(size_h)
print(size_w)


# (192,192,192) -> 0 y si 6 pixeles arriba es (255,255,255) -> sin clickear
# (0,0,255)     -> 1
# (0,128,0)     -> 2
# (255,0,0)     -> 3
# (0, 0, 128)   -> 4
# (128, 0, 0)   -> 5
# (160, 0, 0)   -> 6
# (0, 0, 0)     -> 7 revisar si se murio primero
# (0, 0, 0) -> mina

for a in range(0,10):
    x,y = rPos()
    click(x,y)
    if isDead(): break
    c = color(x,y)
    print(c)

#for x in range(0,16,2):
 #   for y in range(0,16,2):
   #     pyautogui.moveTo(pA[0]+x,pA[1]+y)
   #     print(pyautogui.pixel(pA[0]+x,pA[1]+y))



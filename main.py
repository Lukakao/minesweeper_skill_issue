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
    return (random.randint(1,size_w),random.randint(1,size_h))




pL = pyautogui.center(pyautogui.locateOnScreen("izq.PNG"))
pR = pyautogui.center(pyautogui.locateOnScreen("der.PNG"))
pA = pyautogui.center(pyautogui.locateOnScreen("arriba.PNG"))
pA = (pA[0]+6+8, pA[1]+6+4, 0, 0)
pS = pyautogui.center(pyautogui.locateOnScreen("smiley.PNG"))
print("pos",pS)
pyautogui.click(pS[0]-4,pS[1]+6)
pyautogui.click()

print("pa", pA)

def click(x,y):
    pyautogui.click(pA[0]+x*16,pA[1]+y*16)

# (width,height)

# conseguir map size
try:
    print("coordenada",pA[1])   
    pyautogui.moveTo(pL)
except:
    pass

# tile size 16px
size_h = int((pL[1]-pA[1])/16)
size_w = int((pR[0]-pL[0])/16)

print(size_h)
print(size_w)

pyautogui.moveTo(pA)
pyautogui.click()
time.sleep(0.9)
print(pyautogui.pixel(pA[0],pA[1]))
#for a in range(0,10):
#    x,y = rPos()
#    click(x,y)
#    if isDead(): break
#    time.sleep(0.2)

#for x in range(0,16,2):
 #   for y in range(0,16,2):
   #     pyautogui.moveTo(pA[0]+x,pA[1]+y)
   #     print(pyautogui.pixel(pA[0]+x,pA[1]+y))



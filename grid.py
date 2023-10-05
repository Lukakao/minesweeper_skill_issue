


class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[Celda() for i in range(h)] for j in range(w)] 


    def mostrar(self):
        for x in range(0,self.h):
            s = ''
            a = ''
            b = ' '
            for y in range(0,self.w):
                num = self.grid[x][y].getNum()
                if num != -1: 
                    a = ' '
                    b = ''
                s = s + a + str(num) + b
            print(s)

    def set_celda(self,x,y, n):
        self.grid[x][y].setNum(n)

class Celda:
    def __init__(self):
        self.conocida = False
        self.num = -1
        self.lista = False
    
    def setNum(self, n):
        self.num = n
    
    def getNum(self):
        return self.num
    



#g = Grid(5,16)
#g.mostrar()
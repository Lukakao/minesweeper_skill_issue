


class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[Celda() for i in range(h)] for j in range(w)] 
        self.simgrid = [[0 for i in range(h)] for j in range(w)]  # 1 es chequeado, 0 es no
        self.bordes = []

    def celda_isResuelta(self,x,y):
        return self.grid.isResuelta()


    def mostrar(self):
        for x in range(0,self.h):
            s = ''
            a = ' '
            for y in range(0,self.w):
                num = self.grid[y][x].getNum()
                if num == -1:
                    num = '□'
                elif num == 0:
                    num = ' '
                s = s + a + str(num) + a
            print(s)

    def mostrar_sim(self):
        for x in range(0,self.h):
            s = ''
            for y in range(0,self.w):
                s = s + str(self.simgrid[y][x]) + '  '
            print(s)

    def revisar_bordes_no_existentes(self): # creo que esta no es tan necesaria, ya al tiro se puede saber si la celda no existente, no existe (lol)
        print("len bordes2 ", len(self.bordes))
        for i in range(0,len(self.bordes)-1):
            actual = self.bordes[i]
            if self.simgrid[actual[0]][actual[1]] == 1:
                # esta celda ya se exploró
                self.eliminar_celda_bordes(actual[0],actual[1])

    def eliminar_repetidos_bordes(self):
        res = []
        [res.append(x) for x in self.bordes if x not in res]
        self.bordes = res
        print("len bordes ", len(self.bordes))
        return self.bordes
    
    def eliminar_celda_bordes(self,x,y):
        leng = len(self.bordes)-1
        for i in range(0,leng):
            actual = self.bordes[i]
            if actual[0] == x:
                if actual[1] == y:
                    # eliminar
                    inf = self.bordes[:i]
                    sup = []
                    if i < leng:
                        sup = self.bordes[i+1:]
                    res = inf + sup
                    self.bordes = res

    def get_bordes(self):
        return self.bordes

    def add_borde(self, tupla):
        self.bordes.append(tupla)
    
    def set_celda(self,x,y, n):
        self.grid[x][y].setNum(n)
    
    def set_simcelda(self,x,y):
        self.simgrid[x][y] = 1

    def get_celda(self,x,y):
        return self.grid[x][y]
    
    def get_simcelda(self,x,y):
        return self.simgrid[x][y]

    def get_simgrid(self):
        return self.simgrid

    def get_grid(self):
        return self.grid

class Celda:
    def __init__(self):
        self.conocida = False
        self.num = -1
        self.lista = False
    
    def setNum(self, n):
        self.num = n
    
    def getNum(self):
        return self.num
    
    def isResuelta(self):
        return self.lista



#g = Grid(5,16)
#g.mostrar()
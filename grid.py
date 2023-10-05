


class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[Celda()]*w]*h


    def mostrar(self):
        for x in range(0,self.h):
            s = ''
            for y in range(0,self.w):
                s = s + str(self.grid[x][y].num)
            print(s)

class Celda:
    def __init__(self):
        self.conocida = False
        self.num = -1
        self.lista = False


g = Grid(5,16)
g.mostrar()
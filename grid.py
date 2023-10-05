


class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[0]*w]*h

    def mostrar(self):
        print(self.grid)


class Celda:
    def __init__(self):
        self.conocida = False
        self.num = -1
        self.lista = False


g = Grid(2,3)
g.mostrar()
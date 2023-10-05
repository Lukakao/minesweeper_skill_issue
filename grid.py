


class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[0]*w]*h

    def mostrar(self):
        print(self.grid)




g = Grid(2,3)
g.mostrar()
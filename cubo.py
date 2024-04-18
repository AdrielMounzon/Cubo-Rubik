import copy
import numpy

class Cara:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
class Capa:
    def __init__(self, c1, c2, c3, c4, c5, c6, c7, c8, c9):
        self.caras = numpy.array([[Cara(c1), Cara(c2), Cara(c3)], [Cara(c4), Cara(c5), Cara(c6)], [Cara(c7), Cara(c8), Cara(c9)]])

    def imprimir(self):
        for fila in self.caras:
            for cara in fila:
                print(cara.get_color(), end="")
            print()

    def get_caras(self):
        return self.caras


class Cubo:
    def __init__(self, c1, c2, c3, c4, c5, c6):
        self.capas = {"F":c1, "L":c2, "U":c3, "R":c4, "D":c5, "B":c6}
    
    def imprimir(self):
        for letra, capa in self.capas.items():
            print(letra + ":")
            capa.imprimir()
            print()

    def Mover(self, capas_afectadas, filas, columnas, inversos, capa_rotada, k):
        columnas = [slice(None) if col == ':' else col for col in columnas]
        filas = [slice(None) if fil == ':' else fil for fil in filas]
        capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[filas[3], columnas[3]][::inversos[3]])
        for i in range(0,3):
            self.capas[capas_afectadas[3-i]].get_caras()[filas[3-i], columnas[3-i]] = self.capas[capas_afectadas[2-i]].get_caras()[filas[2-i], columnas[2-i]][::inversos[2-i]]
        self.capas[capas_afectadas[0]].get_caras()[filas[2-i], columnas[2-i]] = capa
        self.capas[capa_rotada].get_caras()[:] = numpy.rot90(self.capas[capa_rotada].get_caras(), k=k)

    def  U(self):
         self.Mover(["F", "L", "B", "R"], [0, 0, 0, 0],[":", ":", ":", ":"], [1, 1, 1, 1], "U", 3) 

    def Up(self):
        self.Mover(["F", "R", "B", "L"], [0, 0, 0, 0],[":", ":", ":", ":"], [1, 1, 1, 1], "U", 1) 

    def D(self):
        self.Mover(["F", "R", "B", "L"], [2, 2, 2, 2],[":", ":", ":", ":"], [1, 1, 1, 1], "D", 3) 

    def Dp(self):
        self.Mover(["F", "L", "B", "R"], [2, 2, 2, 2],[":", ":", ":", ":"], [1, 1, 1, 1], "D", 1) 

    def L(self):
        self.Mover(["F", "D", "B", "U"], [":", ":", ":", ":"], [0, 0, 2, 0], [1, -1, -1, 1], "L", 3)

    def Lp(self):
        self.Mover(["F", "U", "B", "D"], [":", ":", ":", ":"], [0, 0, 2, 0], [1, -1, -1, 1], "L", 1)

    def R(self):
        self.Mover(["F", "U", "B", "D"], [":", ":", ":", ":"], [2, 2, 0, 2], [1, -1, -1, 1], "R", 3)
    
    def Rp(self):
        self.Mover(["F", "D", "B", "U"], [":", ":", ":", ":"], [2, 2, 0, 2], [1, -1, -1, 1], "R", 1)

    def F(self):
        self.Mover(["L", "U", "R", "D"], [":", 2, ":", 0], [2, ":", 0, ":"], [-1, 1, -1, 1], "F", 3)

    def Fp(self):
        self.Mover(["L", "D", "R", "U"], [":", 0, ":", 2], [2, ":", 0, ":"], [1, -1, 1, -1], "F", 1)

    def B(self):
        self.Mover(["L", "D", "R", "U"], [":", 2, ":", 0], [0, ":", 2, ":"], [1, -1, 1, -1], "B", 3)

    def Bp(self):
        self.Mover(["L", "U", "R", "D"], [":", 0, ":", 2], [0, ":", 2, ":"], [-1, 1, -1, 1], "B", 1)
    


capa1 = Capa("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9")
capa2 = Capa("O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9")
capa3 = Capa("W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9")
capa4 = Capa("R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9")
capa5 = Capa("Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9")
capa6 = Capa("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9")

cubo = Cubo(capa1, capa2, capa3, capa4, capa5, capa6)


# capa11 = Capa('R', 'Y', 'B', 'G', 'G', 'R', 'W', 'O', 'Y')
# capa12 = Capa('R', 'R', 'B', 'W', 'Y', 'O', 'O', 'B', 'O')
# capa13 = Capa('B', 'Y', 'R', 'G', 'O', 'Y', 'Y', 'R', 'O')
# capa14 = Capa('Y', 'G', 'W', 'W', 'W', 'B', 'O', 'W', 'G')
# capa15 = Capa('G', 'W', 'G', 'O', 'R', 'G', 'B', 'R', 'Y')
# capa16 = Capa('G', 'O', 'W', 'Y', 'B', 'B', 'R', 'B', 'W')

# cubo2 = Cubo(capa11, capa12, capa13, capa14, capa15, capa16)



# cubo2.L()
# cubo2.U()
# cubo2.U()
# cubo2.Fp()
# cubo2.B()
# cubo2.B()
# cubo2.Rp()
# cubo2.F()
# cubo2.F()
# cubo2.Lp()
# cubo2.Dp()
# cubo2.F()
# cubo2.F()
# cubo2.L()
# cubo2.U()
# cubo2.R()
# cubo2.R()
# cubo2.B()
# cubo2.U()
# cubo2.U()
# cubo2.L()
# cubo2.L()
# cubo2.B()
# cubo2.B()
# cubo2.D()
# cubo2.B()
# cubo2.B()
# cubo2.Dp()
# cubo2.B()
# cubo2.B()

# cubo2.imprimir()
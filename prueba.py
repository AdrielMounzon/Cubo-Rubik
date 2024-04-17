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

    def MoverColumna2(self, capas_afectadas, filas, columnas, inversos, capa_rotada, k):
        self.Mover(capas_afectadas, filas, columnas, inversos, capa_rotada, k)

    def MoverFila(self, capas_afectadas, capa_rotada, k, fila):
        capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[fila])
        for i in range(0,3):
            self.capas[capas_afectadas[3-i]].get_caras()[fila] = self.capas[capas_afectadas[2-i]].get_caras()[fila]
        self.capas[capas_afectadas[0]].get_caras()[fila] = capa
        self.capas[capa_rotada].get_caras()[:] = numpy.rot90(self.capas[capa_rotada].get_caras(), k=k)

    def MoverColumna(self, capas_afectadas, capa_rotada, k, columna):
        capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,columna])
        for i in range(0,3):
            if capas_afectadas[2-i]=="B":
                self.capas[capas_afectadas[3-i]].get_caras()[:,columna] = self.capas[capas_afectadas[2-i]].get_caras()[:,(columna==0)*2][::-1]
            else:
                self.capas[capas_afectadas[3-i]].get_caras()[:,columna] = self.capas[capas_afectadas[2-i]].get_caras()[:,columna]
        self.capas[capas_afectadas[0]].get_caras()[:,columna] = capa
        self.capas[capa_rotada].get_caras()[:] = numpy.rot90(self.capas[capa_rotada].get_caras(), k=k)

    def MoverFilaColumna(self, capas_afectadas, posiciones, capa_rotada, k):
        f4=copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[posiciones[3]])
        self.capas[capas_afectadas[3]].get_caras()[posiciones[3]] = self.capas[capas_afectadas[2]].get_caras()[:,posiciones[2]][::-1]
        self.capas[capas_afectadas[2]].get_caras()[:,posiciones[2]] = self.capas[capas_afectadas[1]].get_caras()[posiciones[1]]
        self.capas[capas_afectadas[1]].get_caras()[posiciones[1]] = self.capas[capas_afectadas[0]].get_caras()[:,posiciones[0]][::-1]
        self.capas[capas_afectadas[0]].get_caras()[:,posiciones[0]] = f4
        self.capas[capa_rotada].get_caras()[:] = numpy.rot90(self.capas[capa_rotada].get_caras(), k=k)

    def MoverFilaColumnaInverso(self, capas_afectadas, posiciones, capa_rotada, k):
        f4=copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[posiciones[3]])
        self.capas[capas_afectadas[3]].get_caras()[posiciones[3]] = self.capas[capas_afectadas[2]].get_caras()[:,posiciones[2]]
        self.capas[capas_afectadas[2]].get_caras()[:,posiciones[2]] = self.capas[capas_afectadas[1]].get_caras()[posiciones[1]][::-1]
        self.capas[capas_afectadas[1]].get_caras()[posiciones[1]] = self.capas[capas_afectadas[0]].get_caras()[:,posiciones[0]]
        self.capas[capas_afectadas[0]].get_caras()[:,posiciones[0]] = f4[::-1]
        self.capas[capa_rotada].get_caras()[:] = numpy.rot90(self.capas[capa_rotada].get_caras(), k=k)


    def  U(self):
         self.MoverFila(["F", "L", "B", "R"], "U", 3, 0)  

    def Up(self):
        self.MoverFila(["F", "R", "B", "L"], "U", 1, 0)

    def D(self):
        self.MoverFila(["F", "R", "B", "L"], "D", 3, 2)

    def Dp(self):
        self.MoverFila(["F", "L", "B", "R"], "D", 1, 2)

    def L(self):
        self.MoverColumna(["F", "D", "B", "U"], "L", 3, 0)

    def L2(self):
        self.MoverColumna2(["F", "D", "B", "U"], [":", ":", ":", ":"], [0, 0, 2, 0], [1, 1, -1, 1], "L", 3)

    def Lp(self):
        self.MoverColumna(["F", "U", "B", "D"], "L", 1, 0)
    
    def R(self):
        self.MoverColumna(["F", "U", "B", "D"], "R", 3, 2)

    def Rp(self):
        self.MoverColumna(["F", "D", "B", "U"], "R", 1, 2)

    def F(self):
        self.MoverFilaColumna(["L", "U", "R", "D"], [2, 2, 0, 0], "F", 3)

    def Fp(self):
        self.MoverFilaColumnaInverso(["L", "D", "R", "U"], [2, 0, 0, 2], "F", 1)

    def B(self):
        self.MoverFilaColumnaInverso(["L", "D", "R", "U"], [0, 2, 2, 0], "B", 3)

    def Bp(self):
        self.MoverFilaColumna(["L", "U", "R", "D"], [0, 0, 2, 2], "B", 1)
    


capa1 = Capa("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9")
capa2 = Capa("O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9")
capa3 = Capa("W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9")
capa4 = Capa("R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9")
capa5 = Capa("Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9")
capa6 = Capa("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9")

cubo = Cubo(capa1, capa2, capa3, capa4, capa5, capa6)

# cubo.R()
# cubo.R()
# cubo.L()
# cubo.L()
# cubo.F()
# cubo.F()
# cubo.B()
# cubo.B()
# cubo.U()
# cubo.U()
# cubo.D()
# cubo.D()

cubo.L2()


# cubo.R()
# cubo.U()
# cubo.Fp()
# cubo.Lp()
# cubo.B()
# cubo.D()
# cubo.Rp()
# cubo.F()
# cubo.U()
# cubo.Bp()
# cubo.D()
# cubo.L()
# cubo.Up()
# cubo.Fp()
# cubo.R()


cubo.imprimir()
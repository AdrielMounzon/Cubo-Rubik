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


    def  Unuevo(self):
         self.Mover(["F", "L", "B", "R"], "U", 3)

    def U(self):
            capas_afectadas = ["F", "L", "B", "R"] 
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[0])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[0] = self.capas[capas_afectadas[2-i]].get_caras()[0]
            self.capas[capas_afectadas[0]].get_caras()[0] = capa
            self.capas["U"].get_caras()[:] = numpy.rot90(self.capas["U"].get_caras(), k=3)

    def Mover(self, capas_afectadas, capa_rotada, k):
        capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[0])
        for i in range(0,3):
            self.capas[capas_afectadas[3-i]].get_caras()[0] = self.capas[capas_afectadas[2-i]].get_caras()[0]
        self.capas[capas_afectadas[0]].get_caras()[0] = capa
        self.capas[capa_rotada].get_caras()[:] = numpy.rot90(self.capas[capa_rotada].get_caras(), k=k)

    def Up(self):
            capas_afectadas = ["F", "R", "B", "L"] 
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[0])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[0] = self.capas[capas_afectadas[2-i]].get_caras()[0]
            self.capas[capas_afectadas[0]].get_caras()[0] = capa
            self.capas["U"].get_caras()[:] = numpy.rot90(self.capas["U"].get_caras(), k=1)

    def D(self):
            capas_afectadas = ["F", "R", "B", "L"] 
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[2])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[2] = self.capas[capas_afectadas[2-i]].get_caras()[2]
            self.capas[capas_afectadas[0]].get_caras()[2] = capa
            self.capas["D"].get_caras()[:] = numpy.rot90(self.capas["D"].get_caras(), k=3)

    def Dp(self):
            capas_afectadas = ["F", "L", "B", "R"] 
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[2])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[2] = self.capas[capas_afectadas[2-i]].get_caras()[2]
            self.capas[capas_afectadas[0]].get_caras()[2] = capa
            self.capas["D"].get_caras()[:] = numpy.rot90(self.capas["D"].get_caras(), k=1)  

    def L(self):
            capas_afectadas = ["F", "D", "B", "U"]
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,0])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[:,0] = self.capas[capas_afectadas[2-i]].get_caras()[:,0]
            self.capas[capas_afectadas[0]].get_caras()[:,0] = capa
            self.capas["L"].get_caras()[:] = numpy.rot90(self.capas["L"].get_caras(), k=3)

    def Lp(self):
            capas_afectadas = ["F", "U", "B", "D"]
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,0])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[:,0] = self.capas[capas_afectadas[2-i]].get_caras()[:,0]
            self.capas[capas_afectadas[0]].get_caras()[:,0] = capa
            self.capas["L"].get_caras()[:] = numpy.rot90(self.capas["L"].get_caras(), k=1)
    
    def R(self):
            capas_afectadas = ["F", "U", "B", "D"]
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,2])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[:,2] = self.capas[capas_afectadas[2-i]].get_caras()[:,2]
            self.capas[capas_afectadas[0]].get_caras()[:,2] = capa
            self.capas["R"].get_caras()[:] = numpy.rot90(self.capas["R"].get_caras(), k=3)

    def Rp(self):
            capas_afectadas = ["F", "D", "B", "U"]
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,2])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[:,2] = self.capas[capas_afectadas[2-i]].get_caras()[:,2]
            self.capas[capas_afectadas[0]].get_caras()[:,2] = capa
            self.capas["R"].get_caras()[:] = numpy.rot90(self.capas["R"].get_caras(), k=1)

    def F(self):
            capas_afectadas = ["L", "U", "R", "D"]
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,2])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[:,2] = self.capas[capas_afectadas[2-i]].get_caras()[:,2]
            self.capas[capas_afectadas[0]].get_caras()[:,2] = capa
            self.capas["F"].get_caras()[:] = numpy.rot90(self.capas["F"].get_caras(), k=3)

    #Probar a partir de aqui
    def Fp(self):
            capas_afectadas = ["L", "D", "R", "U"]
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,2])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[:,2] = self.capas[capas_afectadas[2-i]].get_caras()[:,2]
            self.capas[capas_afectadas[0]].get_caras()[:,2] = capa
            self.capas["F"].get_caras()[:] = numpy.rot90(self.capas["F"].get_caras(), k=1)

    def B(self):
            capas_afectadas = ["L", "U", "R", "D"]
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,0])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[:,0] = self.capas[capas_afectadas[2-i]].get_caras()[:,0]
            self.capas[capas_afectadas[0]].get_caras()[:,0] = capa
            self.capas["B"].get_caras()[:] = numpy.rot90(self.capas["B"].get_caras(), k=3)

    def Bp(self):
            capas_afectadas = ["L", "D", "R", "U"]
            capa = copy.deepcopy(self.capas[capas_afectadas[3]].get_caras()[:,0])
            for i in range(0,3):
                self.capas[capas_afectadas[3-i]].get_caras()[:,0] = self.capas[capas_afectadas[2-i]].get_caras()[:,0]
            self.capas[capas_afectadas[0]].get_caras()[:,0] = capa
            self.capas["B"].get_caras()[:] = numpy.rot90(self.capas["B"].get_caras(), k=1)
    


capa1 = Capa("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9")
capa2 = Capa("R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9")
capa3 = Capa("W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9")
capa4 = Capa("O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9")
capa5 = Capa("Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9")
capa6 = Capa("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9")

cubo = Cubo(capa1, capa2, capa3, capa4, capa5, capa6)

cubo.Unuevo()

cubo.imprimir()
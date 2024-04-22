import copy
import numpy

class Cara:
    def __init__(self, color):
        self.color = color

    def __eq__(self, other):
        if(isinstance(other, Cara)):
            return self.color == other.color

    def get_color(self):
        return self.color
    
class Capa:
    def __init__(self, c1, c2, c3, c4, c5, c6, c7, c8, c9):
        self.caras = numpy.array([[Cara(c1), Cara(c2), Cara(c3)], [Cara(c4), Cara(c5), Cara(c6)], [Cara(c7), Cara(c8), Cara(c9)]])

    def __eq__(self, other):
            if isinstance(other, Capa):
                return numpy.array_equal(self.caras, other.caras)
            return False

    def imprimir(self):
        for fila in self.caras:
            for cara in fila:
                print(cara.get_color(), end="")
            print()

    def get_caras(self):
        return self.caras
    
    def esta_armada(self):
        color = self.caras[1][1].get_color()
        for i in range(0, 3):
            for j in range(0, 3):
                if self.caras[i][j].get_color() != color:
                    return False
        return True
    
    def piezas_desordenadas(self):
        color = self.caras[1][1].get_color()
        cantidad = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.caras[i][j].get_color() != color:
                    cantidad+=1
        return cantidad

class Cubo:
    def __init__(self, c1, c2, c3, c4, c5, c6):
        self.capas = {"F":c1, "L":c2, "U":c3, "R":c4, "D":c5, "B":c6}

    def __eq__(self, other):
        if isinstance(other, Cubo):
            for letra in ["F", "L", "U", "R", "D", "B"]:
                if self.capas[letra] != other.capas[letra]:
                    return False
            return True
        return False
    
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

    def esta_armado(self):
        for clave, valor in self.capas.items():
            if self.capas[clave].esta_armada() != True:
                return False
        return True
    
    def copiar(self):
        return copy.deepcopy(self)
    
    def heuristica(self):
        cantidad = 0
        for clave, valor in self.capas.items():
            cantidad += self.capas[clave].piezas_desordenadas() 
        return cantidad


    
class Lector_txt():
    def __init__(self) -> None:
        pass

    def cargar_txt(self, archivo):
        contadores = {'G': 0, 'O': 0, 'W': 0, 'R': 0, 'Y': 0, 'B': 0}
        with open(archivo, "r") as file:
            lineas = file.readlines()

        capas_leidas = []

        for linea in lineas:
            letras = list(linea.strip())
            if len(letras)!=9:
                print("Error: Se esperaban 9 elementos en cada fila")
                return
            capa = Capa(*letras)
            capas_leidas.append(capa)
            for letra in letras:
                contadores[letra] += 1

        for letra, cantidad in contadores.items():
            if cantidad != 9:
                print("Error: Se esperaban 9 elementos de la letra", letra, "en el archivo.")
                return None

        if len(capas_leidas) != 6:
            print("Error: Se esperaban 6 capas en el archivo.")
            return None
        
        return capas_leidas
    
    def guardar_txt(self, cubo, archivo_salida):
        with open(archivo_salida, "w") as file:
            for letra in ["F", "L", "U", "R", "D", "B"]:
                capa = cubo.capas[letra]
                for fila in capa.caras:
                    for cara in fila:
                        file.write(cara.get_color())
                file.write("\n")
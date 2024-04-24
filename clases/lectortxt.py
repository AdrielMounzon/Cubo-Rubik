from clases.cubo import Capa

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

    def cargar_comandos(self, archivo):
        with open(archivo, "r") as file:
            comandos = file.readline().strip().split(', ')
        return comandos
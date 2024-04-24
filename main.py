from clases.cubo import Cubo
from clases.solucionador import Solucionador
from clases.lectortxt import Lector_txt

if __name__ == "__main__":
    lector = Lector_txt()
    capas = lector.cargar_txt("textos/desarmado.txt")
    cubo = Cubo(*capas)
    
    movimientos = Solucionador.resolver_cubo(cubo)

    if movimientos:
        movimientos_modificados = []
        i = 0
        while i < len(movimientos):
            current = movimientos[i]
            count = 1
            j = i + 1
            while j < len(movimientos) and movimientos[j] == current:
                count += 1
                j += 1
            if count > 1:
                movimientos_modificados.append(current[0]+"2")
                i += 2
            else:
                movimientos_modificados.append(current)
                i += 1

        print("Movimientos necesarios para resolver el cubo:", movimientos_modificados)
    else:
        print("No se encontró solución para el cubo.")

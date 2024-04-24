from cubo import Cubo, Lector_txt
import heapq

class Nodo:
    def __init__(self, cubo, movimientos, costo):
        self.cubo = cubo
        self.movimientos = movimientos
        self.costo = costo
    
    def __lt__(self, other):
        return self.costo < other.costo

def resolver_cubo(cubo):
    frontera = []
    visitados = set()
    movimientos = []
    heapq.heappush(frontera, Nodo(cubo.copiar(), movimientos, cubo.get_heuristica()))

    while frontera:
        nodo_actual = heapq.heappop(frontera)

        if nodo_actual.cubo.esta_armado():
            return nodo_actual.movimientos

        visitados.add(hash(nodo_actual.cubo))

        for movimiento in [Cubo.U, Cubo.Up, Cubo.D, Cubo.Dp, Cubo.L, Cubo.Lp, Cubo.R, Cubo.Rp, Cubo.F, Cubo.Fp, Cubo.B, Cubo.Bp]:
            nuevo_cubo = nodo_actual.cubo.copiar()
            movimiento(nuevo_cubo)

            if hash(nuevo_cubo) not in visitados:
                nuevo_movimientos = nodo_actual.movimientos + [movimiento.__name__]
                heapq.heappush(frontera, Nodo(nuevo_cubo, nuevo_movimientos, len(nuevo_movimientos) + nuevo_cubo.get_heuristica()))

    return None

if __name__ == "__main__":
    lector = Lector_txt()
    capas = lector.cargar_txt("desarmado.txt")
    cubo = Cubo(*capas)
    
    movimientos = resolver_cubo(cubo)

    if movimientos:
        print("Movimientos necesarios para resolver el cubo:", movimientos)
    else:
        print("No se encontró solución para el cubo.")

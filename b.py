from frontiers import Queue
from cubo import Cubo, Lector_txt

class StatesSpace:
    def __init__(self):
        self.space = []

    def add_state(self, value):
        self.space.append(value)

    def __contains__(self, value):
        return value in self.space

    def reset(self):
        self.space = []


class Searcher:
    def __init__(self, space, debug=False):
        self.space = space
        self.debug = debug

    def breadth_first(self, initial_cubo):
        frontier = Queue()
        frontier.put((initial_cubo, []))  # Cambio: Tupla que contiene el cubo y la lista de movimientos
        while not frontier.empty():
            current_cubo, movimientos = frontier.get()  # Cambio: Desempaquetar el cubo y los movimientos
            if current_cubo.esta_armado():
                return movimientos  # Cambio: Devolver la lista de movimientos
            for movimiento in ["U", "Up", "D", "Dp", "L", "Lp", "R", "Rp", "F", "Fp", "B", "Bp"]:
                nuevo_cubo = current_cubo.copiar()  
                getattr(nuevo_cubo, movimiento)()  
                if nuevo_cubo not in self.space:
                    frontier.put((nuevo_cubo, movimientos + [movimiento]))  # Cambio: Agregar el movimiento a la lista
                    self.space.add_state(nuevo_cubo)
        return []  # No se encontró solución
    

if __name__ == "__main__":
    lector = Lector_txt()
    capas_desarmado = lector.cargar_txt("desarmado.txt")
    if capas_desarmado:
        cubo_desarmado = Cubo(*capas_desarmado)

    space = StatesSpace()
    space.add_state(cubo_desarmado)  

    searcher = Searcher(space)

    initial_cubo = cubo_desarmado
    print("Buscando solución...")
    solucion = searcher.breadth_first(initial_cubo)
    if solucion:
        print("¡Solución encontrada!")
        print("Movimientos aplicados:", solucion)
    else:
        print("No se encontró solución.")
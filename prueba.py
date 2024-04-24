from frontiers import PrioritizedQueue
from cubo import Cubo, Lector_txt

class State:
    def __init__(self, value):
        self.value = value
        self.actions = []
        self.visited = False
        self.parent = None
        self.cost = None

    def add_action(self, action):
        if not action in self.actions:
            self.actions.append(action)

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def was_visited(self):
        return self.visited

    def was_reached(self):
        return self.cost is not None or self.parent is not None
    
    def set_parent(self, value):
        self.parent = value

    def set_cost(self, cost):
        self.cost = cost

    # def __lt__(self, other):
    #     return self.value < other.value

    def __str__(self):
        return f"{self.value} -> {self.actions}"

class StatesSpace:
    def __init__(self):
        self.space = {}

    def add_state(self, value):   #Ojo con que los cubos son distintas variables
        esta = False
        for state in self.space.keys():
            if value==state:
                esta=True
                break
        if not esta:
            self.space[value] = State(value)

    def add_action(self, value1, value2):
        self.space[value1].add_action(value2)

    def get_state(self, value):
        if type(value) == tuple:
            return self.space[value[0]]
        else:
            return self.space[value]

    def reset(self):
        self.reset_visited()
        self.reset_costs()

    def reset_costs(self):
        for state in self.space.values():
            state.set_cost(None)

    def reset_visited(self):
        for state in self.space.values():
            state.mark_unvisited()

    def __str__(self):
        return "\n".join(str(state) for state in self.space.values())



class Searcher:
    def __init__(self, space, debug=False):
        self.space = space
        self.debug = debug
    
    def uniform_cost(self, intial_value):
        return self.weighted_search(intial_value, frontier=PrioritizedQueue())
    
    def expand(self, cube):
        movements = ["U", "Up", "D", "Dp", "L", "Lp", "R", "Rp", "F", "Fp", "B", "Bp"]
        # if last_move != "":
        #     if "p" in last_move:
        #         index_to_remove = movements.index(last_move) - 1
        #     else:
        #         index_to_remove = movements.index(last_move) + 1    
        #     del movements[index_to_remove]

        expansions = []
        for movement in movements:
                new_cube = cube.copiar()  
                getattr(new_cube, movement)()
                heuristic = new_cube.get_heuristica()
                expansions.append((new_cube, heuristic))
        # print("Expansiones: ", expansions)
        return expansions

        # if value=="A":
        #     return [('B', 4), ('C', 5)]
        # elif value == "B":
        #     return [('A', 4), ('C', 11), ('D', 9), ('E', 7)]
        # elif value == "C":
        #     return [('A', 5), ('B', 11), ('E', 3)]
        # elif value == "D":
        #     return [('B', 9), ('E', 13), ('F', 2)]
        # elif value == "E":
        #     return [('B', 7), ('C', 3), ('D', 13), ('F', 6)]
        # elif value == "F":
        #     return [('D', 2), ('E', 6)]

    def weighted_search(self, intial_value, frontier):      #REVISAR BIEN SI LA ACCION SERA LA LETRA O EL CUBO EJECUTADO, SE DEBERIA MANEJAR CUBO Y DEVOLVER SOLUCION CON POSICIONES EN LISTA
        initial_state = self.space.get_state(intial_value)
        initial_state.set_cost(0)
        frontier.put((initial_state, 0))

        while not frontier.empty():
            current_state, current_cost = frontier.get()
            current_state.mark_visited()
            if self.debug: print(current_state.value, current_cost)
            
            if current_state.value.esta_armado():
                if self.debug: print("Goal found")
                return self.build_solution_path(current_state), current_cost
            
            options = self.expand(current_state.value)
            for option in options:
                self.space.add_action(current_state.value, option)
                self.space.add_state(option[0])
            # print(self.space.space[current_state.value])

            # print(self.space)
            for action in current_state.actions:
                # print(action)
                # new_cube = current_state.value.copiar()  
                # getattr(new_cube, action[0])()
                # self.space.add_state(action)
                next_state = self.space.get_state(action)
                action_cost = current_cost + action[1]


                if self.debug:
                    print("Nodo", next_state.value, "Visitado: ", next_state.was_reached(), "Action cost:", action_cost, "Next state cost:", next_state.cost)
                if not next_state.was_reached() or action_cost < next_state.cost:
                    if self.debug: print("Entra")
                    next_state.set_parent(current_state)
                    next_state.set_cost(action_cost)
                    if self.debug:print("Expanding:", next_state.value, action_cost)
                    print()
                    frontier.put((next_state, action_cost))
        return []

    def build_solution_path(self, state):
        path = []
        while state:
            path.append(state.value)
            state = state.parent
        return list(reversed(path))




if __name__ == "__main__":
    debugging = True
    space = StatesSpace()

    searcher = Searcher(space, debug=debugging)

    lector = Lector_txt()
    capas_desarmado = lector.cargar_txt("desarmado.txt")
    if capas_desarmado:
        cubo_desarmado = Cubo(*capas_desarmado)

    initial_value = cubo_desarmado
    space.add_state(initial_value)
    print("Buscando camino de", initial_value, "a", "\n")


    print("Buscar en costo uniforme")
    path, cost = searcher.uniform_cost(initial_value)
    print(path, "costo:", cost)

from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar,
    greedy,
)
from simpleai.search.viewers import WebViewer, BaseViewer


def jugar(paredes, cajas, objetivos, jugador, maximos_movimientos):

    
    
    # coordenadas paredes
    PAREDES = paredes

    # coordenada global objetivos
    OBJETIVOS = objetivos

    # listado de acciones disponibles
    ACTIONS = (
    'arriba',
    'abajo',
    'izquierda',
    'derecha',
    )

    def manhattan(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x2 - x1) + abs(y2 - y1)

    def list_to_tuple(listas):
        return tuple([tuple(x) for x in listas])

    def tuple_to_list(tuplas):
        return [list(x) for x in tuplas]

    def neighbor_finder(coordinate, action):
        for cordenada in PAREDES:
            if coordinate==cordenada:
                return None
            
        
        coordinate_x, coordinate_y = coordinate
        neighbors = []

        right = (coordinate_x + 1, coordinate_y)
        left = (coordinate_x - 1, coordinate_y)
        up = (coordinate_x, coordinate_y + 1)
        down = (coordinate_x, coordinate_y - 1)
        
        if right not in PAREDES and action == "derecha":
            return right
        if left not in PAREDES and action == "izquierda":
            return left
        if up not in PAREDES and action == "arriba":
            return up
        if down not in PAREDES and action == "abajo":
            return down
    # (listado coordenadas cajas, listado coordenadas objetivos, posicion jugador, cantidad de movimientos máximos)
    INITIAL = (list_to_tuple(cajas), list_to_tuple(objetivos), jugador, maximos_movimientos)
    class SokobanProblem(SearchProblem):
        def cost(self, state1, action, state2):
            return 1

        def is_goal(self, state):
            cajas, objetivos, jugador, maximos_movimientos = state
            return len(objetivos) == 0 and maximos_movimientos >= 0

        def actions(self, state):
            acciones_disponibles = []
            cajas, objetivos, jugador, maximos_movimientos = state

            if maximos_movimientos < 0:
                return acciones_disponibles

            for action in ACTIONS:
                # Buscar celda adyacente. Celda adyacente es la nueva posicion del jugador.
                celda_adyacente = neighbor_finder(jugador, action)
                if celda_adyacente != None:
                    # Si hay una caja en la nueva posicion del jugador, hay que ver que no haya otra caja pegada.
                    if celda_adyacente in cajas:
                        # Buscar la adyacente de la nueva posicion del jugador, esta celda 2 nos va a ayudar a ver si habia 2 cajas seguidas.
                        celda_adyacente_2 = neighbor_finder(celda_adyacente, action)

                        if not celda_adyacente_2 in cajas:
                            acciones_disponibles.append(action)
                    else: # este else es cuando se mueve jugador sin generar movimiento de caja.
                        acciones_disponibles.append(action)

            return acciones_disponibles

        def result(self, state, action):
            cajas, objetivos, jugador, maximos_movimientos = state

            nueva_posicion_jugador = neighbor_finder(jugador, action)
            cajas_nuevas = []
            objetivos_nuevos = []
            
            if nueva_posicion_jugador in cajas:
                nueva_posicion_caja = neighbor_finder(nueva_posicion_jugador, action)

                for caja in cajas:
                    # Cuando el jugador se desplaza a una celda donde actualmente hay una caja.
                    if nueva_posicion_jugador == caja:
                        cajas_nuevas.append(nueva_posicion_caja)

                        # Si la nueva posicion esta en un objetivo, lo eliminamos de la lista de objetivos.
                        if nueva_posicion_caja in OBJETIVOS:
                            for objetivos_n in objetivos:
                                if objetivos_n != nueva_posicion_caja:
                                 objetivos_nuevos.append(objetivos_n)

                        # Si la vieja posicion estaba en un objetivo, lo agregamos de la lista de objetivos.
                        if caja in OBJETIVOS:
                            for objetivos_n in OBJETIVOS:
                                if objetivos_n == caja:
                                 objetivos_nuevos.append(caja)
                                 objetivos_nuevos = objetivos_nuevos + objetivos

                    else: # Agregamos la caja que no fue modificada.
                        cajas_nuevas.append(caja)

            maximos_movimientos -= 1
            
            return list_to_tuple(cajas_nuevas), list_to_tuple(objetivos_nuevos), nueva_posicion_jugador, maximos_movimientos 


        def heuristic(self, state):
            cajas, objetivos, jugador, maximos_movimientos = state
            return len(objetivos)
    
    problema = SokobanProblem(INITIAL)
    solucion = astar(problema)

    Result = []
    solucion = list_to_tuple(solucion)
    for accion in solucion.path():
        if accion[0] is not None:
            accion = tuple_to_list(accion)
            Result.append(accion)

    return Result
    # if __name__ == "__main__":
    #     viewer = BaseViewer()
    #     #result = depth_first(MisionerosProblem(INICIAL), graph_search=True, viewer=viewer)
    #     #result = breadth_first(MisionerosProblem(INICIAL), graph_search=True, viewer=viewer)
    #     result = astar(SokobanProblem(INITIAL))
    #     solution = []
    #     for action, state in result.path():
    #         if (action is not None):
    #             solution.append(action)

    # return solution

# paredes=[
#     (0, 0),
#     (0, 1),
#     (0, 2),
#     (0, 3),
#     (0, 4),
#     (0, 5),
#     (1, 0),
#     (1, 5),
#     (2, 0),
#     (2, 5),
#     (3, 0),
#     (3, 5),
#     (4, 0),
#     (4, 5),
    
#     (4, 1),
#     (4, 2),
#     (4, 3),
#     (4, 4),

# ]

# cajas=[
    
#     (2, 3)
    
# ]

# objetivos=[
    
#     (1, 3)

# ]

# jugador=(3, 3)
# maximos_movimientos=100
# result = jugar(paredes,cajas,objetivos,jugador,maximos_movimientos)
# print(result)
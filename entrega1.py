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

    # (listado coordenadas cajas, listado coordenadas objetivos, posicion jugador, cantidad de movimientos máximos)
    INITIAL = (cajas, objetivos, jugador, maximos_movimientos)
    
    # coordenadas paredes
    PAREDES = paredes

    # listado de acciones disponibles
    ACTIONS = (
    'arriba',
    'abajo',
    'izquierda',
    'derecha',
    )   

    class SokobanProblem(SearchProblem):
        def cost(self, state1, action, state2):
            return 1

        def is_goal(self, state):
            cajas, objetivos, jugador, maximos_movimientos = state
            return len(objetivos) == 0 and maximos_movimientos >= 0

        def actions(self, state):
            acciones_disponibles = []

            if maximos_movimientos > 0:
                for action in ACTIONS:
                    cajas, objetivos, jugador, maximos_movimientos = self.result(state, action)

                    for pared in PAREDES:
                    if pared 

            return acciones_disponibles

        def result(self, state, action):
            cajas, objetivos, jugador, maximos_movimientos = state
            jugador_x, jugador_y = jugador
            
            if action == 'arriba':
                jugador_y += 1

            if action == 'abajo':
                jugador_y -= 1
            
            if action == 'derecha':
                jugador_x += 1
            
            if action == 'izquierda':
                jugador_x -= 1

            nueva_posicion_jugador = tuple(jugador_x, jugador_y)
            
            for caja in cajas:
                if caja == nueva_posicion_jugador:
                    caja_x, caja_y = caja

                    if action == 'arriba':
                        caja_y += 1

                    if action == 'abajo':
                        caja_y -= 1
                    
                    if action == 'derecha':
                        caja_x += 1
                    
                    if action == 'izquierda':
                        caja_x -= 1
                    
                    nueva_posicion_caja = (caja_x, caja_y)

                    #CREAR LISTA NUEVA PARA IR AGREGANDO LAS CAJAS 
                    cajas.remove(caja)
                    cajas.add(caja)

            maximos_movimientos = maximos_movimientos -1

            return cajas, objetivos, nueva_posicion_jugador, maximos_movimientos

        def heuristic(self, state):
            pass


if __name__ == "__main__":
    viewer = BaseViewer()
    #result = depth_first(MisionerosProblem(INICIAL), graph_search=True, viewer=viewer)
    #result = breadth_first(MisionerosProblem(INICIAL), graph_search=True, viewer=viewer)
    #result = astar(SokobanProblem(jugar([()])), viewer=viewer)

    for action, state in result.path():
        print("Haciendo", action, "llegué a:")
        print(state)

    print("Profundidad:", len(list(result.path())))
    print("Stats:")
    print(viewer.stats)

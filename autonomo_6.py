#Nombre: Marcus Alexander Mayorga Martínez
#Fecha: 25/06/2025

import collections
import heapq

class Grafo:
    def __init__(self):
        #Diccionario que almacena la lista de adyacencia:
        #cada nodo apunta a una lista de nodos vecinos
        self.adyacencia = collections.defaultdict(list)
        #Conjunto que almacena todos los nodos del grafo
        self.nodos = set()

    def agregar_nodo(self, valor_nodo):
        #Agrega un nodo al conjunto de nodos
        self.nodos.add(valor_nodo)

    def agregar_aristas(self, nodo_origen, nodo_destino, dirigido=True):
        #Si los nodos no existen, se agregan al grafo
        if nodo_origen not in self.nodos:
            self.agregar_nodo(nodo_origen)
        if nodo_destino not in self.nodos:
            self.agregar_nodo(nodo_destino)

        #Se agrega la arista desde nodo_origen a nodo_destino
        self.adyacencia[nodo_origen].append(nodo_destino)

        #Si el grafo no es dirigido, también se agrega la arista inversa
        if not dirigido:
            self.adyacencia[nodo_destino].append(nodo_origen)

    def bfs(self, nodo_inicio):
        #Recorrido en anchura (BFS)
        visitados = set() #Para evitar visitar nodos repetidos
        cola = collections.deque([nodo_inicio]) #Cola para gestionar el orden de visita
        resultado = [] #Lista para almacenar el orden de recorrido

        #Validar que el nodo de inicio exista en el grafo
        if nodo_inicio not in self.nodos:
            return f"El nodo {nodo_inicio} no existe en el grafo."

        visitados.add(nodo_inicio)

        while cola:
            nodo_actual = cola.popleft() #Sacar el nodo más antiguo en la cola
            resultado.append(nodo_actual)

            #Agregar a la cola los vecinos no visitados
            for vecino in self.adyacencia[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return resultado

    def dfs(self, nodo_inicio):
        #Recorrido en profundidad (DFS)
        visitados = set()
        resultado = []

        #Validar nodo de inicio
        if nodo_inicio not in self.nodos:
            return f"El nodo {nodo_inicio} no existe en el grafo."

        def dfs_recursivo(nodo):
            #Marca el nodo actual como visitado y lo agrega al resultado
            visitados.add(nodo)
            resultado.append(nodo)

            #Recorre todos los vecinos no visitados recursivamente
            for vecino in self.adyacencia[nodo]:
                if vecino not in visitados:
                    dfs_recursivo(vecino)

        #Iniciar DFS desde el nodo de inicio
        dfs_recursivo(nodo_inicio)
        return resultado

    def detectar_ciclo(self):
        #Detecta ciclos en un grafo dirigido usando DFS
        visitados = set() #Nodos visitados completamente
        recursion_pila = set() #Nodos en la pila de recursión actual

        def _detectar_ciclo_util(nodo):
            #Marca el nodo actual como visitado y lo añade a la pila de recursión
            visitados.add(nodo)
            recursion_pila.add(nodo)

            #Recorre vecinos
            for vecino in self.adyacencia[nodo]:
                if vecino not in visitados:
                    if _detectar_ciclo_util(vecino): #Si se detecta ciclo en recursión, retorna True
                        return True
                elif vecino in recursion_pila: #Ciclo detectado
                    return True

            #Quita el nodo de la pila antes de volver
            recursion_pila.remove(nodo)
            return False

        #Ejecuta DFS para cada nodo no visitado
        for nodo in self.nodos:
            if nodo not in visitados:
                if _detectar_ciclo_util(nodo):
                    return True #Ciclo encontrado
        return False #No se encontraron ciclos

    def dijkstra(self, nodo_inicio):
        #Algoritmo de Dijkstra para caminos mínimos (suponiendo peso 1 en aristas)
        if nodo_inicio not in self.nodos:
            return f"El nodo {nodo_inicio} no existe en el grafo."

        #Inicializa todas las distancias con infinito, excepto el nodo inicial
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[nodo_inicio] = 0

        #Cola de prioridad para procesar nodos con la menor distancia primero
        cola_prioridad = [(0, nodo_inicio)]

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            #Ignora si ya hay un camino más corto registrado
            if distancia_actual > distancias[nodo_actual]:
                continue

            #Actualiza las distancias de los vecinos
            for vecino in self.adyacencia[nodo_actual]:
                distancia = distancia_actual + 1
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        return distancias


if __name__ == "__main__":
    g = Grafo()
    g.agregar_aristas("A", "B")
    g.agregar_aristas("A", "C")
    g.agregar_aristas("B", "C")
    g.agregar_aristas("B", "D")
    g.agregar_aristas("C", "D")
    g.agregar_aristas("D", "E")
    g.agregar_aristas("E", "F")

    #Detección de ciclos
    g_ciclo = Grafo()
    g_ciclo.agregar_aristas("A", "B")
    g_ciclo.agregar_aristas("B", "C")
    g_ciclo.agregar_aristas("C", "A")  # Ciclo
    g_ciclo.agregar_aristas("C", "D")

    #Imprimir resultados
    print("Inserción de nodos y aristas:")
    print("Nodos del grafo:", sorted(list(g.nodos)))
    print("Lista de adyacencia:", dict(g.adyacencia))

    print("Recorrido BFS desde A:", g.bfs("A"))
    print("Recorrido DFS desde A:", g.dfs("A"))

    print("Detección de ciclos:")
    print("El grafo 'g' tiene ciclos:", g.detectar_ciclo())
    print("El grafo 'g_ciclo' tiene ciclos:", g_ciclo.detectar_ciclo())

    print("Camino más corto desde A con Dijkstra:")
    distancias = g.dijkstra("A")
    for nodo, dist in distancias.items():
        print(f"Distancia desde A a {nodo}: {dist}")
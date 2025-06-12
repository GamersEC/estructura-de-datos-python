#Nombre: Marcus Alexander Mayorga Martínez
#Fecha: 15 de junio del 2025
#------------------------------------------


#Clase nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


#Clase para el árbol binario de búsqueda
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None


    #Funcion para insertar un valor en el árbol
    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    #Funcion recursiva para insertar un valor
    def _insertar_rec(self, nodo, valor):
        if nodo is None:
            return Nodo(valor) #Se crea un nuevo nodo si el nodo actual es None
        if valor < nodo.valor:
            nodo.izq = self._insertar_rec(nodo.izq, valor) #Si el valor es menor, se inserta en el subárbol izquierdo
        elif valor > nodo.valor:
            nodo.der = self._insertar_rec(nodo.der, valor) #Si el valor es mayor, se inserta en el subárbol derecho
        return nodo


    #Funcion para buscar un valor en el árbol
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)

    #Funcion recursiva para buscar un valor
    def _buscar_rec(self, nodo, valor):
        if nodo is None or nodo.valor == valor: #Si el nodo es None o el valor es igual al valor del nodo, se retorna el nodo
            return nodo
        if valor < nodo.valor:
            return self._buscar_rec(nodo.izq, valor) #Si el valor es menor, se busca en el subárbol izquierdo
        return self._buscar_rec(nodo.der, valor) #Si el valor es mayor, se busca en el subárbol derecho


    #Recorrido del arbol en inorden
    def inorden(self):
        return self._recorrer_inorden(self.raiz)

    #Funcion recursiva para recorrer el árbol en inorden
    def _recorrer_inorden(self, nodo):
        if nodo is None:
            return []
        return self._recorrer_inorden(nodo.izq) + [nodo.valor] + self._recorrer_inorden(nodo.der)


    #Recorrido del arbol en preorden
    def preorden(self):
        return self._recorrer_preorden(self.raiz)

    #Funcion recursiva para recorrer el árbol en preorden
    def _recorrer_preorden(self, nodo):
        if nodo is None:
            return []
        return [nodo.valor] + self._recorrer_preorden(nodo.izq) + self._recorrer_preorden(nodo.der)


    #Recorrido del arbol en postorden
    def postorden(self):
        return self._recorrer_postorden(self.raiz)

    #Funcion recursiva para recorrer el árbol en postorden
    def _recorrer_postorden(self, nodo):
        if nodo is None:
            return []
        return self._recorrer_postorden(nodo.izq) + self._recorrer_postorden(nodo.der) + [nodo.valor]


    #Funcion para eliminar un valor del árbol
    def eliminar(self, valor):
        self.raiz = self._eliminar_rec(self.raiz, valor)

    #Funcion recursiva para eliminar un valor
    def _eliminar_rec(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izq = self._eliminar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_rec(nodo.der, valor)
        else:
            #Caso 1: Sin hijos
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            #Caso 2: Dos hijos
            sucesor = self._min_valor(nodo.der) #Encuentra el sucesor inorden
            nodo.valor = sucesor.valor #Reemplaza el valor del nodo a eliminar con el valor del sucesor
            nodo.der = self._eliminar_rec(nodo.der, sucesor.valor) #Elimina el sucesor inorden
        return nodo


    #Funcion para encontrar el nodo con el valor mínimo en un subárbol
    def _min_valor(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual


#Prueba
arbol = ArbolBinarioBusqueda()
for valor in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(valor)

print("Inorden:", arbol.inorden())
print("Preorden:", arbol.preorden())
print("Postorden:", arbol.postorden())
print("Buscar 60:", "Encontrado" if arbol.buscar(60) else "No encontrado")

arbol.eliminar(70)
print("Inorden después de eliminar 70:", arbol.inorden())
#BST
#Clase nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#Clase arbol binario de busqueda
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_recursivo(self.raiz, valor) # Cambiado aquí

    def insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self.insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self.insertar_recursivo(nodo_actual.derecha, valor)

    #Funcion buscar recursiva
    def buscar(self, valor):
        return self.buscar_recursivo(self.raiz, valor)

    def buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        elif valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self.buscar_recursivo(nodo_actual.izquierda, valor)
        else:
            return self.buscar_recursivo(nodo_actual.derecha, valor)

    #Funciona para mostrar
    def mostrar(self):
        self.mostrar_recursivo(self.raiz)

    def mostrar_recursivo(self, nodo):
        if nodo is not None:
            self.mostrar_recursivo(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.mostrar_recursivo(nodo.derecha)



    #Funciona eliminar recursiva
    def eliminar(self, valor):
        self.raiz = self.eliminar_recursivo(self.raiz, valor)

    def eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierda = self.eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self.eliminar_recursivo(nodo.derecha, valor)
        else:
            #Caso 1: sin hijos
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            #Caso 2: un hijo
            elif nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
        return nodo

    def encontrar_min(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo



arbol = ArbolBinario()
arbol.insertar(30)
arbol.insertar(20)
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(3)

print("Mostrar arbol en Inorden: ")
arbol.mostrar()

print("El elemento a buscar dentro del arbol es: 20", arbol.buscar(20))
print("El elemento a buscar dentro del arbol es: 6", arbol.buscar(6))

print("El elemento 10 ha sido eliminando del árbol")
arbol.eliminar(10)

#Imprimir el árbol después de eliminar el elemento
print("Árbol después de eliminar 10:")
arbol.mostrar()

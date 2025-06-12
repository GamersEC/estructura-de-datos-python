#Nombre: Marcus Alexander Mayorga Martínez
#Fecha: 02/06/2025

#Clase Nodo binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

#Recorrido del inorden: izquierda -> raiz -> derecha
def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izq) #Recorrer subárbol izquierdo
        print(nodo.valor, end=' ') #Mostrar el valor del nodo
        inorden(nodo.der)

#Posorden: izquierda -> derecha -> raiz
def posorden(nodo):
    if nodo is not None:
        posorden(nodo.izq) #Recorrer subárbol izquierdo
        posorden(nodo.der) #Recorrer subárbol derecho
        print(nodo.valor, end=' ') #Mostrar el valor del nodo


#Buscar dado un valor
def buscar(nodo, valor):
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    elif valor < nodo.valor:
        return buscar(nodo.izq, valor)
    else:
        return buscar(nodo.der, valor)


def buscar_min(nodo):
    actual = nodo
    while actual.izq is not None:
        actual = actual.izq
    return actual


# Eliminar
def eliminar(nodo, valor):
    if nodo is None:
        return nodo
    if valor < nodo.valor:  # Si el valor a eliminar es menor, buscar en el subárbol izquierdo
        nodo.izq = eliminar(nodo.izq, valor)
    elif valor > nodo.valor:  # Si el valor a eliminar es mayor, buscar en el subárbol derecho
        nodo.der = eliminar(nodo.der, valor)
    else:
        # Caso 1 arbol no tenga hijos
        if nodo.izq is None and nodo.der is None:
            return None

        # Caso 2 solo tenga un hijo
        elif nodo.izq is None:  #Si solo tiene hijo derecho
            return nodo.der
        elif nodo.der is None:  #Si solo tiene hijo izquierdo
            return nodo.izq

        # Caso 3 que tenga dos hijos
        temp = buscar_min(nodo.der)
        nodo.valor = temp.valor
        nodo.der = eliminar(nodo.der, temp.valor)
    return nodo  # Retornar el nodo actualizado


#Insertar
def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)
    if valor < nodo.valor:
        nodo.izq = insertar(nodo.izq, valor)
    else:
        nodo.der = insertar(nodo.der, valor)
    return nodo

#Crear el arbol
raiz = None
valores = [20, 10, 15, 8, 25, 7]
for n in valores:
    raiz = insertar(raiz, n)

#Mostrar
print("Recorrido inorden: ")
inorden(raiz)

#Buscar
print("\nBuscar el elemento 15: ", buscar(raiz, 15))  #Llamar a la función de búsqueda

#Eliminar
print("\nEliminar el elemento 10: ")
raiz = eliminar(raiz, 10)

#Mostrar el árbol después de eliminar
print("El arbol nuevo es: ")
posorden(raiz)

#Ingresar los elementos en el arbol
raiz = Nodo(15)
raiz.izq = Nodo(10)
raiz.der = Nodo(20)
raiz.der = Nodo(18)
raiz.izq.izq = Nodo(8)
raiz.der.der = Nodo(25)

#Mostrar arbol inorden
print(f"El recorido inorden del árbol es:")
inorden(raiz)  #Llamar a la función de recorrido inorden

#Mostrar arbol posorden
print(f"\nEl recorido posorden del árbol es:")
posorden(raiz)  #Llamar a la función de recorrido posorden
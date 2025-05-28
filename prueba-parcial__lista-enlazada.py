#-------------------------------------------
#Nombre: Marcus Alexander Mayorga Martínez
#Fecha: 27 de mayo del 2025
#-------------------------------------------



#Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato #Dato almacenado en el nodo
        self.siguiente = None #Puntero al siguiente nodo


#Clase lista enlazada simple
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None #Puntero al primer nodo de la lista


    #Inserta un nuevo nodo al inicio de la lista
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato) #Crea el nuevo nodo con el dato
        nuevo.siguiente = self.cabeza #Apunta al nodo actual de la cabeza
        self.cabeza = nuevo #Actualiza la cabeza para que apunte al nuevo nodo
        print(f"Insertado al inicio: {dato}")


    #Inserta un nuevo nodo al final de la lista
    def insertar_final(self, dato):
        nuevo = Nodo(dato) #Crear nuevo nodo con el dato
        if self.cabeza is None: #Si la lista está vacia
            self.cabeza = nuevo #El nuevo nodo sera la cabeza
        else:
            actual = self.cabeza

            #Recorre hasta llegar al ultimo nodo
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo #Enlazar el ultimo nodo con el nuevo nodo
        print(f"Insertado al final: {dato}")


    #Elimina el primer nodo que contiene el valor dado
    def eliminar(self, valor):
        if self.cabeza is None: #Si la lista está vacia
            print("La lista esta vacia.")
            return

        #Si el nodo a eliminar es el primero
        if self.cabeza.dato == valor:
            self.cabeza = self.cabeza.siguiente #Mover la cabeza al siguiente nodo
            print(f"Elemento eliminado: {valor}")
            return

        anterior = self.cabeza
        actual = self.cabeza.siguiente

        #Recorrer la lista buscando el nodo con el valor
        while actual:
            if actual.dato == valor:
                anterior.siguiente = actual.siguiente #Saltar el nodo actual
                print(f"Elemento eliminado: {valor}")
                return
            anterior = actual
            actual = actual.siguiente

        #Indicar que el valor no fue encontrado
        print(f"Elemento no encontrado: {valor}")


    #Busca un valor en la lista y devuelve su posicion
    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0

        #Recorre la lista buscando el valor
        while actual:
            if actual.dato == valor:
                print(f"Elemento '{valor}' encontrado en la posicion {posicion}.")
                return posicion
            actual = actual.siguiente
            posicion += 1
        print(f"Elemento '{valor}' no encontrado en la lista.")
        return -1  #Valor no encontrado


    #Muestra todos los elementos de la lista
    def mostrar(self):
        actual = self.cabeza
        if not actual:
            print("La lista esta vacia.")
            return
        print("Contenido de la lista:")
        while actual:
            print(actual.dato, end=" -> ")  #Imprimir dato acompañado de una flecha
            actual = actual.siguiente
        print("None")  #Fin de la lista


#Función que contiene un menu interactivo para manipular la lista enlazada
def menu_lista():
    lista = ListaEnlazada()  #Crear una instancia de ListaEnlazada

    while True:
        print("\nMenu de Lista Enlazada Simple")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Eliminar por valor")
        print("4. Buscar por valor")
        print("5. Mostrar lista")
        print("6. Salir")

        opcion = input("Seleccione una opcion (1-6): ")

        if opcion == '1':
            dato = input("Dato a insertar al inicio: ")
            lista.insertar_inicio(dato)

        elif opcion == '2':
            dato = input("Dato a insertar al final: ")
            lista.insertar_final(dato)

        elif opcion == '3':
            valor = input("Valor a eliminar: ")
            lista.eliminar(valor)

        elif opcion == '4':
            valor = input("Valor a buscar: ")
            lista.buscar(valor)

        elif opcion == '5':
            lista.mostrar()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida.")

#Punto de entrada del programa
if __name__ == "__main__":
    menu_lista()
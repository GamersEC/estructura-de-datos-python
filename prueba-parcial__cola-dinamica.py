#-------------------------------------------
#Nombre: Marcus Alexander Mayorga Martínez
#Fecha: 27 de mayo del 2025
#-------------------------------------------



#Creamos una excepción personalizada para manejar el caso de cola vacía
class ColaVaciaException(Exception):
    pass


#Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato #Valor almacenado en el nodo
        self.siguiente = None #Referencia al siguiente nodo


#Clase Cola
class Cola:
    def __init__(self):
        self.frente = None #Nodo al frente de la cola
        self.final = None #Nodo al final de la cola
        self._tamano = 0 #Contador del numero de elementos en la cola


    #Añade un nuevo elemento al final de la cola
    def enqueue(self, dato):
        nuevo = Nodo(dato) #Crea un nuevo nodo con el dato
        if self.is_empty(): #Si la cola esta vacia
            self.frente = self.final = nuevo #El nuevo nodo es el frente y final
        else:
            self.final.siguiente = nuevo #Enlaza el ultimo nodo al nuevo
            self.final = nuevo #Actualiza el final a nuevo nodo
        self._tamano += 1 #Incrementar el tamaño de la cola
        print(f"Elemento encolado: {dato}")


    #Remueve y desencola el elemento al frente de la cola
    def dequeue(self):
        if self.is_empty(): #Si la cola esta vacia, no se puede desencolar
            raise ColaVaciaException("La cola está vacia, no se puede desencolar.")
        valor = self.frente.dato #Guarda el dato del nodo frente
        self.frente = self.frente.siguiente #Avanzar el frente al siguiente nodo
        if self.frente is None: #Si la cola queda vacia, actualizar final
            self.final = None
        self._tamano -= 1 #Decrementa el tamaño de la cola
        return valor #Devolver el dato desencolado


    #Retorna el valor del frente sin eliminarlo
    def peek(self):
        if self.is_empty():
            raise ColaVaciaException("La cola está vacía, no hay frente.")
        return self.frente.dato


    #Verifica si la cola esta vacia
    def is_empty(self):
        return self.frente is None


    #Devuelve el tamaño actual de la cola
    def size(self):
        return self._tamano


    #Busca un valor en la cola y retorna su posicion
    def search(self, valor):
        actual = self.frente
        posicion = 0
        while actual:
            if actual.dato == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1


    #Imprime todos los elementos de la cola
    def mostrar(self):
        actual = self.frente
        if self.is_empty():
            print("La cola está vacía.")
        else:
            while actual:
                print(actual.dato, end=" -> ")
                actual = actual.siguiente
            print("None")


#Menu de opciones
def menu_cola():
    cola = Cola() #Creamos la instancia de cola

    while True:
        print("\nMenu de Cola Dinamica")
        print("1. Encolar (enqueue)")
        print("2. Desencolar (dequeue)")
        print("3. Ver frente (peek)")
        print("4. Verificar si esta vacia (is_empty)")
        print("5. Obtener tamaño (size)")
        print("6. Buscar elemento (search)")
        print("7. Mostrar cola (mostrar)")
        print("8. Salir")

        opcion = input("Seleccione una opcion (1-8): ").strip()

        if opcion == '1':
            dato_str = input("Ingrese el dato a encolar: ")

            #Condicional para convertir el dato ingresado a int, float o str
            for conv in (int, float, str):
                try:
                    dato = conv(dato_str)
                    break
                except ValueError:
                    continue
            cola.enqueue(dato)

        elif opcion == '2':
            try:
                valor = cola.dequeue()
                print(f"Elemento desencolado: {valor}")
            except ColaVaciaException as e:
                print("Error:", str(e))

        elif opcion == '3':
            try:
                print("Frente de la cola:", cola.peek())
            except ColaVaciaException as e:
                print("Error:", str(e))

        elif opcion == '4':
            print("La cola esta vacia." if cola.is_empty() else "La cola NO está vacia.")

        elif opcion == '5':
            print(f"Tamaño de la cola: {cola.size()}")

        elif opcion == '6':
            buscar = input("Valor a buscar: ")

            #Condicional para convertir el valor ingresado a int, float o str
            for conv in (int, float, str):
                try:
                    valor = conv(buscar)
                    break
                except ValueError:
                    continue
            pos = cola.search(valor)
            print(f"Elemento encontrado en posicion {pos}." if pos != -1 else "Elemento no encontrado.")

        elif opcion == '7':
            print("Contenido de la cola:")
            cola.mostrar()

        elif opcion == '8':
            print("Saliendo...")
            break

        else:
            print("Opcion inválida.")

#Punto de entrada del programa
if __name__ == "__main__":
    menu_cola()
# Cola con las 4 operaciones

#Clase Nodo:
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

#Clase Cola:
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    # proceso para verificar si la cola está vacía
    def vacia(self):
        return self.frente is None

    def encolar_agregar(self, valor):
        nuevo = Nodo(valor)
        if self.vacia():
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f"Elemento {valor} agregado a la cola.")

    #Utiliza la propiedad cola FIFO (primero en entrar, primero en salir)
    def desencolar_eliminar(self):
        if self.vacia():
            print("La cola está vacía. No se puede desencolar.")
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"El producto tecnologico {valor} ha sido eliminado/desencolado.")
        return valor

    #Identficamos cual es el frente
    def frente(self):
        if self.vacia():
            print("La cola está vacía.")
            return None
        return self.frente.valor


    def mostrar(self):
        if self.vacia():
            print("La cola está vacía.")
            return
        actual = self.frente
        print("Los productos tecnologicos son: ")
        while actual:
            print(f"El producto {actual.valor}")
            actual = actual.siguiente

    #Valor del producto a actualizar, dato nuevo para actualizar
    def actualizar_producto(self, v_actual, n_valor):
        if self.vacia():
            print("La cola está vacía.")
            return
        actual = self.frente
        flag= False
        while actual:
            if actual.valor == v_actual:
                actual.valor = n_valor
                print(f"Elemento actual: {actual.valor} - {n_valor}")
                flag= True
                break
            actual = actual.siguiente
        if not flag:
            print(f"Elemento no encontrado.")


cola = Cola()

cola.encolar_agregar("PC")
cola.encolar_agregar("Mouse")
cola.encolar_agregar("Teclado")
cola.encolar_agregar("Pantalla")

cola.mostrar()
cola.actualizar_producto("USB", "Mouse inalambrico")

cola.mostrar()

cola.desencolar_eliminar()

cola.mostrar()
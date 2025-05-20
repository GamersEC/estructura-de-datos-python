# Atecion de personas en un hospital simulando una cola de prioridad
# Prioridad va a hacer normal o urgente
# Insertar los nombres de personas con el tipo de tramite

class Nodo:
    def __init__(self, nombre, tipo_tramite):
        self.nombre = nombre
        self.tipo_tramite = tipo_tramite
        self.siguiente = None


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def vacia(self):
        return self.frente is None

    # Ingresar personas por el tipo de tramite
    def encolar_agregar(self, nombre, tipo_tramite):
        nuevo = Nodo(nombre, tipo_tramite)
        if self.vacia():
            self.frente = self.final = nuevo
        elif tipo_tramite == 'Urgente':
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:  # Si el tramite es normal
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f"La persona con el tramite {tipo_tramite} se agrego.")

    # Atencion segun el tipo de tramite


    def atender(self):
        if self.vacia():
            print("Cola vacía.")
            return
        print("Personas con trámite Urgente:")
        actual = self.frente
        while actual:
            if actual.tipo_tramite == 'Urgente':
                print(f"Nombre: {actual.nombre}, Tipo de trámite: {actual.tipo_tramite}")
            actual = actual.siguiente


cola = Cola()

cola.encolar_agregar("Lucia", "Urgente")
cola.encolar_agregar("Ana", "Urgente")
cola.encolar_agregar("Jose", "Normal")
cola.encolar_agregar("Raul", "Urgente")

cola.atender()

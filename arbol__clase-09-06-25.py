class Nodo:
    def __init__(self, pregunta, izq=None, der=None):
        self.pregunta = pregunta
        self.izq = izq
        self.der = der

#Respuestas de las hojas
nodo_producto_recomendar = Nodo("No hay productos para recomendación")
nodo_libro = Nodo("Recomiendo: libro ABC")
nodo_accesorio = Nodo("Recomiendo: accesorios tecnológicos")

#Nuevos nodos de recomendación para laptops
nodo_hp = Nodo("Recomiendo: HP Pavilion")
nodo_dell = Nodo("Recomiendo: Dell Inspiron")


#Nodo que pregunta por la marca de la laptop
pregunta_marca_laptop = Nodo("¿Prefieres una laptop de la marca Dell?", izq=nodo_hp, der=nodo_dell)


#Nodos intermedios
nodo_buscar_libro = Nodo("¿Buscas un libro?", izq=nodo_producto_recomendar, der=nodo_libro)
nodo_precio = Nodo("¿Precio es mayor a $300?", izq=nodo_accesorio, der=pregunta_marca_laptop)


#Nodo raíz
raiz = Nodo("¿Busca un producto tecnológico?", izq=nodo_buscar_libro, der=nodo_precio)

#Función para recorrer el árbol
def recorrer_arbol(nodo):
    #Pregunta
    if nodo.izq is None and nodo.der is None:
        print(f"\n{nodo.pregunta}")
        return

    respuesta = input(f"{nodo.pregunta} (si/no): ").strip().lower()
    if respuesta == "si":
        recorrer_arbol(nodo.der)
    elif respuesta == "no":
        recorrer_arbol(nodo.izq)
    else:
        print("Respuesta no válida, por favor ingrese 'si' o 'no'.")
        recorrer_arbol(nodo)

print("Árbol de recomendación de productos")
recorrer_arbol(raiz)
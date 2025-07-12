#Nombre: Marcus Mayorga

#Funcion de búsqueda binaria
def busqueda_binaria(lista, elemento_a_buscar):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:

        #Calculamos el punto medio para dividir la lista
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == elemento_a_buscar:
            return medio
        elif valor_medio < elemento_a_buscar:

           #El elemento a buscar está en la mitad derecha
            izquierda = medio + 1
        else:

            #El elemento a buscar está en la mitad izquierda
            derecha = medio - 1

    #Termina en -1 si no se encuentra el elemento
    return -1



#Prueba de busqueda binaria
lista_apellidos = ["Alvarez", "Andrade", "Bravo", "Castro", "Díaz", "Espinoza", "Gómez", "Martínez", "Paredes", "Ramírez"]
elemento = 'Gonzales'
indice_1 = busqueda_binaria(lista_apellidos, elemento)

if indice_1 != -1:
    print(f"\nLista: {lista_apellidos}")
    print(f"El elemento {elemento} se encontró en la posición: {indice_1}")
else:
    print(f"\nLista: {lista_apellidos}")
    print(f"El elemento {elemento} no se encontró en la lista.")
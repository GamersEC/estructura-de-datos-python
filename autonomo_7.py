#Actividad 2: Implementación y análisis
def busqueda_secuencial(lista_desordenada, valor):
    pasos = 0
    for i, elemento in enumerate(lista_desordenada):
        pasos += 1
        if elemento == valor:
            return i, pasos
    return -1, pasos

def busqueda_binaria(lista_ordenada, valor):
    izquierda, derecha = 0, len(lista_ordenada) - 1
    pasos = 0
    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio] == valor:
            return medio, pasos
        elif lista_ordenada[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, pasos

def busqueda_en_matriz(matriz, valor):
    pasos = 0
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            pasos += 1
            if elemento == valor:
                return (i, j), pasos
    return -1, pasos



#Prueba de las funciones
lista_desordenada = [42, 13, 5, 77, 24]
lista_ordenada = [5, 13, 24, 42, 77]
matriz = [
    [1, 4, 6],
    [10, 14, 18],
    [20, 25, 30]
]
valor_a_buscar = 14

pos, pasos = busqueda_secuencial(lista_desordenada, 5)
print(f"Búsqueda Secuencial (buscando 5): Posición {pos}, Pasos: {pasos}")

pos, pasos = busqueda_binaria(lista_ordenada, 77)
print(f"Búsqueda Binaria (buscando 77): Posición {pos}, Pasos: {pasos}")

print("\nBuscando el valor 14")
pos_matriz, pasos_matriz = busqueda_en_matriz(matriz, valor_a_buscar)
print(f"Búsqueda en Matriz 2D (buscando 14): Posición {pos_matriz}, Pasos: {pasos_matriz}")
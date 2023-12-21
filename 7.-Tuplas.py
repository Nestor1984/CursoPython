"""
Tupla: es una estructura de datos propia de Python que permite almacenar
distintos valores, son inmutables: no cambian una vez inicializadas
"""

tupla = (1, 2, 3) # Definicion de una tupla 1
print(tupla)

tupla2 = (7, "Nestor", True, 450.1, 16 + 7j) # Definicion de una tupla 2
print(tupla2)

tupla3 = (9, 3, (4, 5, 6)) # Definicion de una tupla dentro de otra tupla
print(tupla3)

# Nota: En tuplas se trabaja con posiciones que inician desde la posicion 0, igual que en arreglos
print(tupla2[1])

# Ejemplos con metodos
print(tupla2.count(7)) # .count(): Este metodo cuenta cuantas veces contiene la tupla el dato que le pases como argumento.
print(tupla3.index(3)) # .index(): Este metodo te dice la posicion en la que se encuentra el dato que le pases como argumento.
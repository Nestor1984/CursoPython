
texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2

#Primera forma
print(textoFinal)

#Segunda forma - usando comodines
print("El saludo es: %s %s " % (texto1, texto2))

#Tercera forma - usando comodines con posiciones
saludoFinal = "Saludo: {0} {1}".format(texto1, texto2) #.format(0, 1)
print(saludoFinal)

#Cuarta forma - usando seudonimos o alias
saludoFinal2 = "Saludo: {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal2)
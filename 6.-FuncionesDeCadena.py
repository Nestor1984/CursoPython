
texto = "Bienvenidos a todo el mundo"

print(texto)
print(texto.lower()) #Metodo para convetir minusculas
print(texto.upper()) #Metodo para convetir mayusculas
print(texto.title()) #Metodo para convetir primer caracter de cada palabra a mayusculas
print(texto.count("a")) #Metodo para saber cuantas veces encuentra la coincidencia

textoFinal = texto.replace("a", "3") #Metodo para reemplazar texto
print(textoFinal)

cadenaSeparada = texto.split(" ") #Metodo para devolver un arreglo, en este caso separado por espacios
print(cadenaSeparada)

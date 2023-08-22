# demuestra funcion map() en python
# 22-08-2023

# definimos una funcion para calcular cuadrados
def cuadrados (n):
    return n ** 2

## inicializamos una lista de numeros
numeros = [1,2,3,4,5]
print(f"La lista numeros inicial es: {numeros}")

#Calculamos los cuadrados y almacenamos en una lista denomidada cuadrados
cuadrados = map(cuadrados, numeros)
# imprimomso la listra cuadrados con el cast o palabra reservada de python "list"

print(f"Los cuadrados usando map y la funcion cuadrados se presenta asi: {list(cuadrados)}")


# Procesamos a elevar al cuadraro cada numero de la lista usando map y la funcion lambda  por ejemplo;
# para ello usamos la variable x para calcular el valor al cuadrado tomando cada elemento
# de la lista numeros original
#
#

resultado = map(lambda x: x * x, numeros)

# imprimimos la nueva lista con los cuadrados, pero usando la instruccion (list) para ver
#los resultados.

print(f"Los cuadrados de la lista numeros usando map y lambda son, {list(resultado)}")

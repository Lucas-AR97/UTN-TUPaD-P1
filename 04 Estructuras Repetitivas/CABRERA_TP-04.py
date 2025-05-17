# 1) Números del 0 al 100

# Imprime los números del 0 al 100, uno por línea
for i in range(101):
    print(i)


# 2) Contar dígitos de un número

# Solicita un número entero
numero = input("Ingrese un número entero: ")

# Muestra la cantidad de dígitos usando la longitud del string
print("Cantidad de dígitos:", len(numero))


# 3) Suma entre dos valores (excluidos)

# Solicita los dos valores
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Ordena los valores si es necesario
inicio = min(a, b) + 1
fin = max(a, b)

# Suma los valores entre ellos, excluyendo los extremos
suma = 0
for i in range(inicio, fin):
    suma += i

print("Suma entre los números:", suma)


# 4) Sumar hasta ingresar 0

# Inicializa suma y variable de entrada
suma = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("Suma total:", suma)


# 5) Adivinar número aleatorio

import random

# Genera un número entre 0 y 9
secreto = random.randint(0, 9)
intentos = 0

# Bucle de adivinanza
while True:
    intento = int(input("Adivine el número (0 a 9): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto! Número adivinado en {intentos} intentos.")
        break


# 6) Pares del 100 al 0 (decreciente)

# # Imprime números pares desde 100 hasta 0
for i in range(100, -1, -2):
    print(i)


# 7) Sumar del 0 hasta un número dado

# Solicita número límite
n = int(input("Ingrese un número positivo: "))

# Calcula la suma desde 0 hasta n
suma = 0
for i in range(n + 1):
    suma += i

print("Suma total:", suma)


# 8) Clasificación de 100 números

# Inicialización de contadores
pares = impares = positivos = negativos = 0

# Cambiar 100 por otro valor para pruebas
for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

# Muestra los resultados
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")


# 9) Media de 100 números

# Inicialización
suma = 0

# Cambiar 100 por otro valor para pruebas
for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

# Calcula media
media = suma / 100
print("Media:", media)


# 10) Invertir dígitos de un número

# Solicita número al usuario
numero = input("Ingrese un número: ")

# Invierte la cadena con slicing
numero_invertido = numero[::-1]

print("Número invertido:", numero_invertido)

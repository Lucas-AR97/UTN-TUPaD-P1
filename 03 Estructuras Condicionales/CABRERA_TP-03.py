# 1) Edad y mayoría de edad

# Solicita al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Verifica si la edad es mayor a 18 y muestra el mensaje correspondiente
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# 2) Nota aprobada o desaprobada

# Solicita la nota del usuario
nota = int(input("Ingrese su nota: "))

# Verifica si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Verificación de número par

# Solicita un número al usuario
numero = int(input("Ingrese un número par: "))

# Usa el operador módulo (%) para verificar si es par
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) Clasificación por edad

# Solicita la edad del usuario
edad = int(input("Ingrese su edad: "))

# Clasifica según el rango etario
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# 5) Validación de longitud de contraseña

# Solicita una contraseña al usuario
contrasena = input("Ingrese una contraseña: ")

# Verifica que tenga entre 8 y 14 caracteres
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) Análisis estadístico con bias

from statistics import mode, median, mean
import random

# Crea una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula moda, mediana y media
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Compara valores para detectar sesgo
if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")


# 7) Añadir signo de exclamación si termina en vocal

# Solicita una palabra o frase
frase = input("Ingrese una frase o palabra: ")

# Verifica si termina con vocal
if frase[-1].lower() in "aeiou":
    frase += "!"
    
# Muestra el resultado
print(frase)


# 8) Transformar nombre según opción

# Solicita el nombre del usuario
nombre = input("Ingrese su nombre: ")

# Solicita una opción de formato
opcion = int(input("Ingrese 1 (mayúsculas), 2 (minúsculas), 3 (primera letra mayúscula): "))

# Aplica la transformación según la opción elegida
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")


# 9) Clasificación por magnitud de terremoto

# Solicita magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasifica según escala de Richter
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")


# 10) Determinar estación del año

# Solicita hemisferio, mes y día
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día: "))

# Convierte mes y día en una clave única para comparar
fecha = (mes, dia)

# Determina estación según la fecha y hemisferio
if (fecha >= (12, 21) or fecha <= (3, 20)):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (fecha >= (3, 21) and fecha <= (6, 20)):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (fecha >= (6, 21) and fecha <= (9, 20)):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (fecha >= (9, 21) and fecha <= (12, 20)):
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

# Muestra el resultado
print(f"Estación: {estacion}")

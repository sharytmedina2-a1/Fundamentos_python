# --- EJERCICIO 1: Creación de Variables ---
# Definición de variables con distintos tipos de datos (Nombre, Valor, Promedio)

nombre = "Sharyt"
valor_producto = 500000
promedio_asignatura = 4.5

print("Resultados Ejercicio 1:")
print(f"1. Nombre: {nombre}")
print(f"2. Precio del producto: ${valor_producto}")
print(f"3. Promedio: {promedio_asignatura}")

# --- EJERCICIO 2: Operadores con Tipos de Datos ---
# Solicitar datos al usuario y realizar operaciones matemáticas

e1 = int(input("Ingrese el primer número entero: "))
e2 = int(input("Ingrese el segundo número entero: "))
d1 = float(input("Ingrese un número decimal: "))

suma = e1 + e2 + d1
mayor = max(e1, e2)

print("\nDesglose de resultados:")
print(f"A. La suma total es: {suma}")
print(f"B. El mayor entre {e1} y {e2} es: {mayor}")

import math

# --- EJERCICIO 3: Potenciación ---
# Elevar una base a un exponente ingresado por el usuario
# Se utiliza float() para evitar errores si el usuario ingresa decimales o espacios

try:
    # .strip() elimina espacios accidentales al inicio o final
    base_input = input("Ingrese la base: ").strip()
    exponente_input = input("Ingrese el exponente: ").strip()

    # Convertimos a float para mayor flexibilidad
    base = float(base_input)
    exponente = float(exponente_input)

    resultado = base ** exponente

    print(f"\n--- Resultado ---")
    print(f"Base: {base}")
    print(f"Exponente: {exponente}")
    print(f"{base} elevado a {exponente} es igual a: {resultado}")

except ValueError:
    print("\nError: Por favor, ingrese solo números válidos (sin letras ni caracteres especiales).")

import math

# --- EJERCICIO 4: Raíz Cuadrada ---
# El usuario agrega los valores para calcular sus raíces cuadradas
# Se utiliza map() para convertir la entrada en una lista de números decimales

print("--- PROCESADOR DE RAÍCES CUADRADAS ---")

try:
    # Solicitamos al usuario los números separados por espacio
    entrada = input("Ingrese los números que desea procesar (separados por espacio): ").strip()

    # Usamos map para convertir cada elemento de la entrada en un número (float)
    # Esto permite manejar tanto enteros como decimales
    numeros = list(map(float, entrada.split()))

    if len(numeros) > 0:
        print("\nResultados del cálculo:")
        for n in numeros:
            # Controlamos que el número no sea negativo para evitar error matemático
            if n >= 0:
                raiz = math.sqrt(n)
                print(f"-> La raíz cuadrada de {n} es: {raiz:.2f}")
            else:
                print(f"-> Error: {n} es un número negativo (no tiene raíz real)")
    else:
        print("\nNo se ingresaron números para procesar.")

except ValueError:
    print("\nError: Asegúrese de ingresar únicamente números válidos separados por un espacio.")


# --- EJERCICIO 5: Promedio de Notas ---
# Cálculo del promedio final de un estudiante

estudiante = input("Nombre del estudiante: ")
# Usamos map para convertir las notas ingresadas en una lista de floats
notas_input = input("Ingrese las 5 notas separadas por espacio: ")
notas = list(map(float, notas_input.split()))

if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print(f"\nEstudiante: {estudiante}")
    print(f"Promedio Final: {promedio:.2f}")
else:
    print("No se ingresaron notas.")


# --- EJERCICIO 6: Intercambio de Valores ---
# Cambiar el valor de dos variables usando una variable auxiliar

a = input("Ingrese valor para variable A: ")
b = input("Ingrese valor para variable B: ")

print(f"\nValores originales: A = {a}, B = {b}")

auxiliar = a
a = b
b = auxiliar

print(f"Valores intercambiados: A = {a}, B = {b}")

# --- EJERCICIO 7: Operación Booleana ---
# Evaluación de expresiones lógicas (OR / AND)

print("Evaluación de la expresión: (5 == 2) or (2 > 1)")

estado = (5 == 2) or (2 > 1)

print(f"El resultado lógico de la variable 'Estado' es: {estado}")

# --- EJERCICIO 8: Operación Aritmética Compleja ---
# Resolución siguiendo la jerarquía de operadores en Python

# Expresión: (9 / 2) + 8 * 2 / 1 - (2 + 2)
resultado = (9 / 2) + 8 * 2 / 1 - (2 + 2)

print(f"Operación: (9 / 2) + 8 * 2 / 1 - (2 + 2)")
print(f"Resultado final: {resultado}")

# --- EJERCICIO 9: Áreas y Perímetros ---
# Cálculos para Cuadrado y Rectángulo

print("Cálculo Geométrico:")
# Cuadrado
lado = float(input("Ingrese el lado del cuadrado: "))
print(f"Cuadrado -> Área: {lado**2} | Perímetro: {lado*4}")

# Rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
print(f"Rectángulo -> Área: {base*altura} | Perímetro: {2*(base+altura)}")

import math

# --- EJERCICIO 10: Categorías por Edad ---
# Clasificación detallada con entrada de usuario, map y math.sqrt

def clasificar(edad):
    if edad <= 5: return "Infante"
    elif edad <= 10: return "Niño"
    elif edad <= 15: return "Pre adolescente"
    elif edad <= 18: return "Adolescente"
    elif edad <= 25: return "Pre adulto"
    elif edad <= 40: return "Adulto"
    elif edad <= 55: return "Pre anciano"
    else: return "Anciano"

print("--- PROCESADOR DE EDADES ---")
entrada = input("Ingrese las edades que desea procesar (separadas por espacio): ")

# Punto: Uso de MAP para convertir a enteros
edades = list(map(int, entrada.split()))

# Procesamiento punto por punto
for e in edades:
    # Punto: Uso de math.sqrt
    raiz_e = math.sqrt(e)
    categoria = clasificar(e)
    
    print("-" * 40)
    print(f"Análisis de Punto:")
    print(f"  * Edad: {e} años")
    print(f"  * Raíz cuadrada de la edad: {raiz_e:.2f}")
    print(f"  * Clasificación: {categoria}")
print("-" * 40)
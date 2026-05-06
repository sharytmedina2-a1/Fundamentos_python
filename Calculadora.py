# Actividad 2: Calculadora de Notas

# 1. Pedir las tres notas
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

# 2. Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

# 3. Calcular cuántos puntos faltan para 5.0
puntos_faltante = 5.0 - promedio

# 4. Determinar si aprueba
aprueba = promedio >= 3.0

# 5. Mostrar resultados
print( "\n ")
print("Promedio:", round(promedio, 2))
print("Puntos faltantes para 5.0:", round(puntos_faltante, 2))

if aprueba:
    print("Estado: Aprobado ")
else:
    print("Estado: Reprobado") 
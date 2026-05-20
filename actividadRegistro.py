# actividad2_diccionarios.py

# Diccionario con aprendices
grupo = {
    3321349: {
        "nombre": "Ana",
        "edad": 19,
        "notas": [4.5, 3.8, 4.2, 4.0],
        "ciudad": "Bogotá"
    },

    3322: {
        "nombre": "Luis",
        "edad": 21,
        "notas": [2.8, 3.0, 2.5, 3.1],
        "ciudad": "Medellín"
    },

    3323: {
        "nombre": "Sofía",
        "edad": 20,
        "notas": [4.8, 4.7, 4.9, 5.0],
        "ciudad": "Cali"
    },

    3324: {
        "nombre": "Carlos",
        "edad": 22,
        "notas": [3.5, 3.2, 3.8, 3.0],
        "ciudad": "Barranquilla"
    }
}

# Función para calcular promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Reporte de aprendices
print("REPORTE DE APRENDICES\n")

for ficha, datos in grupo.items():

    promedio = calcular_promedio(datos["notas"])

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Ciudad: {datos['ciudad']}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")
# Agregar nuevo aprendiz
grupo[3325] = {
    "nombre": "Marta",
    "edad": 23,
    "notas": [4.0, 3.9, 4.1, 4.3],
    "ciudad": "Tunja"
}

# Actualizar ciudad de un aprendiz
grupo[3322]["ciudad"] = "Cartagena"

print("\nNUEVO APRENDIZ AGREGADO")
print(grupo[3325])

# Ordenar aprendices de mayor a menor promedio
print("\nAPRENDICES ORDENADOS POR PROMEDIO")

ordenados = sorted(
    grupo.items(),
    key=lambda elemento: calcular_promedio(elemento[1]["notas"]),
    reverse=True
)

for ficha, datos in ordenados:
    promedio = calcular_promedio(datos["notas"])

    print(f"{datos['nombre']} -> {promedio:.2f}")
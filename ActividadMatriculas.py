# actividad4_sets.py

# Conjuntos de aprendices
python_curso = {'Ana','Luis','Marta','Carlos','Sofia','Pedro'}

java_curso = {'Luis','Carlos','Pedro','Laura','Diego'}

bd_curso = {'Marta','Sofia','Laura','Ana','Miguel'}

# Unión total de aprendices
total_unicos = python_curso | java_curso | bd_curso

print("TOTAL DE APRENDICES ÚNICOS")
print(total_unicos)
print(f"Cantidad: {len(total_unicos)}")

# Aprendices que cursan Python y Java
python_java = python_curso & java_curso

print("\nAPRENDICES EN PYTHON Y JAVA")
print(python_java)

# Aprendices solo en Python
solo_python = python_curso - java_curso - bd_curso

print("\nAPRENDICES SOLO EN PYTHON")
print(solo_python)

# Aprendices en exactamente dos programas
dos_programas = (
    (python_curso & java_curso) |
    (python_curso & bd_curso) |
    (java_curso & bd_curso)
) - (python_curso & java_curso & bd_curso)

print("\nAPRENDICES EN EXACTAMENTE DOS PROGRAMAS")
print(dos_programas)

# Lista con duplicados
inscripciones = [
    'Ana','Luis','Ana','Marta',
    'Carlos','Luis','Sofia',
    'Pedro','Ana'
]

# Convertir a conjunto
unicos_inscritos = set(inscripciones)

print("\nINSCRIPCIONES ÚNICAS")
print(unicos_inscritos)
print(f"Cantidad de inscritos únicos: {len(unicos_inscritos)}")

# Diccionario con cantidad de programas
conteo_programas = {
    aprendiz:
    (aprendiz in python_curso) +
    (aprendiz in java_curso) +
    (aprendiz in bd_curso)

    for aprendiz in total_unicos
}

print("\nCANTIDAD DE PROGRAMAS POR APRENDIZ")

for aprendiz, cantidad in conteo_programas.items():
    print(f"{aprendiz}: {cantidad}")

# Bonus
tres_programas = python_curso & java_curso & bd_curso

print("\n APRENDICES EN LOS TRES PROGRAMAS")
print(tres_programas)
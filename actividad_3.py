# 1. Solicitar peso y estatura
try:
    peso = float(input("Ingresa tu peso en kg: "))
    estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))

    # 5. Bonus: Validar valores positivos
    if peso <= 0 or estatura <= 0:
        print("Error: El peso y la estatura deben ser valores positivos.")
    else:
        # 2. Calcular IMC
        imc = peso / (estatura ** 2)

        # 3. Clasificar el resultado con if / elif / else
        if imc < 18.5:
            clasificacion = "😒 Bajo peso"
        elif 18.5 <= imc <= 24.9:
            clasificacion = "😊 Normal"
        elif 25 <= imc <= 29.9:
            clasificacion = "😩 Sobrepeso"
        else: # >= 30
            clasificacion = "😨 Obesidad"

        # 4. Imprimir valor y clasificación
        print(f"\nTu IMC es: {imc:.2f}")
        print(f"Clasificación: {clasificacion}")

except ValueError:
    print("Error: Por favor ingresa solo números.")
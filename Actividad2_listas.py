temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

print (f"la temperatura del dia 1 es {temperaturas [0]}")
print (f"la temperatura del dia 11 es {temperaturas [-3]}")
print (f"la temperatura del dia 7 es {temperaturas [6]}")
print (f"la temperatura del penultimo dia es {temperaturas [12]}")

#slicing para tarer e imprimir: la primera semana (dia 1-7), la segunda semana dias (8-14)

print (f"las temperaturas de la primera semana son {temperaturas[0:7]}")
print (f"las temperaturas de la segunda semana son {temperaturas[7:14]}")

#Solo los dias pares de toda la quinsena (dias 2,4,6,8,10,12,14)
print (f"la temperaturas de los dias pares son {temperaturas [1::2]}")

#La lista de temperatura en orden invertido
print (f"las temperaturas en orden invertido son{temperaturas[::-1]}")

#Calcula e imprime la temperatura promedio de cada semana por separado usando, sum() y len () 
primera_semana_1 = temperaturas[0:7]
segunda_semana_2 = temperaturas[7:14]

promedio_semana_1 = sum(primera_semana_1) / len(primera_semana_1)
promedio_semana_2 = sum(segunda_semana_2) / len (segunda_semana_2)

print(f" el promedio de la semana 1 es {int (promedio_semana_1)}")
print (f" el promedio de la segunda semana es {int (promedio_semana_2)}")

#Bonus determina cual de las siguientes semanas tuvo mayor temperatura promedio 

if promedio_semana_1 > promedio_semana_2:
    print("la semana uno tuvo mayor promedio")
elif promedio_semana_1 < promedio_semana_2:
    print("la segunda semana tuvo mayor prommedio")
else:
    ("las semanas tuvieron el mismo promedio")
    



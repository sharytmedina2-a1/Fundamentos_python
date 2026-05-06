#ondicional/IF/ELIF/ELSE

if True:
    print ("la condicion es verdadera")
    
elif False: 
    print ("La segunda condicion es verdadera en ELIF")
    
elif True: 
    print ("La tercera condicion es verdadera en ELIF")
    
else:
    print ("la condicion es falsa")
    
    
   # Ejercicio: Clasificación de Edad

edad = 12

if edad < 18:
    print("Eres un menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
    
   #operador ternario 
   
numero = 4
if numero % 2 == 0:
    print ("El numero es par")
else:
    print ("El numero es impar")
    
print ("el numero es par" if numero % 2 == 0 else "El numero es impar")
    
import random

print("🎲Bienvenido al juego de los dados🎲\n")

#INPUT
nombre = input ("¿Cual es tu nombre?")
numero = int(input("Elige un numero del 1 al 6:"))

#VALIDACIÓN
if numero >=1 and numero <=6: 
    dado = random.randint(1,6)
    print ("\n🎲El dado cayo en:",dado)
    
    #RESULTADO
    if numero == dado:
        print("🥳¡GANASTE!",nombre)
    else: 
        print ("😿 Perdiste",nombre)
        
        #BONUS (USA LOGICO)
        if numero == dado and numero == 6:
            print ("🔥¡SACASTE EL NUMERO MAS ALTO!")
            
else: 
    print("❌ Numero invalido")
    
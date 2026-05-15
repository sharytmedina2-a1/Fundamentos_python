#TUPLAS

#Estructura de una tupla

tupla = ("elemento_1", "elemento_2", "elemento_3")
print(type(tupla)) # <class 'tuple'>

tupla_2 = "a", "b", "c"
print(type(tupla_2))

tupla_3 = ("Hola")
print(type(tupla_3))

tupla_4 = tuple ("Hola")
print (tupla_4) #('h', 'o', 'l', 'a')

tuplas_mixta = ("hola", 123, 3.14, True, [1,2,3])
print(tuplas_mixta)

#Tuplade aprendices SENA ADSO 

#indice:         0         1          2            3         4
aprendices = ("simon", "camilo", "santiago", "valentina","laura")
print(aprendices)

#Acceder a un elemento de la tupla 
print (aprendices[2]) #Santiago

#modificar un elemento de la tupla 
# aprendiz [2]= "Daniel" #Esto genera un error porque las tuplas son inmutables 

#Consultar ranngos de elementos de las listas 
print(aprendices[0:2]) #(simon', 'camilo')
print(aprendices[1:4]) #('camilo, 'santiago', 'valentina')
print(aprendices[1:])  #('camilo, 'santiago', 'valentina', 'laura')

#sumar 2 duplas 
tupla= (1,2,3)
tupla_2 = (4,5,6)
tuplas_suma = tupla * 3
print (tuplas_suma) #(1,2,3,4,5,6)

#multiplicar una tupla
tupla_multiplicada = tupla *3
print (tupla_multiplicada)

#metodos de las duplas 

#medir el largo con len ()
print (len(aprendices)) #5

#cortar elementos repartidos en una tupla con count
print (aprendices.count("camilo")) #1

#obtener el indice de un elemento con index
print (aprendices.index("valentina")) #3

#modificar una tupla en una lista 

print (type(aprendices)) #<class 'tuple'>

aprendices_lista = list(aprendices)
aprendices_lista.append("Felipe")
print (aprendices_lista)
print (type(aprendices_lista))

aprendices = tuple (aprendices_lista) #convertimos la lista de nuevo en una tupla
print (aprendices)

 #comprobar pertenencia (in)
print("simon" in aprendices) #True
print("Andres" in aprendices) #false 

#empaquetar tuplas 
programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "Topografia"

tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas)

#Desempaquetar duplas 
tupla_desempaquetada =("ADSO","SST","TOPPGRAFIA")
programa_1,programa_2,programa_3 = tupla_desempaquetada
print(programa_1) #ADSO

#ejercicio 2 desempaquetar duplas 

tupla_ciudades = ("Bogota", "Medellin","Cali")

ciudad_1, *ciudad_2, ciudad_3 = tupla_ciudades
print(ciudad_1) #Bogota
print(ciudad_2) #['Medellin', 'Cali']

for ciudad in tupla_ciudades: 
    print (ciudad)
    
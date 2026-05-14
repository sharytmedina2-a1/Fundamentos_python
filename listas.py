#Listas 

#Esctruvtura de una lista 
listas = ["objeto_1", "objeto_2", "objeto_3"]
print (type(listas)) #class list


#Lista de aprendices de ADSO

#Crear una lista vacia
# indice         0        1       2        3         
Aprendices = ["Miguel","Brayan","David","Daniela"]

#Acceder a un elemento de la lista
print(Aprendices[1])

#Modificar un elemto de la lista 
Aprendices [1] = "Camilo"
print (Aprendices)

#Consultar rangos de elemtos de la lista 
print( Aprendices [0:2]) #["Camilo", "Miguel"]
print( Aprendices[:1])
print( Aprendices [3:1])
print( Aprendices[0:2:3])

# unir 2 listas

aprendices_ficha_3321349 = ["Jhon", "Mario", "Mario", "Andres"]
aprendices_ficha_2321322 = ["Maria", "Luna", "Miguel"]

Aprendices_unidos = aprendices_ficha_2321322 + aprendices_ficha_3321349
print(Aprendices_unidos)


# medir el largo con len() para saber cuantos hay en la lista.
print(len(Aprendices_unidos))

#contar elementos repetidos
count_Mario = aprendices_ficha_3321349.count("Mario")
print(f"el aprendiz aparece {count_Mario} veces en la lista")

print(aprendices_ficha_3321349.count("Sharyt"))

#obtener el indice de un elemento con index
indice_jhon = aprendices_ficha_2321322.index("Miguel")
print (f "el nombre de miguel se ecnuentra en el indice {indice_miguel}")

#ordenar (sort y reverse)

# Conjuntos (SETS) en python

#Estructura de un conjunto 

conjunto = set ()

print(type(conjunto)) #class 'set'> - esto si es un set

#--creación--
lenguajes = {"python","java","C++","python","java"}
print(lenguajes)

#Metodos de modificación 
frutas = {"mago", "guayaba","mora"}
frutas.add("Maracuya") #Agrega un elemento
frutas.add("mango") #No hace nada ya exieste 
frutas.remove("mora") #Elimina lanza error si no existe 
frutas.discard("papaya") #Elimina no lanza error si no existe
elem = frutas.pop() #Elimina y retorna un elemento aleatorio
print(elem)

#Verificar pertenencia: 0(1) ---
print("python" in lenguajes) #True instantaneo sin importar 
print("COBOL") in lenguajes

python_devs = {"Ana","Luis","Brayan","Miguel","Juan"}
java_devs = {"luis","Ana","pedro","Laura"}

#Union de conjuntos 
union ={"Ana","Luis","Marta","Carlos","Sofia","Pedro","Laura"}

#interaccion 
interaccion = {"lus","carlos"}
ambos = python_devs & java_devs
interaccion = python_devs.intersection(java_devs)
print(interaccion)

#Diferencia
solo_python = python_devs
print
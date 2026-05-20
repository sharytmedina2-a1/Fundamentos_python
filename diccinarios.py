#Diccionario (caracteristicas a un Elemnto)

#creacion de un diccionario 
#Estructura de un diccionario 

diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"
}

#diccionario vacio 
diccionario_vacio = {}

#Diccionario con elementos 
diccionario_aprendiz = {
    "nombre": "Sharyt",
    "Apellido": "Medina",
    "ficha": "3321349",
    "programa": "Adso",
    "edad" : 19
}

print (type(diccionario_aprendiz))

#Obtener el valor del Diccionario 
print(diccionario_aprendiz ("programa"))
print(diccionario_aprendiz.get ("programa"))

#Obtener solo las claves del diccionario 
print(diccionario_aprendiz.keys())

#Obtener solo los valores del Diccionario 
print(diccionario_aprendiz.values())

#Obtener la clave y el valor 
print(diccionario_aprendiz.items())

#Agregar un nuevo elemento al diccionario 
diccionario_aprendiz["correo"] = "Sharytmedina2@gmail.com"

#Modificar un valor del Diccionario 
diccionario_aprendiz["programa"] = "SST"
print(diccionario_aprendiz)

#Metodo uptade ()

diccionario_aprendiz.update({"nombre":"Yuliana"}) #Modifica un elemento
diccionario_aprendiz.update({"ciudad":"Sogamoso"}) #agrega un nuevo elemento 
print(diccionario_aprendiz)

#Comprobar pertenencia (in)

if "ficha" in diccionario_aprendiz:
    print("ficha es una de las propiedades de este diccionario")
    
#Recorrer un diccionario con un ciclo for
for clave in diccionario_aprendiz.key():
    print(clave)
    
#Recorrer solo los valores del Diccionario 
for valor in diccionario_aprendiz.values():
    print (valor)
    
#Recorrer las claves y los valores del Diccionario 
for clave, valor in diccionario_aprendiz.items ():
    print(f"{clave}:{valor}")
    
#Eliminar Elementos de un diccionario POP ()
diccionario_aprendiz.popitem() #Elimina el ultimo elemento agregado 
print(diccionario_aprendiz)

diccionario_aprendiz.pop("edad") #Elimina un elemento especifico 
print(diccionario_aprendiz)

diccionario_aprendiz.clear() #Elimina todos los elementos del diccionario
print(diccionario_aprendiz)

#Diccionarios Anidados 

aprendices = {
    "aprendiz_1": {                       
    "nombre": "Sharyt",
    "Apellido": "Medina",
    "ficha": "3321349",
    "programa": "Adso",
    "edad" : 19
    },
    "aprendiz_2": {
    "Nombre": "Brayan",
    "apellido": "Orduz",
    "Ficha": "3321349",
    "programa": "Adso",
    "edad" : 20
    }, 
    "aprendiz_3": {
    "Nombre": "Miguel",
    "apellido": "Castañeda",
    "Ficha": "3321349",
    "programa": "Adso",
    "edad" : 20
    }
}

#Acceder a un valor de un diccionario Anidado 
print(aprendices["aprendiz_2"]["programa"]) #SST

#Reccorrer un diccionario anidado con un ciclo for 
for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    for clave,valor in datos.items():
        print(f" {clave}:{valor}")

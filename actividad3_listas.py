#Declara una lista canciones con 5 nombres de canciones, de tu género favorito.


Canciones_fav = ["Amor de manicomio", "Fiesta pagana", "Esperando un pin", "Creep", "Querer querernos"]
print(Canciones_fav)
print("--" * 50)

#append() para agregar una canción nueva al final;
Canciones_fav.append("el tierno")
print(Canciones_fav)
print("--" * 50)

#insert() para agregar, otra canción en la segunda posición;

Canciones_fav.insert(1, "el sol no regresa")
print("se agrego una nueva canciones de primeras", Canciones_fav)

lista_bonus = ["Bonus Track 1", "Bonus Track 2"]
print("--" * 50)

#extend() para fusionar con esta lista: ["Bonus Track 1", "Bonus Track 2"].
Canciones_fav.extend(lista_bonus)
print(Canciones_fav)
print("--" * 50)

#Usa remove() para eliminar una canción por su nombre y pop() para eliminar la última canción,
Canciones_fav.remove("Amor de manicomio")
print(Canciones_fav)

Canciones_fav.pop()
print(Canciones_fav)
print("--" * 50)

#Usa sort() para ordenar la lista alfabéticamente y muéstrala ordenada.
Canciones_fav.sort()
print("Lista ordenada", Canciones_fav)
print("--" * 50)


#Responde estas preguntas usando métodos:

#¿Cuántas canciones tiene la playlist?
print(len(Canciones_fav))
print("--" * 50)

#¿En qué posición está la primera canción que agregaste?

indice_primera_cancion = Canciones_fav.index("MLP")
print(f"el indice de el sol no regresa es: {indice_primera_cancion}")
print("--" * 50)

#¿Cuántas veces aparece el string 'Bonus Track 1'?

count_bonus = Canciones_fav.count("Bonus Track 1")
print(f"el elemento bonus track 1 se repite en la lista: {count_bonus} vez")
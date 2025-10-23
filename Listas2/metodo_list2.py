#              1        2         3        4        5
#             -5        -4         -3     -2        -1
cursos = [ "python", "django", "flask", "ruby", "mongodb"] #strings (5)

##metodos de listas
# copy
# reverse
# sort

#copy
copy_lista = cursos.copy()  # Crea una copia superficial de la lista
print(copy_lista)


#reverse
cursos.reverse()  # Invierte el orden de los elementos en la lista
print(cursos)


#sort
cursos.sort() # Oredena los elementos de la lista en orden ascendente  alfabetico de a la z
print(cursos)

# ordenar de la z a la a
# cursos.sort(reverse=True)  # Ordena los elementos de la lista en orden descendente
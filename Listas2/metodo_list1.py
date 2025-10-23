#             1        2         3        4        5
#            -5     -4        -3        -2        -1 
cursos = ["python", "django", "flask", "ruby", "mongodb"] #strings (5)
new_cursos = ["Recat","Next"]


#permite agregar un elemento al final de la lista
cursos.append("Ruby on rails") # Agrega "Ruby on rails" al final de la lista

cursos.append("PHP")
cursos.append("JavaScript")


#permite insert un elemento en una posicion especifica
cursos.insert(0, "Rust") # Inserta "Rust" al inicio de la lista

cursos.insert(4, "C#")
cursos.insert(2, "MySQL")


cursos.extend(new_cursos) # Agrega los elementos de new_cursos al final de cursos


# Verifica si un elemento está en la lista
print(
    "python" in cursos  # Verifica si "python" está en la lista
)

print(
    "Vue" in cursos  # Verifica si "Vue" está en la lista
)

# Verfiica en que indice se encuentra un elemento
print(
    cursos.index("flask")  # Obtiene el índice del primer elemento "flask"
)

print(
    cursos.index("C#")  # Obtiene el índice del primer elemento "C#"
)

# Elimina un elemento específico de la lista
cursos.remove("C#")  # Elimina el primer elemento "C#"

# Elimina el último elemento de la lista
cursos.pop()  # Elimina y devuelve el último elemento de la lista

#expulsar el primer elemento de la lista con pop(0)
first_elemento= cursos.pop(0)
print(first_elemento)


#limpia la lista pero toda 
cursos.clear()  # Elimina todos los elementos de la lista


print(cursos)
print(len(cursos))


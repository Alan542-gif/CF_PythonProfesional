#              -5      -4        -3        -2        -1
#              0        1         2        3        4
cursos = ["python", "django", "flask", "ruby", "mongodb"] #strings (5)


# Slicing de listas
#                [start:end]
new_list = cursos [0:3]

# [:3] empieza desde el incio osea 0 

new_list = cursos [2:5]
# [2:5] empieza desde el 2 hasta el final
# funciona igual de [2:] y va del dos al final

print(new_list)



#shallow copy
"""
cursos_copy = cursos[:]
# cursos_copy = cursos.copy()  # Otra forma de hacer una copia superficial

print(cursos_copy)

"""
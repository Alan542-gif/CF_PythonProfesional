# DEFINICIÓN DE UNA TUPLA 

#               0           1      2
settings = ("localhost", 3306, True)

print(settings)
print(type(settings))

print("________________________")

print(settings[0])
print(settings[1])
print(settings[2])


#si accedemos a un índice que no existe, nos dará error (index error)

#las tuplas son inmutables, no podemos modificar sus valores

#para fines de lectura, para que consserven por el resto del programa los valores que tienen.

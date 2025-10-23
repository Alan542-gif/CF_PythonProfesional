#se puede crear una tupla sin parentesis

settings = ("localhost", 3306, True)

# se deben de separar por comas los elementos de la tupla


numbers = 1, 2, 3, 4, 5

print(numbers)
print(type(numbers))

#aunque en la definicion no se usen parentesis, sigue siendo una tupla por que lo reconoce asi python

# si queremos crear una tupla de un solo elemento, debemos poner una coma al final
#valores debe ir separados por comas
#si vemos valores separados por una coma, estamos tratrando con una tupla
numbers1= 1, 

print("numbers1")
print(type(numbers1))
#funciones de tuplas

numbers = (1,4,5,3,3,7,2,10)

print (len(numbers))  #len, nos devuelve la cantidad de elementos de la tupla

print(sorted(numbers)) #sorted, nos devuelve una lista con los elementos ordenados
# el ordenamiento sera de forma ascendente por defecto

print(sorted(numbers, reverse=True)) # si queremos ordenarlo de forma descendente

print(numbers.count(3)) #count, nos devuelve la cantidad de veces que aparece un elemento en la tupla
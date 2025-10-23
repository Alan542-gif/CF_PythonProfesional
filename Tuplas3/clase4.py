#desempaquetado de tuplas 2 
#             0          1         2         3           4          5
courses = ("Python", "Django", "Ruby","Ruby on Rails", "MySQL", "MongoDB")

#exceptuar algunos valores al desempaquetar

#conjuncion de guiones bajas _ para ignorar valores

va1, _, var3, _, var5, _ = courses

print(va1, var3, var5)

print(_)  #ultima variable _ tiene el valor de la ultima posicion ignorada


var1, var2, *sub_courses = courses
print( var1, var2, sub_courses)

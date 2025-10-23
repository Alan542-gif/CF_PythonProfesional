#las tuplas en python son inmutables, no se pueden modificar una vez creadas
#ni se pueden agregar o eliminar elementos que se encuentre dentro de ella

#desempaquetado de tuplas
#             0          1         2         3           4
courses = ("Python", "Django", "Ruby","Ruby on Rails", "MySQL")

print(courses)

#var1= courses[0]
#var2= courses[1]
#var3= courses[2]
#var4= courses[3]
#var5= courses[4]

var1, var2, var3, var4, var5 = courses

print(var1, var2, var3, var4, var5)

#concepto de desempaquetado de tuplas

#zip 
#permite trabajar con diferentes conecciones y apartir de ellas crear tuplas

users = ["user1", "user2", "user3"]
courses = ["Python", "Django", "Ruby"]
scores = [100, 90, 80]

response = list(zip (users, courses, scores))

#response = list(zip (users, courses,scores))
#list, vams a generar una lista de tuplas

#response = tuple(zip (users, courses, scores))
# tuple, vamos a generaruna tupla de tuplas

print(response)  #objeto zip 

#el primer elemento de cada iterable se empareja, luego el segundo elemento de cada iterable se empareja, y asi sucesivamente


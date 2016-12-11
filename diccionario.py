diccionario = {'a':True, 5:'Esto es un string',  (1, 2):False} #Las claves deben de ser inmutables tal como los enteros, strings y tuplas.
print(diccionario)

diccionario = {'a':True, 5:'Esto es un string',  (1, 2):False,  'a':100} #Si una llave se repite, toma siempre el ultimo valor
print(diccionario)

#Modificar/Agregar valores al diccionario
diccionario['n'] = 'Nuevo string' #Nueva clave/valor
print(diccionario)

#Obtener un valor desde un diccionario
valor = diccionario['a']
print('Valor obtenido en la variable valor: ',  valor)

#Get nos ayuda a evitar errores al monento de obtener un valor del diccionario
valor = diccionario.get('z',  False) #Nos devuelve False si no encuentra la llave en el diccionario
print(valor)

#Eliminar una clave/valor del diccionario
del diccionario[5]
print(diccionario)

#Obtiniendo las llaves del diccionario
llaves = diccionario.keys() #Obtenemos un objeto iterable para poder recorerlo si es necesario
print(llaves)

#Convirtiendo el objeto iterable en una lista pura (Podemos convertirlo a tupla con la palabra tuple)
llaves = list(diccionario.keys())
print(llaves)

#Obteniendo los valores del diccionario y convertirlos a una lista pura (Podemos convertirlo a tupla con la palabra tuple)
valores = list(diccionario.values())
print(valores)

#Formas de extender diccionarios
#La forma menos recomendada
diccionario2 = {'x':3,  'y':4}
diccionario['x'] = diccionario2['x']
diccionario['y'] = diccionario2['y']
print(diccionario)

#La forma recomendada
diccionario.update(diccionario2) #Esto actualiza diccionario, agregando los elementos del diccionario 2
print(diccionario)

curso = 'Curso'
mi_string = 'Python 3'

# Metodos de FORMATO

resultado = '{} de {}'.format(curso,  mi_string) #Forma estandar
print(resultado)

resultado = '{a} de {b}'.format(a=curso, b=mi_string) #Con alias
print(resultado)

resultado = resultado.lower()
print('En minusculas con "lower()": ', resultado)

resultado = resultado.upper()
print('En mayusculas con "upper()": ', resultado)

resultado = resultado.title()
print('Las primeras letras con mayuscula con "title()": ', resultado)

# Metodos de BUSQUEDA

posicion = resultado.find('Python') #Nos indica en que POSICION inicia la palabra buscada
print(posicion)

contar = resultado.count('o') #Nos indica cuantas veces se repite la palabra o letra buscada
print(contar)

nuevo_string = resultado.replace('o',  'x') #Reemplaza la palabra o letra buscada por la nueva letra o palabra asignada
print(nuevo_string)

nuevo_string = resultado.split(' ') #Secciona mi string segun el criterio y me devuelve una lista
print(nuevo_string)

lista = ['Strings',  1,  5.3,  True]
lista_numeros = [12, 5, 32, 26, 42, 6, 58, 70]
lista_numeros_dos = [35, 36]

lista.append(6) #Agrega un elemento al final de la lista
lista.insert(1,  'Instertado') #Inserta un elemento en un lugar especifico de la lista
lista.remove(1) #Elimina un elemento de la lista

print('Lista completa ',  lista)
ultimo_valor = lista.pop()
print('Lista completa sin el ultimo valor',  lista)
print('Un elemento de la lista ',  lista[1])
print('Ultimo valor extraido de la lista',  ultimo_valor)

print(lista_numeros)
lista_numeros.sort() #Ordena la lista de enteros en orden ascendente
print(lista_numeros)
lista_numeros.sort(reverse=True) #Ordena la lista de enteros en orden descendente
print(lista_numeros)

lista_numeros.extend(lista_numeros_dos) #Unir los valores de dos listas
print(lista_numeros)

lista_numeros.append(lista_numeros_dos) #Agrega la lista a la otra lista
print(lista_numeros)

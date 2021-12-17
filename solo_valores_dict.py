def solo_valores(dic):
    lista = []
    for c, v in dic.items():
        lista.append(v)
    return lista

#Funcionamiento  
edades = {
    "Juan": 10,
    "Maria": 11,
    "Carlos": 9,
}
print(solo_valores(edades)) # [10, 11, 9]

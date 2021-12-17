#Ordenamiento por el métudo de Burbuja
def ord_burbuja(lst):
    for numpas in range(len(lst) - 1, 0, -1):
        for i in range(numpas):
            if lst[i] > lst[i + 1]:
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp

#Funcionamiento
lista = [54,26,93,17,77,31,44,55,20]
ord_burbuja(lista)
print("ordenado %s" %lista) # [17,20,26,31,44,54,55,77,91]

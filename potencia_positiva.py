#Función que calcula la potencia positiva de un número
def potencia_positiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        resultado = 1
        while exponente > 0:
            resultado *= base
            exponente -= 1
        return resultado
#Prueba de funcionamiento        
print(potencia_positiva(5,3))

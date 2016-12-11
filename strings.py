# Trabajando con Strings
mi_string = "Hola mundo!, esto es un string."

mi_string_con_salto_de_linea_manual = """Hola mundo!,
Este es un string con salto de linea manual"""

mi_string_con_salto_de_linea_automatico = """Hola mundo!,\nEste es un string con salto de linea automatico"""

curso = "Python 3"
nombre = "Juan Perez"

# Formas de concatenar Strings
mensaje_final = "Nuevo curso de "+ curso+ " por " + nombre #1
mensaje_final = "Nuevo curso de %s por %s" %(curso,  nombre) #2
mensaje_final = "Nuevo curso de {} por {}".format(curso,  nombre) #3

print(mi_string)
print(mi_string_con_salto_de_linea_manual)
print(mi_string_con_salto_de_linea_automatico)

print(mensaje_final)

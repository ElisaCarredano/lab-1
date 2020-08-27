#Clase de programacion
#Proyecyo: Instrucciones 
#Autor: Carredano Ochoa Elisa
#Carnet: 16285-20
#Fecha: 27 de agosto 2020
#Operaciones divisibles
print("¡Hola! Estamos resolviendo operaciones divisibles")

a = input("Ingresa el valor de A: ")
a = int(a)

b = input("Ingresa un valor para B: ")
b = int(b)

mod1 = b % a
mod2 = a % b 

#el valor de verdad
#Doble igual sirve para evaluar si dos numeros son iguales
# Mod1 es igual a 0?
val1 = (mod1 == 0) 

# Mod2 ws igual a 0?
val2 = (mod2 == 0)

print("B es divisible entre A es: ", val1)
print("A es divisible entre B es: ", val2)
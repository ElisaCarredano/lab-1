#Clase de programacion
#Proyecyo: Instrucciones 
#Autor: Carredano Ochoa Elisa
#Carnet: 16285-20
#Fecha: 27 de agosto 2020
#Operaciones cuadraticas
print("¡Hola! Estamos resolviendo operaciones cuadraticas")

a = input("Ingresa el valor de A: ")
a = int(a)

b = input("Ingresa un valor para B: ")
b = int(b)

c = input("Ingresa un valor para C: ")
c = int(c)

# ac 2 + bx + c = 0
b_neg = -1 * b
exp = 1 / 2  

# x1 = (-b + ((b^2 - 4ac) ^ 1/2)/2a
x1 = (b_neg + ((b**2) - 4*a*c) ** exp) / (2 * a)

# x2 = (-b + ((b^2 - 4ac) ^ 1/2)/2a
x2 = (b_neg - ((b**2) - 4*a*c) ** exp) / (2 * a)

print("x1 es: ", x1)
print("x2 es: ", x2)
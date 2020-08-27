#Clase de programacion
#Proyecyo: Instrucciones 
#Autor: Carredano Ochoa Elisa
#Carnet: 16285-20
#Fecha: 27 de agosto 2020
#Diferentes operaciones con numeros
print("¡Hola! Estamos haciendo varias operaciones")

num_1 = input("Ingresa un numero: ")
num_1 = int(num_1)

num_2 = input("Ingresa otro numero: ")
num_2 = int(num_2)

num_3 = input("Ingresa un numero mas: ")
num_3 = int(num_3)

input('Presionar enter para ver la operacion') 

#Sumar dos numeros
suma = num_1 + num_2
print("la suma del primero y el segundo es: " ,suma)

#Multiplicamos el primero y el segundo
mult = num_1 * num_2
print("la multiplicacion del primero y el segundo es: ", mult)

#dividimos el tercero y el primero
div = num_3 / num_1
print("la division del tercer y el primero es: ", div)

#restamos los tres numeros
Resta = num_1 - num_2 - num_3
print("la resta de los tres numeros es: ", Resta)

#elevar un numero
exp = num_1 ** num_2
print("el primer numero elevado al segundo es: ", exp)

#modulo - operacion que devuelve el residuo de una division
#8 / 3 = 2.67
#El modulo seria 2 
modulo = num_3 / num_1
print("el residuo de la division  del primero y el tercero es: ", modulo)

#Division piso
#el residuo de una division aproximado a su resultado entero mas cercano por
#debajo
piso = num_3 // num_1
print("el piso de la division del tercer y el primero es:" , piso)
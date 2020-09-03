#Parcial de programacion
#Proyecyo: Calculo de distancia 
#Autor: Carredano Ochoa Elisa
#Carnet: 16285-20
#Fecha: 03 de septiembre 2020
#Calcular la distancia de un objeto
print("¡Bienvenido! Calcularemos la distancia de cualquier objeto: ")

nombre = input("Ingresa el nombre de tu objeto: ")

V_inicial = input("ingrese la velocidad en m/s: ")
V_inicial = int(V_inicial)

tiempo = input("ingrese el tiempo en segundos: ")
tiempo = int(tiempo)

aceleracion = input("ingrese la aceleracion del objeto: ")
aceleracion = int(aceleracion)

input('Presionar enter para ver tu resultado')

#operacion para nuestrro resultado
distancia = print(V_inicial * tiempo + 1/2 * aceleracion * tiempo**2)

#Clase de programacion
#Proyecyo: Tiempo de Vida
#Autor: Carredano Ochoa Elisa
#Carnet: 16285-20
#Este programa encontrara el tiempo de vida de una persona en base a su fecha de nacimiento

from datetime import date

#Fecha de hoy
hoy = date.today()

#obtener el dia de hoy
dia = hoy.day

#mes obtener el mes de hoy
mes = hoy.month

#obtener el año de hoy
year= hoy.year

#Obtener los datos de la persona
print("Hola,vamos a averiguar tu tiempo de vida en este mundo")

#0btener el nombre y apellido de la persona 
Nombres = input("Ingresa tus nombres: ")
Apellidos = input("Ingresa tus apellidos: ")

#obtener el dia de nacimiento de la persona
dia_nac = input("¿cual es el dia de la fecha de tu nacimiento?: ")
dia_nac = int(dia_nac)

#obtener el mes de nacimiento de la persona
mes_nac = input("¿cual es el mes de la fecha de tu nacimiento?: ")
mes_nac = int(mes_nac)

#obtener el año de nacimiento de la persona
year_nac = input("¿En que año naciste?: ")
year_nac = int(year_nac)

diff_year = year - year_nac
diff_dia = dia - dia_nac
diff_mes = mes - mes_nac
diff_year-= ((mes , dia) < (mes_nac , dia_nac))
# String - cadena - str
print("tienes " + str(diff_year) + " años " + str(diff_mes) + " meses " + str(diff_dia) + " dias ") 
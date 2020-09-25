#Clase de programacion
#Proyecyo 1 Introduccion a la programacion
#Autores: Carredano Ochoa Elisa - Alvarado Morales Lluviza 
#Carnet: 16285-20 , 15196-20
#Fecha: 25 de septiembre 2020
#Cuanto sabes de Cultura General
marcador_correcta = 0
from time import sleep
from screen import clear 
from random import randint

print("Contesta este Quizz y te diremos a que escritor famoso te pareces. XD")
sleep(7)
clear()

print("Principalmente, consiste en una serie de preguntas en las que aparecen unas respuestas multiples que tienes que seleccionar") 
print("para completar este Quizz tienes que responder a todas las preguntas.")
print("No olvides compartir con tus amigos tus resultados y guarda este programa, te aseguramos horas de diversión! :) ")

sleep(20)
clear()

nombre = input("Ingresa tu nombre y apellido: ")
nombre = str(nombre)
sleep(1)
clear()

genero = input("Ingresa tu genero")
#muestro las opciones al usuario
print("""
1. masculino
2. femenino
""")
eleccion_usuario = input("Selecciona el numero: ")
eleccion_usuario = int(eleccion_usuario) 
sleep(1)
clear()

pais = input("¿De que pais nos visitas?: ")
pais = str(pais)
sleep(1)
clear()

inicio = input("Enhorabuena, vamos a comenzar con este Quizz")
sleep(0.60)
clear()
inicio = input("Presiona ENTER para comenzar")
sleep(0.80)
clear()

pregunta_1 = input("¿Cuál es el lugar más frío de la tierra?")
#Muestro las opciones al usuario
print("""
1. Polo Norte
2. La Artantida
3. Alaska
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1:
    print("¡Incorrecto! 0 pts.")     
elif eleccion_usuario == 2:
    marcador_correcta += 10
    print("¡Correcto! Has ganado 10 pts.")
else: 
    print("¡Incorrecto! 0 pts.")
sleep(3)
clear()

pregunta_2 = input("¿Cómo se llama la Reina del Reino Unido?")
#Muestro las opciones al usuario
print("""
1. Reina Isabel II
2. Reina Maria
3. Reina Sofia II
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
elif eleccion_usuario == 2:
    print("¡Incorrecto! 0 pts.")
else: 
    print("¡Incorrecto! 0 pts.")
sleep(3)
clear()

pregunta_3 = input("¿Cuándo acabó la II Guerra Mundial?")
#Muestro las opciones al usuario
print("""
1. 1946
2. 1940
3. 1945
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
    print("¡Incorrecto! 0 pts.")
elif eleccion_usuario == 2:
    print("¡Incorrecto! 0 pts.")
else: 
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
sleep(3)
clear()

pregunta_4 = input("¿Dónde se encuentra la Sagrada Familia?")
#Muestro las opciones al usuario
print("""
1. Barcelona
2. Quetzaltenango
3. Roma
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
elif eleccion_usuario == 2:
    print("¡Incorrecto! 0 pts.")
else: 
    print("¡Incorrecto! 0 pts.")
sleep(3)
clear()

pregunta_5 = input("¿Cómo se denomina el resultado de la multiplicación?")
#Muestro las opciones al usuario
print("""
1. Residuo
2. Producto
3. Cociente
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
    print("¡Incorrecto! 0 pts.")
elif eleccion_usuario == 2:
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
else: 
    print("¡Incorrecto! 0 pts.")
sleep(3)
clear()

pregunta_6 = input("¿Qué año llegó Cristóbal Colón a América?")
#Muestro las opciones al usuario
print("""
1. 1491
2. 1490
3. 1492
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
    print("¡Incorrecto! 0 pts.")
elif eleccion_usuario == 2:
    print("¡Incorrecto! 0 pts.")
else: 
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
sleep(3)
clear()

pregunta_7 = input("¿Cuál es el disco más vendido de la historia?")
#Muestro las opciones al usuario
print("""
1. Back in Black de AC/DC
2. The Dark Side of the Moon de Pink Floyd.
3. Thiller de Michael Jackson
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
     print("¡Incorrecto! 0 pts.")
elif eleccion_usuario == 2:
    print("¡Incorrecto! 0 pts.")
else: 
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
    sleep(3)
    clear()

pregunta_8 = input("¿Cuál es tercer planeta en el sistema solar?")
#Muestro las opciones al usuario
print("""
1. Tierra
2. Marte
3. Jupiter
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
elif eleccion_usuario == 2:
    print("¡Incorrecto! 0 pts.")
else: 
    print("¡Incorrecto! 0 pts.") 
sleep(3)
clear()

pregunta_9 = input("¿Cuál es el primero de la lista de los números primos?")
#Muestro las opciones al usuario
print("""
1. 2
2. 1
3. 5
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
elif eleccion_usuario == 2:
    print("¡Incorrecto! 0 pts.")
else: 
    print("¡Incorrecto! 0 pts.")
sleep(3)
clear()

pregunta_10 = input("¿Quien traiciono a Jesus de Nazareth?")
#Muestro las opciones al usuario
print("""
1. Judas Tadeo
2. Judas Iscariote
3. Lazaro
""")
eleccion_usuario = input("Elige una: ")
eleccion_usuario = int(eleccion_usuario)

if eleccion_usuario == 1: 
    print("¡Incorrecto! 0 pts.")
elif eleccion_usuario == 2:
    print("¡Correcto! Has ganado 10 pts.")
    marcador_correcta += 10
else: 
    print("¡Incorrecto! 0 pts.")
sleep(3)
clear()

fin = input("Has concluido con este Quizz")
sleep(0.50)
clear()
fin = input("Presiona ENTER para ver tus resultados")
print("Excelente lo has logrado, has ganado", marcador_correcta, "puntos", "Eeeeeeh :P")
lista_escritores = ["James Joyce: Eres muy parecido a James Joycey escribe relatos de momentos que se revelo la verdad real sobre una persona u objeto ", 
"Sofocles: Eres muy parecido a Sófocles ya que fue un poeta trágico griego. Autor de obras como Antígona y Edipo rey, se sitúa, junto con Esquilo y Eurípides, entre las figuras más destacadas de la tragedia griega. ", 
"Homero: Eres muy parecido a Homero un poeta muy conocido en la antigua grecia, el se basaba el los rasgos del lenguaje de sus obras un escritor que su obras o poemas orales eran cantadas como obras epicas tradiconales de la epoca ",
"William Shakespeare: Eres muy parecido a William Shakespeare es considerado el escritor más importante en lengua inglesa y uno de los más célebres de la literatura universal"]
for escritores in lista_escritores:
    print("Este es tu escritor. ¿Quieres saberlo?: ")
    respuesta = input("si / no")
    if respuesta == "si":
        print("este seria tu escritor", escritores)
    else:
        print("Gracias por participar XD")
        break
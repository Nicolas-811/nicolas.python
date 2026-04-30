#uso y ejemplo de random

# import random

# num=random.randint(1,10)
# print(num)

# for i in range(num):
#     print("hola nicolas")

# dado=random.randint(1,6)
# print("El dado dio: ", dado)

# crear una tabla de multiplicar
# de 1 a 24, mostrar la tabla

# num=int(input("Ingrese un numero: "))

# for i in range(10):
#     print(num, "x" , i+1 , "=", num*(i+1))
#     print(i)

# import random
# num=random.randint(1,24)
# for i in range(num):
#     print(num, "x", i+1 , "=" , num*(i+1))

# tirar 2 dados y si sale par
# se va a la carcel

import random


# dado1=random.randint(1,6)
# dado2=random.randint(1,6)
# print("dado 1: ", dado1)
# print("dado 2: ", dado2)


# if dado1==dado2:
#     print("¡IRÁS A LA CÁRCEL!")
# else:
#     print("Te salvaste, avanza ")

# se genera un golpe aleatorio entre 10 y 70 
# si el golpe tiene mas de 50 de fuerza, es un golpe critico
# sino, no es muy efectivo

# strike=random.randint(10,70)

# if strike>50:
#     print("golpe critico ", strike)
# else:
#     print("golpe no muy  efectivo ", strike)

#tres personas juegan golf
# cada persona tiene la posibilidad de golpear
# y la distancia varia entre 60 y 190
# mostar el final, el golpe mas fuerte

import random

# nombre1 = input("Ingresa el nombre del jugador 1: ")
# nombre2 = input("Ingresa el nombre del jugador 2: ")
# nombre3 = input("Ingresa el nombre del jugador 3: ")

# jugador1=random.randint(60,190)
# jugador2=random.randint(60,190)
# jugador3=random.randint(60,190)

# print(nombre1 + ": ", jugador1)
# print(nombre2 + ": ", jugador2)
# print(nombre3 + ": ", jugador3)

# if jugador1>jugador2 and jugador1>jugador3:
#     print("El ganador es " + nombre1 + " con un golpe de: ", jugador1)
# elif jugador2>jugador1 and jugador2>jugador3:
#     print("El ganador es " + nombre2 + " con un golpe de: ", jugador2)
# else:
#     print("El ganador es " + nombre3 + " con un golpe de: ", jugador3)


#KILLER INSTINCT

# Dos peleadores se piden al inicio de la pelea
# cada peleador inica con 100 de hp
# se debe hacer una pelea por turnos
# y cada golpe varia entre 7 y 18
# se termina el match cuando uno de los dos 
# tiene su hp menor o igual a 0
# se debe mostrar el ganador final
#BONUS: mostrar la barra de energia de cada peleador

j1=input("ingrese el nombre del jugador 1: ")
j2=input("ingrese el nombre del jugador 2: ")
j1p1_hp=100
j1p2_hp=100
j1p1=random.randint(7,18)
j1p2=random.randint(7,18)
if j1p1>j1p2:
    j1p2_hp-=j1p1
    print(j1, "golpeo a ", j2, "con un golpe de: ", j1p1)
    print(j2, "tiene un golpe de: ", j1p2)
    print(j1, "tiene ", j1p1_hp, "de hp")
    print(j2, "tiene ", j1p2_hp, "de hp")
elif j1p2>j1p1:
    print(j2, "golpeo a ", j1, "con un golpe de: ", j1p2)
    print(j1, "tiene un golpe de: ", j1p1)
    j1p1_hp-=j1p2
    print(j1, "tiene ", j1p1_hp, "de hp")
    print(j2, "tiene ", j1p2_hp, "de hp")
else:
    print("empate, ambos golpearon con la misma fuerza")
    print("ambos jugadores tiene ", j1p1_hp, "de hp")
    print("ambos jugadores tiene ", j1p2_hp, "de hp")





# turno=1
# if turno%2==0:
#     print("Turno uno")
# else:
#     print("Turno dos")










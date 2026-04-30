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

jugador1=random.randint(60,190)
jugador2=random.randint(60,190)
jugador3=random.randint(60,190)

print("jugador 1: ", jugador1)
print("jugador 2: ", jugador2)
print("jugador 3: ", jugador3)

if jugador1>jugador2 and jugador1>jugador3:
    print("El jugador 1 es el ganador con un golpe de: ", jugador1)
elif jugador2>jugador1 and jugador2>jugador3:
    print("El jugador 2 es el ganador con un golpe de: ", jugador2)
else:
    print("El jugador 3 es el ganador con un golpe de: ", jugador3)









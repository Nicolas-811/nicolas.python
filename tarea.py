# Deberás construir un programa que esta diseñado para ayudar en la venta de pasajes. Inicia preguntándote cuántos pasajes deseas vender.
#  Luego, utiliza un proceso organizado (llamado bucle for) para pedirte el precio de cada pasaje por separado. Si ingresas un valor que
#  no es un número, te indica que necesitas proporcionar un valor numérico válido. Al final, mues-tra el monto total que se ha obtenido
#  por la venta de todos los pasajes
# •	Solicita al usuario la cantidad de pasajes a vender.
# •	Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
# •	Dentro del bucle, se solicita al usuario el precio de cada pasaje y se acumula en la variable totalIngresos.
# •	Si el usuario ingresa un valor no numérico para el precio del pasaje, el programa muestra un mensaje y sale del bucle usando break.
# •	Finalmente, se imprime el total de ingresos por la venta de pasajes

# while True:
#     try:
#         pasajes=int(input("Cuantos pasajes desea vender?: "))
#         break
#     except Exception as e:
#         print("solo valores enteros", e)

# total_ingresos=0

# for i in range (pasajes):
#     while True:
#         try:
#             precio=float(input(f"Ingrese el precio del pasaje {i+1}: "))
#             total_ingresos+=precio
#             break

#         except ValueError as e:
#             print("No es un numero valido", e)

# print("el monto total obtenido por la venta es: ", total_ingresos)

# Realiza construcción de un programa que deba realizar lo siguiente: 
# Comienza con la inicialización de variables y solicita al usuario la cantidad de bultos.
# Luego, utiliza un bucle FOR para procesar cada bulto, solicitando el peso al usuario y manejando posibles errores
# (agregar excepciones). Dependiendo del peso ingresado, acumula valores y contadores correspondientes para bultos livianos y normales.
# Finalmente, imprime el total a pagar por bultos livianos y normales, así como la cantidad de bultos en cada categoría

# Una empresa de transporte requiere automatizar sus procesos de cálculo para poder cobrar por la cantidad de paquetes que trae un cliente.
# Para calcular el valor total a cobrar y catalogarlo para envío,  requiere preguntar el peso de cada bulto y determinar el valor según 
# lo siguiente:


# while True:
#     try:
#         cant=int(input("Cuantos bultos son?: "))
#         break
#     except Exception as e:
#         print("solo valores enteros", e)

# bulto_liviano=0
# bulto_normales=0

# for i in range (cant):
#     while True:
#         try:
#             bulto=float(input(f"Ingrese el peso del bulto {i+1}: (en Kg): "))
#             if bulto <=5:
#                 bulto_liviano+=1
#             else:
#                 bulto_normales+=1          
#             break

#         except ValueError as e:
#             print("No es un numero valido", e)


# print(f"bultos livianos: {bulto_liviano*1000}")
# print(f"bultos normales: {bulto_normales*2000}")
# print(f"el total a pagar es: {bulto_liviano*1000+bulto_normales*2000}")


'''Ahora, realiza la siguiente modificación al programa anterior: 
El bucle For, debe ser reemplazado por una sentencia While, que permita ejecutarse mientras la variable “nroBulto”
sea menor o igual a la cantidad de bultos ingresados por el usuario.
Recuerda incluir sentencias de validación'''

while True:
    try:
        cant=int(input("Cuantos bultos son?: "))
        break
    except Exception as e:
        print("solo valores enteros", e)

bulto_liviano=0
bulto_normales=0

nroBulto = 1
while nroBulto <= cant:
    while True:
        try:
            bulto = float(input(f"Ingrese el peso del bulto {nroBulto}: (en Kg): "))
            if bulto <= 5:
                bulto_liviano += 1
            else:
                bulto_normales += 1
            nroBulto += 1
            break

        except ValueError as e:
            print("No es un numero valido", e)


print(f"bultos livianos: {bulto_liviano*1000}")
print(f"bultos normales: {bulto_normales*2000}")
print(f"el total a pagar es: {bulto_liviano*1000+bulto_normales*2000}")

# ''pedir la cantidad de notas al usuario, luego pedir la nota individualmente, calcular el promedio de todas las notas y
# mostrar si aprueba o no''''''
# ''

notas=int(input("ingrese la cantidad de notas: "))
suma=0

for i in range (notas):
    while True:
        try:
            nota=float(input(f"ingrese la nota {i+1}: "))
            suma+=nota
            break
        except ValueError as e:
            print("solo valores decimales. Error: ", e)
promedio=suma/notas
print(f"El promedio es: {promedio}")
if promedio >= 4.0:
    print("¡Aprobado!")
else:
    print("¡Reprobado!")
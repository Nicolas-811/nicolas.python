#ejemplo de while y su uso

# cont=1
# while cont<=3:
#     print(f"contador {cont}")
#     cont+=1


# pin=3535

# code=int(input("ingrese su pin: "))

# while pin!=code:
#     print("Error, intentelo de nuevo")
#     code=int(input("ingrese su pin: "))
# print("PIN CORRECTO")

# USANDO WHILE, PIDA AL USUARIO UN NUMERO
# Y MUESTRE SU TABLA DE MULTIPLICAR HASTA EL 10

numero=int(input("Ingrese un numero: "))
suma=1

while suma<=10:
    print(f"{numero} * {suma} = {numero*suma}")
    suma+=1
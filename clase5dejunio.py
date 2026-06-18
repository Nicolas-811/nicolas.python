# juguetes=["yo-yo", "tetris"]
# def mostrar():
#     c=1
#     for j in juguetes:
#         print(c, ".-", j)
#         c+=1
#     print("."*30)

# def actualizar():               
#     mostrar()
#     print("Que juguete desea actualizar?: ")
#     actualizar=int(input())
#     nuevojuguete=input("Ingrese el nuevo juguete: ")
#     juguetes[actualizar-1]=nuevojuguete

# def eliminar():
#     mostrar()
#     eliminar=int(input("Que juguete desea eliminar?: "))
#     juguetes.pop(eliminar-1)
#     print("Juguete eliminado")

# def agregar():
#     mostrar()
#     ju=input("Ingrese un juguete: ")
#     juguetes.append(ju)
#     print("Juguete agregado")


# def menujuguetes():
#     while True:
#         try:
#             print("1. Agregar juguete")
#             print("2. Eliminar juguete")
#             print("3. Actualizar juguete")
#             print("4. Mostrar juguetes")
#             print("5. Salir")
#             op=int(input("Seleccione una opcion: "))

#             match op:
                
#                 case 2:
#                     eliminar()                
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     print("Saliendo")
#                     break
#                 case _:
#                     print("opcion invalida")
#         except Exception as e:
#             print("Error: ", e)



def validar_lista_numeros():
    while True:
        try:
            entrada: str=input("Ingrese una lista de números enteros separados por espacios: ")

            lista_numeros=[]

            for numero in entrada.split():
                lista_numeros.append(int(numero))

            return lista_numeros
        
        except ValueError as er:
            print("Error: debe ingresar solo numeros enteros", er)

def separar_pares_impares(lista):

    pares=[]
    impares=[]

    for numero in lista:

        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

numeros=validar_lista_numeros()

pares, impares= separar_pares_impares(numeros)

print("numeros pares: ", pares)
print("numeros impares: ", impares)

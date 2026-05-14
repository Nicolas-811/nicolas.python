#ejemplo y uso de try except
# while True:
#     try:
#         numero=int(input("ingrese un numero: "))
#         break
#     except:
#         print("Solo numeros enteros")


# sacar promedio
# print("ingrese tres notas")
# total=0

# for i in range (3):
#     while True:
#         try:
#             n=float(input(f"ingrese la nota {i+1}: "))
#             break
#         except:
#             print("se debe ingresar numeros decimales")

#             prom=total/3
# print(f"El promedio es {prom}")



# while True:
#     try:
#         num=int(input("ingrese un numero: "))
#         break
#     except ValueError:
#         print("Solo numeros enteros")


# op=0
# total=0
# while op!=4:
#     print("1.- PC $500.000")
#     print("2.- LGTV 55 pulgadas $450.000")
#     print("3.- Microondas Mademsa $100.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     try:
#         op=int(input())
#     except ValueError:
#         print("Solo numeros enteros")
#         continue
#     match op:
#         case 1:
#             print("El total a pagar es ",500000*1.19 )
#             total+=500000*1.19
#         case 2:
#             print("El total a pagar es ",450000*1.19 )
#             total+=450000*1.19
#         case 3:
#             print("El total a pagar es ",100000*1.19 )
#             total+=100000*1.19
#         case 4:
#             print("Saliendo")
#             print("El total a pagar es", total)
#         case _:
#             print("Opción inválida")


op=0
total=0
while op!=4:
    try:
        print("1.- PC $500.000")
        print("2.- LGTV 55 pulgadas $450.000")
        print("3.- Microondas Mademsa $100.000")
        print("4.- Salir")
        print("Seleccione una opcion")
        op=int(input())
    except ValueError as e:
        print("Error", e)
        print("Solo se aceptan numeros enteros")
    match op:
        case 1:
            print("El total a pagar es ",500000*1.19 )
            total+=500000*1.19
        case 2:
            print("El total a pagar es ",450000*1.19 )
            total+=450000*1.19
        case 3:
            print("El total a pagar es ",100000*1.19 )
            total+=100000*1.19
        case 4:
            print("Saliendo")
            print("El total a pagar es", total)
        case _:
            print("Opción inválida")

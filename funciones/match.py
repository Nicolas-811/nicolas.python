#explicacion y uso de match

op=0
total=0
while op !=4:

    print("1.- PC $800000")
    print("2.- TV $450000")
    print("3.- Parlante $90000")
    print("4.- Saliendo")
    print("Seleccione una opcion: ")
    op=int(input())
    match op:
        
        case 1:
            print("Tiene que pagar: ", 800000*1.19)
            total+=800000*1.19
            print(total)
        case 2:
            print("Tiene que pagar: ", 450000*1.19)
            total+=450000*1.19
        case 3:
            print("tiene que pagar: ", 90000*1.19)
            total+=90000*1.19
        case 4:
            print("Saliendo")
            print(f"El total a pagar con IVA es: ", total)
        case _:
            print("opcion invalida")

print("Fin del programa")
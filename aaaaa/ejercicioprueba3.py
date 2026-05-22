#Registro de juegos - Uso de try except obligatorio

# def obtener_nombre():
#     while True:
#         nombre=input("nombre del juego: ")
#         if len(nombre)>=5 and " " not in nombre:
#             return nombre.upper()
#         print("error: minimo 5 caracteres sin espacios")

# def obtener_precio():
#     while True:
#         try:
#             precio=int(input("precio del juego: "))
#             if precio>0:
#                 return precio
#             print("error: debe ser un numero positivo")
#         except ValueError:
#             print("error: debe ingresar un numero entero")

# def obtener_clasificacion():
#     while True:
#         clasificacion=input("clasificacion por edad (E, +12, M): ").upper()
#         if clasificacion in ["E", "+12", "M"]:
#             return clasificacion
#         print("error: ingrese E, +12 o M")

# def clasificar_precio(precio):
#     if 20000<=precio<40000:
#         return "Indie"
#     elif precio>=40000:
#         return "Estudio"
#     return None

# # Programa principal
# contadores={"Indie":0, "Estudio":0, "E":0, "+12":0, "M":0}

# print("Registro de Juegos\n")

# while True:
#     try:
#         cantidad=int(input("cuantos juegos desea registrar?: "))
#         if cantidad>0:
#             break
#         print("error: ingrese un numero mayor a cero")
#     except ValueError:
#         print("error: debe ingresar un numero entero")

# for i in range(cantidad):
#     print(f"\n--- Juego {i+1} ---")
#     nombre=obtener_nombre()
#     precio=obtener_precio()
#     categoria=clasificar_precio(precio)
    
#     if not categoria:
#         print("el precio no entra en ninguna categoria")
#         continue
    
#     clasificacion=obtener_clasificacion()
    
#     contadores[categoria]+=1
#     contadores[clasificacion]+=1
#     print(f"✓ {nombre} - ${precio} - {categoria} - {clasificacion}")

# # Resumen final
# print("\n=== RESUMEN FINAL ===")
# print(f"Juegos Indie: {contadores['Indie']}")
# print(f"Juegos Estudio: {contadores['Estudio']}")
# print(f"Clasificacion E: {contadores['E']}")
# print(f"Clasificacion +12: {contadores['+12']}")
# print(f"Clasificacion M: {contadores['M']}")


    
#EJERCICIO2

deuda=100000

while True:
    print("Menu")
    print("1. pago tarjeta")
    print("2. simulacion de compras")
    print("3. salir")
    opcion=input("ingrese una opcion: ")

    if opcion =="1":
        try:
            pago=int(input("ingrese monto a pagar: "))
            if pago<0:
                print("el monto no puede ser negativo")
            elif pago>deuda:
                print("el pago no puede superar la deuda")
            else:
                deuda-=pago    
                print("pago realizado correctamente")
                print("deuda actual: ", deuda)
        except:
            print("error, debe ingresar numeros")

    elif opcion =="2":
        while True:
            try:
                compra=int(input("ingrese monto de compra (0 para salir)"))
                if compra ==0:
                    break
                elif compra<0:
                    print("monto invalido")
                else:
                    deuda +=compra
                    print("compra realizada")
                    print("deuda actual: ", deuda)
            except:
                print("error, ingrese numeros")

    elif opcion =="3":
        print("programa finalizado")
        break
    else:
        print("opcion incorrecta")


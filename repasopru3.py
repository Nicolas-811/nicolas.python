#op=0

# while op!=3:
#     try:
#         print("selecciona una opcion")
#         print("1.-chocolate")
#         print("2.-mocca")
#         print("3.-salir")
#         op=int(input())
        
        
#     except ValueError as e:
#         print("solo numeros enteros")
#         print("error: ", e)
#     else:
#         print("bien hecho")











#hacer un menu, donde los camiones chicos sean de 3 toneladas hacia abajo, el mediano entre 4 y 8 toneladas y mas de 9 toneladas es camion
#grand; solo mostrar numeros enteros positivos

# op=0
# camion_chico=0
# camion_mediano=0
# camion_grande=0
# suma=0

# while True:
#     try:
#         print("selecciona una opcion")
#         print("1.-ingresar camion")
#         print("2.-mostrar totales")
#         print("3.-mostrar cantidad de camiones")
#         print("4.-mostrar capacidad total de camiones")
#         print("5.-ingrese la marca del camion")
#         print("6.-salir")
#         op=int(input())
#         match op:
#             case 1:
#                 while True:
#                     try:
#                         peso=int(input("ingrese la capacidad del camion: "))
#                         if peso > 0:
             
#                             suma+=peso
                            
#                             if 0 < peso <= 3:
#                                 print("El camion es chico")
#                                 camion_chico+=1
#                             elif 4 <= peso <= 8:
#                                 print("El camion es mediano")
#                                 camion_mediano+=1
#                             else:
#                                 print("El camion es grande")
#                                 camion_grande+=1
#                             break
#                         else:
#                             print("Solo numeros enteros positivos")
#                     except ValueError as er:
#                         print("solo numeros enteros positivos", er)
#                         break
#             case 2:
#                 print(f"El total de camiones chicos son: {camion_chico}")
#                 print(f"El total de camiones medianos son: {camion_mediano}")  
#                 print(f"El total de camiones grandes son: {camion_grande}")
#             case 3:
#                 print(f"cantidad de camiones totales es: {camion_chico+camion_mediano+camion_grande}")      
#             case 4:
#                 print(f"La capacidad total de los camiones es: {suma}")
#             case 5:
#                 marca=input("ingrese la marca del camion: ")
#                 if 3<= len(marca)<=8:
#                     print("marca valida")
#                 else:
#                     print("marca invalida, debe ser entre 3 a 8 caracteres")
#             case 6:
#                 print("Saliendo del sistema")
#                 break
#             case _:
#                 print("Opcion invalida")
                
#     except ValueError as er:
#         print(f"Error {er}")
                   
            
        






# una galeria de arte tiene 100 espacios para cuadros
# preguntar cuantas personas vinieron a ver cuadros
# al salir de la galeria , preguntar a cada persona, cuantos cuadros vio, por cada persona        
# clasificar los cuadros vistos y no vistos




    
        
total_cuadros=100
cant_personas=int(input("cuantas personas vinieron a ver cuadros?: "))

for i in range(cant_personas):
    print(f"cantidad de persona {i+1}")
    vistos = int(input("cuantos cuadros vio?: "))
    if vistos > total_cuadros:
        print(f"error, la galeria solo tiene {total_cuadros} cuadros")
    elif vistos < 0:
        print("error, no puedes ingresar numeros negativos")
    else:
        no_vistos = total_cuadros - vistos
        print(f"cuadros vistos: {vistos}")
        print(f"cuadros no vistos: {no_vistos}")

        


while true
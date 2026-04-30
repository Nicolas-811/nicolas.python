def calculadora():
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese otro numero: "))
    op=0
    while op !=4:
        print("1.- Suma ")
        print("2.- Resta ")
        print("3.- Multiplicacion ")
        print("4.- Division ")
        print("5.- Salir")
        print("Seleccione una opcion")
        op=int(input("Igrese la operacion que desea realizar: "))
        match op:
            case 1:
                print("El resultado es: ", num1+num2)
            case 2:
                print("El resultado es: ", num1-num2)
            case 3:
                print("El resultado es: ", num1*num2)
            case 4:
                print("El resultado es: ", num1/num2)
            case 5:
                print("Saliendo del programa")



def ClaveShazam():
    clave="shazam"
    palabra=input("ingrese la clave: ").lower()
    if clave==palabra:
        print("la contraseña es correcta")
    else:
        print("la contraseña es incorrecta")



def palabrasecreta():
    palabra_secreta="python"
    intentos=3
    for i in range(intentos):
        juego=input("ingrese la palabra secreta: ").lower()
        if juego=="python":
            print("correcto, Haz ganado")
            break
        elif juego!="python":
            print("Ha perdido, intentelo nuevamente")


#votatoon

toon1=input("ingrese el toon 1: ")
toon2=input("ingrese el toon 2: ")

v1=0
v2=0

cant=int(input("cuantos votantes son? "))

while cant>0:
    voto=int(input(f"Por quien votara? 1.- {tonn1} 2.-{toon2}: "))
    if voto==1:
        v1+=
    elif voto==2:
        v2+=1
    else:
        print("Voto nulo")
    cant-=

if v1>v2:
    print(f"Ganó {toon1} con {v1} votos ")
elif v1<v2:
    print(f"Ganó {toon2} con {v2} votos ")
else:
    print("Es un empate")

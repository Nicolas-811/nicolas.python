#1)Crear un programa que pregunte al usuario su nombre, edad y comida favorita.
#Luego, imprima un mensaje que contenga esa información
#Ejemplo: "Hola, mi nombre es [nombre], tengo [edad] años y mi comida favorita es [comida favorita]."

# nombre=input("ingrese su nombre: ")
# edad=int(input("ingrese su edad: "))
# comida_favorita=input("ingrese su comida favorita: ")
# print("su nombre es ", nombre, "su edad es ", edad, "y su comida favorita es ", comida_favorita)

#2)Crear un programa que pregunte al usuario por un número, y luego muestre
#el numero anterior, el numero ingresado, y el numero siguiente
#Ejemplo: "Números: 3, 4, 5"

# numero=int(input("ingrese un numero: "))
# antecesor=numero-1
# sucesor=numero+1
# print("el numero que ingreso es: ", numero, "su antecesor es: ", antecesor, "y el sucesor es: ", sucesor)


#3)Crear un programa que pregunte por cantidad de dinero y si tiene receta médica.
#Si tiene el dinero suficiente y tiene receta médica, el medicamento se puede vender(Cuesta $10mil pesos).
# cantidad_dinero=int(input("Cuanto saldo tiene disponible ? "))
# receta_medica=input("Tiene receta medica ? ")
# if cantidad_dinero>=10000 and receta_medica=="si":
#     print("Puede realizar la compra")
# elif cantidad_dinero<10000 and receta_medica=="no":
#     print("No le alcanza y ademas no tiene la receta")
# else:
#     print("Vuelva cuando tenga el dinero suficiente y la receta medica")


#4)Crear un programa que pregunte al usuario su edad y muestre por pantalla todos
#los años que ha cumplido (desde 1 hasta su edad)
# edad=int(input("ingrese su edad: "))
# for i in range(edad):
#     print("usted ha cumplido: ", i+1, "años hasta la fecha")

#5)Crea un juego que se trate de adivinar una palabra secreta. El usuario tiene 3 intentos.
#el programa debe informar cuando el usuario lo hace mal o bien.
#la palabra secreta es "python"
#Puedes usar .lower() para convertir la respuesta del usuario a minúsculas
#ejemplo: respuesta=PYTHON     respuesta.lower()        respuesta=python
# respuesta= input("Adivina la palabra").lower()         respuesta=python 
palabra_secreta="python"
intentos=3
for i in range(intentos):
    juego=input("ingrese la palabra secreta: ").lower()
    if juego=="python":
        print("correcto, Haz ganado")
        break
    elif juego!="python":
        print("Ha perdido, intentelo nuevamente")



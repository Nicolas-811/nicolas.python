import random, time
# num=random.randint(1,9)

# while abs(-3)!=num:
#     print(num)
#     time.sleep(1)
#     num=random.randint(1,9)


# n1=int(input("ingrese el valor del limite inferior: "))
# n2=int(input("ingrese el valor del limite superior: "))
# #VALIDAR QUE EL LIMITE SUPERIOR SEA MAYOR QUE EL LIMITE INFERIOR
# #HAY UN LIMITE QUE ROMPE EL DESEO
# while n1>n2:
#     print("El limite superior debe ser mayor que el limite inferior")
#     n1=int(input("ingrese el valor del limite inferior: "))
#     n2=int(input("ingrese el valor del limite superior: "))
# num=random.randint(n1,n2)
# print("El numero aleatorio generado es:", num)

#Realizar la clasificacion de peces y generar una cantidad aleatoria de captura de peces
#entre 10 y 20, capturar peces y clasificarlos por su peso, para saber como se venderan
#si es de 800 gramos o menos, va en lata
#si es de 801 o mas, a la plancha y cuantos quedaron para embasar en lata

# total_peces=random.randint(10,20)
# lata=0
# plancha=0
# for i in range(total_peces):
#     peso=random.randint(500,3000)
#     print("Peso del pez capturado: ", peso)
#     if peso<=800:
#         lata=lata+1
#     else:
#         plancha=plancha+1
# print("Cantidad de peces para lata: ", lata)
# print("Cantidad de peces para plancha: ", plancha)

#Fabrica de enlatados 
#se necesita hacer el algoritmo de productos enlatados, se debe consultar el peso del proodcuto (en gramos), (solo valores positivos)
#el porcentaje de sodio en el (solo valores entre 1 y 100)
#si se vendera nacional o internacionalmente
#considerar los criterios de la siguente tabla

#menos de 500 gramos, lata normal
#de 501 hasta 1500 gramos, lata grande
#si el sodio es menos de 5%, lata queda igual
#si es entre 5% y 8%, lata especial
#si tiene 9% o mas, lata acorazada
#a las latas internacionales, se les debe pegar un sticker de validacion sanitaria

# peso=random.randint(100,2000)
# sodio=random.randint(1,100)
# nacionalidad=input("¿El producto se vendera nacional o internacionalmente? (nacional/internacional): ")
# while nacionalidad!="nacional" and nacionalidad!="internacional":
#     print("Debe ingresar 'nacional' o 'internacional'")
#     nacionalidad=input("¿El producto se vendera nacional o internacionalmente? (nacional/internacional): ")
# time.sleep(1)
# if peso<=500:
#     lata="lata normal"
# elif peso<=1500:
#     lata="lata grande"
# else:
#     lata="lata extra grande"

# if sodio<5:
#     lata=lata
# elif sodio<=8:
#     lata=lata+" especial"
# else:
#     lata=lata+" acorazada"

# if nacionalidad=="internacional":
#     lata=lata+" con sticker de validacion sanitaria"
# print("El tipo de lata que se necesita es:", lata)


#ó

peso=int(input("Ingrese el peso del producto en gramos: "))
sodio=int(input("Ingrese el porcentaje de sodio en el producto (1-100): "))
mercado=input("¿El producto se vendera nacional o internacionalmente? (nacional/internacional): ")

if peso<=500:
    lata="lata normal"
elif peso<=1500:
    lata="lata grande"
else:
    lata="lata extra grande"

if sodio<5:
    lata=lata
elif sodio<=8:
    lata=lata+" especial"
else:
    lata=lata+" acorazada"
if mercado=="internacional":
    lata=lata+" con sticker de validacion sanitaria"

if sodio<5:
    sod=""
elif sodio<=8:
    sod="especial"
else:
    sod="acorazada" 

if mercado==1:
    stiker=""
else:
    stiker="con sticker de validacion sanitaria"
print("El tipo de lata que se necesita es:", lata, "y el tipo de sodio es:", sod, stiker)





# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es: {n1+n2}")

# suma()

#SIN ARGUMENTO Y CON RETORNO
# def sumaRet():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     return n1+n2

# print(sumaRet())


# def sumaRet():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     return n1+n2
# res=sumaRet()
# print("El resultado es ", res)


# def saludaME(name):
#     print("Hola ", name)

# saludaME("Thor")

# def mitadprecio(precio):
#     print("El precio es ", precio/2)

# pre=int(input("Ingrese el precio: "))
# mitadprecio(pre)

#con argumento y con retorno

# def sumaRetArg(n1,n2):
#     return n1+n1
# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese otro numero: "))

# print("El resultado de la suma es: ", sumaRetArg(num1, num2))





#crear una calculadora para las 4 operaciones basicas y usando funciones
#estas deben tener argument y return

def sumar(a, b):
    return a+b

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))

print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opcion=int(input("Seleccione una opcion: "))

if opcion == 1:
    print("El resultado de la suma es: ", sumar(num1, num2))

elif opcion == 2:
    print("El resultado de la resta es: ", restar(num1, num2))

elif opcion == 3:
    print("El resultado de la multiplicacion es: ", multiplicar(num1, num2))

elif opcion == 4:
    print("El resultado de la division es: ", dividir(num1, num2))

else:
    print("opcion invalida")




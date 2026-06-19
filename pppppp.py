# series_famosas = {
#     "Breaking Bad": "Drama",
#     "Game of Thrones": "Fantasía",
#     "Stranger Things": "Ciencia ficción",
#     "La Casa de Papel": "Acción",
#     "Friends": "Comedia"
# }

# for serie, genero in series_famosas.items():
#     print(f"Serie: {serie} - Género: {genero}")


# Lista de comidas típicas de Chile
# comidas_chilenas = [
#     "Empanada de pino",
#     "Pastel de choclo",
#     "Cazuela",
#     "Curanto",
#     "Completo"
# ]

# Diccionario de comidas típicas de Chile
# comidas_info = {
#     "Empanada de pino": "Carne, cebolla, huevo y aceituna",
#     "Pastel de choclo": "Preparado con choclo molido y carne",
#     "Cazuela": "Caldo con carne, verduras y papas",
#     "Curanto": "Mariscos, carnes y papas cocidos",
#     "Completo": "Hot dog con tomate, palta y mayonesa"
# }

# print("Lista de comidas:")
# for comida in comidas_chilenas:
#     print("-", comida)

# print("Diccionario de comidas:")
# for comida, descripcion in comidas_info.items():
#     print(f"{comida}: {descripcion}")


# frutas = {
#     "manzana": "Roja y dulce",
#     "platano": "Amarillo y rico en potasio",
#     "naranja": "Cítrica y rica en vitamina C",
#     "uva": "Pequeña y jugosa",
#     "frutilla": "Roja y dulce"
# }

# lista_frutas = list(frutas.keys())

# print("Diccionario:", frutas)
# print("Lista:", lista_frutas)



# postres = {
#     "Torta de mil hojas": "Postre tradicional con capas de masa y manjar",
#     "Leche asada": "Postre preparado con leche, huevos y azúcar",
#     "Mote con huesillo": "Postre típico chileno con duraznos deshidratados",
#     "Brazo de reina": "Bizcocho enrollado relleno con manjar",
#     "Helado": "Postre frío de distintos sabores"
# }

# print(postres)

#"[ corchetes lista]"
#"{llaves diccionario}"

## Crear un gestor de pacientes
'''crear al gestor de pacientes en un centro medico
Para poner el nombre se debe validar que no este vacio 
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
FOnasa 54%
Isapre 27%
Fodesa 12,5%

'''

# pacientes = [
#     {
#         "nombre": "Aquiles Baeza",
#         "prevision": "Fonasa",
#         "temperatura": 34.6,
#         "grave": False
#     }
# ]

# def validarEstado(temp):
#     return temp > 39

# def mostrarPacientes():
#     if len(pacientes) == 0:
#         print("No hay pacientes.")
#     else:
#         for i, p in enumerate(pacientes, start=1):
#             print(f"{i}. {p}")

# def agregarPaciente():

#     while True:
#         nombre = input("Ingrese nombre: ").strip()

#         if len(nombre) > 8:
#             break

#         print("El nombre debe tener más de 8 caracteres.")

#     while True:
#         prevision = input("Ingrese previsión (Fonasa, Isapre o Fodesa): ").capitalize()

#         if prevision in ["Fonasa", "Isapre", "Fodesa"]:
#             break

#         print("Previsión inválida")

#     temperatura = float(input("Ingrese temperatura: "))

#     pacientes.append({
#         "nombre": nombre,
#         "prevision": prevision,
#         "temperatura": temperatura,
#         "grave": validarEstado(temperatura)
#     })

#     print("Paciente agregado correctamente")

# def eliminarPaciente():
#     mostrarPacientes()

#     paciente = int(input("¿Qué paciente desea eliminar?: "))

#     pacientes.pop(paciente - 1)

#     print("Paciente eliminado")

# def tomarTemperatura():

#     mostrarPacientes()

#     paciente = int(input("Seleccione paciente: "))

#     temperatura = float(input("Nueva temperatura: "))

#     pacientes[paciente - 1]["temperatura"] = temperatura
#     pacientes[paciente - 1]["grave"] = validarEstado(temperatura)

#     print("Temperatura actualizada")

# def cobrarAtencion():

#     mostrarPacientes()

#     paciente = int(input("¿Qué paciente va a pagar?: "))

#     prevision = pacientes[paciente - 1]["prevision"]

#     valor = 25000

#     match prevision:
#         case "Fonasa":
#             total = valor * 0.46
#         case "Isapre":
#             total = valor * 0.73
#         case "Fodesa":
#             total = valor * 0.875

#     print(f"Total a pagar: ", total)

# while True:

#     try:

#         print("CENTRO MÉDICO")
#         print("1. Agregar paciente")
#         print("2. Eliminar paciente")
#         print("3. Tomar temperatura")
#         print("4. Cobrar atención")
#         print("5. Mostrar pacientes")
#         print("6. Salir")

#         op = int(input("Seleccione una opción: "))

#         match op:

#             case 1:
#                 agregarPaciente()

#             case 2:
#                 eliminarPaciente()

#             case 3:
#                 tomarTemperatura()

#             case 4:
#                 cobrarAtencion()

#             case 5:
#                 mostrarPacientes()

#             case 6:
#                 print("Saliendo...")
#                 break

#             case _:
#                 print("Opción inválida.")

#     except Exception as e:
#         print("Error:", e)









notas=[4.6, 7.0, 3.4, 6.6, 3.9]

#crear una funcion para poder pasarle la lista
#como parametro y mostrar el promedio
#mostrar si aprueba o no

def promedio_notas(lista):
    return sum(lista) / len(lista)

promedio=promedio_notas(notas)

print("promedio:", promedio)

if promedio>= 4.0:
    print("Aprobó")
else:
    print("Reprobó")

#"O"

def calcularprom(n):
    total=0
    for uwu in n:
        total+=uwu
    prom=total/len(n)
    return round(prom, 1)
print("El promedio es: ", calcularprom(notas))

print(max(notas))
print(min(notas))




peliculas=[
    {"titulo": "inception", "director": "christopher nolan",
     "genero": "ciencia ficcion", "año": 2010},
    {"titulo": "jurassic park", "director": "steven spilberg",
     "genero": "ciencia ficcion", "año": 1993},
    {"titulo": "seven", "director": "david fincher",
     "genero": "thiller", "año": 1997},
]






# crear un gestor de peliculas
# el titulo debe tener mas de 2 caracteres
# el año debe ser superior a 1960 y debe ser inferior al año actual
# el director debe tener nombre y apellido
# mostrar el siguiente menu

'''
1.ingresar pelicula
2.quitar pelicula
3.actualizar pelicula
4.mostrar pelicula
5.mostrar solo los titulos
6. ordenar por año(decreciente)
7.salir
'''

peliculas = [
    {"titulo": "Titanic", "anio": 1997, "director": "James Cameron"}
]

# Validar título
def validarTitulo(titulo):
    return len(titulo) > 2

# Validar año
def validarAnio(anio):
    return anio > 1960 and anio <= 2025

# Validar director
def validarDirector(director):
    return len(director.split()) >= 2

# Mostrar películas
def mostrarPeliculas():
    if len(peliculas) == 0:
        print("No hay películas registradas")
    else:
        for i, p in enumerate(peliculas, start=1):
            print(f"{i}. {p}")

# Ingresar película
def agregarPelicula():
    titulo = input("Ingrese título: ")

    if not validarTitulo(titulo):
        print("Título inválido")
        return

    anio = int(input("Ingrese año: "))

    if not validarAnio(anio):
        print("Año inválido")
        return

    director = input("Ingrese director: ")

    if not validarDirector(director):
        print("Debe ingresar nombre y apellido")
        return

    peliculas.append({
        "titulo": titulo,
        "anio": anio,
        "director": director
    })

    print("Película agregada")

# Eliminar película
def eliminarPelicula():
    mostrarPeliculas()
    pos = int(input("Número de película a eliminar: "))
    peliculas.pop(pos - 1)

# Actualizar película
def actualizarPelicula():
    mostrarPeliculas()
    pos = int(input("Número de película a actualizar: "))

    peliculas[pos-1]["titulo"] = input("Nuevo título: ")
    peliculas[pos-1]["anio"] = int(input("Nuevo año: "))
    peliculas[pos-1]["director"] = input("Nuevo director: ")

    print("Película actualizada")

# Mostrar solo títulos
def mostrarTitulos():
    for p in peliculas:
        print(p["titulo"])

# Ordenar por año descendente
def ordenarAnio():
    peliculas.sort(key=lambda x: x["anio"], reverse=True)

    print("Películas ordenadas")

# Menú
while True:
    print("1. Ingresar película")
    print("2. Quitar película")
    print("3. Actualizar película")
    print("4. Mostrar películas")
    print("5. Mostrar solo títulos")
    print("6. Ordenar por año (decreciente)")
    print("7. Salir")

    op = int(input("Seleccione una opción: "))

    match op:
        case 1:
            agregarPelicula()
        case 2:
            eliminarPelicula()
        case 3:
            actualizarPelicula()
        case 4:
            mostrarPeliculas()
        case 5:
            mostrarTitulos()
        case 6:
            ordenarAnio()
        case 7:
            print("Saliendo...")
            break
        case _:
            print("Opción inválida")
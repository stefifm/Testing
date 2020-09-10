import random

class Participantes:
    def __init__(self, nom, conti, rank):
        self.nombre = nom
        self.continente = conti
        self.ranking = rank

class Fixture:
    def __init__(self, equipo1, punt1, equipo2, punt2):
        self.equipo1 = equipo1
        self.punto1 = punt1
        self.equipo2 = equipo2
        self.punto2 = punt2


def to_string(participantes):
    resultado = " "
    resultado += "El participante es: "
    resultado += " - Nombre: " + participantes.nombre
    resultado += " - Continente: " + str(participantes.continente)
    resultado += " - Ranking: " + str(participantes.ranking)
    return resultado

def to_string2(fixture):
    res = " "
    res += "Fixture..."
    res += "Equipo 1: " + fixture.equipo1
    res += "- Puntos del equipo 1: " + str(fixture.punto1)
    res += "\nVS "
    res += "Equipo 2: " + fixture.equipo2
    res += "- Puntos del equipo 2: " + str(fixture.punto2)
    res += "\n"

def mostrar_participantes(participantes):
    for i in range(len(participantes)):
        #muestra cada participante invocando a la función to_string
        print(to_string(participantes[i]))

def mostrar_fixture(fixture):
    for i in range(len(fixture)):
        print(to_string2(fixture[i]))

def orden_sort(participantes):
    #algoritmo de selección directa
    n = len(participantes)
    for i in range(n-1):
        for j in range(i+1, n):
            if participantes[i].ranking > participantes[j].ranking:
                participantes[i], participantes[j] = participantes[j], participantes[i]
    return participantes

def validar_rango(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input("Ingrese un valor entre " + str(inf) +
                          " y " + str(sup) + ": "))
        if n < inf or n > sup:
            print("Error")
    return n

def validar(inf, sup):
    n = inf
    while n <= inf or n < sup or n > sup:
        n = int(input("Cargue la cantidad de participantes: "))
        if n <= inf or n < sup or n > sup:
            print("Error. Ingrese un número que no sea cero y no sea menor o mayor a 16.")
    return n

def linear_search(nom, nombre):
    for i in range(nom):
        if nombre == nom[i]:
            return i
        return -1

def validar_nombre(participantes):
    nom = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express")
    print("Lista de los equipos participantes:",nom)
    for i in range(len(participantes)):
        nombre = input("Ingrese el nombre del equipo: ")
        while linear_search(nom, nombre) != -1:
            nombre = input("Ese nombre ya existe. Ingrese lo que están en la lista: ")
    return nombre



def cargar_vector(participantes):
    for i in range(len(participantes)):
        # cargar datos de los participantes
        nombre = validar_nombre(participantes)
        continente = validar_rango(0, 4)
        ranking = validar_rango(1, 50)
        # crear el participante
        a = Participantes(nombre, continente, ranking)
        # grabar en el vector
        participantes[i] = a
    return participantes

def estadistica_continente(participantes):
    n = len(participantes)
    conteo = [0] * n
    for i in range(n):
        pos = participantes[i].continente
        conteo[pos] += 1
    return conteo

def estadistica_promedio_puntos(participantes):
    suma = 0
    cant = len(participantes)
    promedio = 0
    for i in range(len(participantes)):
        suma += participantes[i].punto1 + participantes[i].punto2
    if cant != 0:
        promedio = round(suma / cant, 2)
    return promedio


def vector_automatico(participantes):
    nom = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express")
    for i in range(len(participantes)):
        nombre = random.choice(nom)
        continente = random.randint(0, 4)
        ranking = random.randint(1, 50)
        part = Participantes(nombre, continente, ranking)
        participantes[i] = part
    return participantes


def vec_fixture(participantes):
    n = len(participantes) // 2
    posicion = len(participantes) - 1
    c = 0
    for i in range(n):
        equipo1 = participantes[i].nombre
        punto1 = random.randint(100, 600)
        equipo2 = participantes[posicion-c].nombre
        punto2 = random.randint(100, 600)
        c += 1
        b = Fixture(equipo1, punto1 ,equipo2, punto2)
        participantes[i] = b
    return participantes

# def mensaje_cruce(fixture):
#     print("Enfrentamientos")
#     n = len(fixture)//2
#     posicion = len(fixture) - 1
#     c = 0
#     cruces = " "
#     for i in range(n):
#         cruces += str(fixture[i].equipo1)+str(fixture[i].puntos1)+" vs " + \
#                   str(fixture[
#                                                             posicion-c].equipo2)
#         cruces += "\n"
#         c += 1
#     return cruces
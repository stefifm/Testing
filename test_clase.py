import random

class Participantes:
    def __init__(self, nom, conti, rank):
        self.nombre = nom
        self.continente = conti
        self.ranking = rank

class Fixture:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.punto1 = random.randint(100, 600)
        self.equipo2 = equipo2
        self.punto2 = random.randint(100, 600)


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


def vector_automatico(participantes):
    nom = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express")
    for i in range(len(participantes)):
        nombre = random.choice(nom)
        continente = random.randint(0, 4)
        ranking = random.randint(1, 50)
        p = Participantes(nombre, continente, ranking)
        participantes[i] = p
    return participantes



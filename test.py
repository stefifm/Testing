import random
#Primera parte: carga del vector participantes

#Primer paso: definir la clase

class Participantes:
    def __init__(self, nom, conti, rank):
        self.nombre = nom
        self.continente = conti
        self.ranking = rank

#segunda clase, Fixture

class Fixture:
    def __init__(self, team1, punt1,team2, punt2):
        self.equipo1 = team1
        self.puntos1 = punt1
        self.equipo2 = team2
        self.puntos2 = punt2



def to_string(participantes):
    r = " "
    r += "Nombre: " + participantes.nombre
    r += " Continente: " + str(participantes.continente)
    r += " Ranking: " + str(participantes.ranking)
    r += "\n"
    return r


#Funciones para la carga
#Carga automática para probar

def carga_automatica(participantes):
    nom = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express")
    for i in range(len(participantes)):
        nombre = random.choice(nom)
        continente = random.randint(0, 4)
        ranking = random.randint(1, 50)
        p1 = Participantes(nombre, continente, ranking)
        participantes[i] = p1
    return participantes

def orden_sort(participantes):
    #algoritmo de selección directa
    n = len(participantes)
    for i in range(n-1):
        for j in range(i+1, n):
            if participantes[i].ranking > participantes[j].ranking:
                participantes[i], participantes[j] = participantes[j], participantes[i]
    return participantes

def mostrar_participantes(participantes):
    for i in range(len(participantes)):
        print(to_string(participantes[i]))

#Parte 2: Genera los cruces de octavos
def fixture(participantes):
    n = len(participantes) // 2
    posicion = len(participantes) - 1
    c = 0

    for i in range(n):
        equipo1 = participantes[i].nombre
        equipo2 = participantes[posicion-c].nombre
        puntos1 = random.randint(100, 600)
        puntos2 = random.randint(100, 600)
        c += 1
        f = Fixture(equipo1, puntos1, equipo2, puntos2)
        print(f.equipo1, f.puntos1, "vs", f.equipo2, f.puntos2)

#La parte más difícil, los cuartos de final
def ganadores(fixture):
    ganadores = [0] * len(fixture)
    for i in range(len(fixture)):
        if fixture[i].puntos1 > fixture[i].puntos2:
            ganadores = fixture[i].nombre
        else:
            ganadores = fixture[i].nombre
    return ganadores

def cuartos(ganadores):
    n = len(ganadores) // 2
    posicion = len(ganadores) - 1
    c = 0
    for i in range(n):
        team1 = ganadores[i].nombre
        team2 = ganadores[posicion - c].nombre
        print(team1,"vs", team2)
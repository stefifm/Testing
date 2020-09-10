import participantes

print("Programa principal del TP3")




def principal():
    n = 16
    competidores = []

    print("Lista de participantes que estarán en competencia\n")

    lista_participantes = ["Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express"]

    for i in range(len(lista_participantes)):
        print(lista_participantes[i])

    print("\nHora de cargar los participantes en los arreglos\n")
    opcion = int(input("1 para hacer la carga manual. 2 para carga "
                       "automática: "))
    if opcion == 1:
        participantes.carga_manual(competidores)
    else:
        participantes.carga_automatica(competidores)

    print("\nOrdenar y mostrar los competidores\n")
    participantes.orden_sort(competidores)
    participantes.mostrar_participantes(competidores)

    print("Estádistica cantidad de participantes por continente\n")
    participantes.estadistica_continente(competidores)

    print("\n Intento de octavos\n")
    participantes.fixture(competidores)

    print("\nEstadística promedio de puntos en octavos")
    participantes.estadistica_promedio_ronda(competidores)

    print("\nintento de cuartos\n")
    cuartos = participantes.ganador(competidores)
    participantes.fixture(cuartos)
    print("\nEstadística promedio de puntos en cuartos:")
    participantes.estadistica_promedio_ronda(cuartos)



    print("\nIntento de semifinales\n")
    semis = participantes.ganador(cuartos)
    participantes.fixture(semis)
    print("\nEstadística promedio de puntos en semifinales:")
    participantes.estadistica_promedio_ronda(semis)

    print("\nIntento de final \n")
    final = participantes.final(semis)
    participantes.fixture(final)
    primero, segundo = participantes.top2(final)
    print("\nCampeón:",participantes.to_string(primero))
    print("Subcampeón:",participantes.to_string(segundo))

    print("\n Intento de tercer puesto\n")
    tercer = participantes.tercer(semis)
    participantes.fixture(tercer)
    tercer_puesto = participantes.tercero(tercer)
    print("\nTercer puesto:",participantes.to_string(tercer_puesto))

    print("\nNuevo Ranking tras la competencia\n")
    new_list = participantes.nuevo_arreglo(primero, segundo, tercer_puesto,
                                   competidores)
    participantes.orden_sort(new_list)
    participantes.mostrar_participantes(new_list)





if __name__ == "__main__":
    principal()
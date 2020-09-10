import planb

print("Este es el plan b")





def principal():
    n = 16
    participantes = []
    planb.carga_automatica(participantes)

    planb.orden_sort(participantes)
    planb.mostrar_participantes(participantes)

    #generaciópn de los cruces
    print("OCTAVOS\n")
    planb.octavos(participantes)
    print("INTENTO DE CUARTOS\n")
    cuartos = planb.ganadores(participantes)
    planb.cruces(cuartos)
    print("\nINTENTO DE SEMIFINAL\n")
    semis = planb.ganadores(cuartos)
    planb.cruces(semis)
    print("\nINTENTO DE FINAL\n")
    final = planb.ganadores(semis)
    pri, seg = planb.final(final)
    print("El primero es:",pri)
    print("El segundo es:",seg)











if __name__ == "__main__":
    principal()
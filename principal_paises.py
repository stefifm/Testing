"""
Aquí está el programa principal del trabajo práctico
"""



import funciones_paises


def principal():
    vec_paises = []
    fd = "paises.csv"
    carga_matriz = False
    opcion = 0
    while opcion != 8:
        print("Menú de opciones")
        print("1) Muestra del listado completo de países")
        print("2) País con mayor cantidad de campeonatos")
        print("3) Cantidad de países que ganaron por confederación")
        print("4) Registro y archivo de confederación")
        print("5) Búsqueda de una confederación")
        print("6) Fixture matriz del próximo mundial")
        print("7) Búsqueda del país en el nuevo fixture")
        print("8) Salir.")
        opcion = funciones_paises.validar_rango(1, 8,"\nIngrese una opción: ")
        print("\n","=" * 100,"\n")
        if opcion == 1:
            print("LISTADO COMPLETO DE PAÍSES")
            print("-" * 100, "\n")
            funciones_paises.cargar_vector(fd, vec_paises)
            funciones_paises.mostrar_vector_paises(vec_paises)
            print("\n", "=" * 100)
        elif opcion == 2:
            print("PAÍS CON MAYOR CANTIDAD DE CAMPEONATOS")
            print("-" * 100, "\n")
            mayor = funciones_paises.mayor(vec_paises)
            funciones_paises.mostrar_vector_paises(mayor)
            print("\n", "=" * 100)
        elif opcion == 3:
            print("CANTIDAD DE PAÍSES QUE FUERON CAMPEONES POR CONFEDERACIÓN")
            print("-" * 100, "\n")
            funciones_paises.contador_paises_campeonatos(vec_paises)
            print("\n", "=" * 100)
        elif opcion == 4:
            print("UNA CONFEDERACIÓN, UN ARCHIVO")
            print("-" * 100, "\n")
            x = funciones_paises.validar_rango(0, 5,"Ingrese el código de "
                                                    "confederación (0 a 5):")
            vec_conf = funciones_paises.vector_confederacion(vec_paises,x)
            funciones_paises.orden_sort(vec_conf)
            archivo = "clasificacion" + str(x) + ".dat"
            funciones_paises.grabar_archivo_confederacion(vec_conf,archivo)
            print("\n", "=" * 100)
        elif opcion == 5:
            print("BUSCANDO UNA CONFEDERACIÓN...Y SU ARCHIVO")
            print("-" * 100, "\n")
            conf = funciones_paises.validar_rango(0, 5, "Ingrese el código de "
                                                    "confederación (0 a 5):")
            vec_conf = funciones_paises.vector_confederacion(vec_paises, conf)
            funciones_paises.orden_sort(vec_conf)
            archivo = "clasificacion" + str(conf) + ".dat"
            funciones_paises.buscar_archivo(archivo, vec_conf)
            print("\n", "=" * 100)
        elif opcion == 6:
            print("ARMANDO EL FIXTURE DEL PRÓXIMO MUNDIAL...")
            print("-" * 100, "\n")
            y = funciones_paises.validar_anfitrion(vec_paises)
            mat = funciones_paises.matriz(vec_paises, y)
            funciones_paises.mostrar_matriz(mat)
            carga_matriz = True
            print("\n", "=" * 100)
        elif opcion == 7:
            print("VER SI UN PAÍS CLASIFICÓ AL MUNDIAL...")
            print("-" * 100, "\n")
            if carga_matriz == False:
                print("No se cargó la matriz")
            else:
                pais = input("Ingrese un país: ")
                grupo = funciones_paises.buscar_pais_matriz(mat, pais)
                if grupo != None:
                    print("Está en el mundial y se encuentra en el grupo",
                          funciones_paises.convertir_num_letra_grupo(grupo))
                else:
                    print("No se clasificó al mundial")
            print("\n", "=" * 100)
        else:
            print("=============== PROGAMA FINALIZADO =================")


if __name__ == "__main__":
    principal()
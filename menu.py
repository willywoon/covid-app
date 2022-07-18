import os
from cargar import cargar
from conexion import Conexion


def menuApp():

    menu = True

    while menu:

        print("""

        1. mostrar pais
        2. mostrar todos los paises
        3. eliminar pais
        4. modificar pais
        5. actualizar datos
        6. salir
        """)

        opcion = input("ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print("mostrar pais")
            codigoPais = input("ingrese el codigo del pais: ")
            consultaDB = Conexion()
            codigoPais = codigoPais.lower()
            if len(codigoPais) > 3:
                pais = consultaDB.mostrarPaisPorNombre(codigoPais)
                if pais == None:
                    print("No existe el pais")
                else:
                    print("codigo pais: '{}'', nombre pais: '{}', total confirmados: {}, total de muertos: {}, total nuevos fallecidos: {}, fecha: {}".format(
                        pais[0], pais[1], pais[2], pais[3], pais[4], pais[5]))

            if len(codigoPais) == 2:
                pais = consultaDB.mostrarPais(codigoPais)
                if pais == None:
                    print("no existe el pais")
                else:
                    print("codigo pais: '{}'', nombre pais: '{}', total confirmados: {}, total de muertos: {}, total nuevos fallecidos: {}, fecha: {}".format(
                        pais[0], pais[1], pais[2], pais[3], pais[4], pais[5]))

        elif opcion == "2":
            os.system("cls")
            print("mostrar todos los paises")
            consultaDB = Conexion()
            paises = consultaDB.mostrarTodos()
            for pais in paises:
                print("codigo", pais[0])
                print("nombre", pais[1])
                print("total confirmados", pais[2])
                print("total de muertos", pais[3])
                print("total nuevos fallecidos", pais[4])
                print("fecha", pais[5])
                print("---------------------------------------------------")

        elif opcion == "3":
            os.system("cls")
            print("eliminar pais")
            codigoPais = input("ingrese el codigo del pais: ")
            consultaDB = Conexion()
            consultaDB.eliminarPais(codigoPais)
            print("pais eliminado")

        elif opcion == "4":
            os.system("cls")
            print("modificar pais")
            codigoPais = input("ingrese el codigo del pais: ")
            confirmados = input("ingrese el total de confirmados: ")
            muertos = input("ingrese el total de muertos: ")
            nuevosMuertos = input("ingrese el total de nuevos muertos: ")
            fecha = input("ingrese la fecha: ")
            consultaDB = Conexion()
            consultaDB.modificarPais(
                codigoPais, confirmados, muertos, nuevosMuertos, fecha)
            print("pais modificado")

        elif opcion == "5":
            os.system("cls")
            print("actualizar datos")
            cargar()
            print("datos actualizados")

        elif opcion == "6":
            print("salir")
            menu = False

        else:
            print("opcion no valida")
            os.system("cls")

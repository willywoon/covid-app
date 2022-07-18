from conexion import Conexion
from consulta import Consulta


def cargar():
    nuevaConsulta = Consulta('https://api.covid19api.com/summary')
    db = Conexion()
    nuevaConsulta.consultar()

    for pais in nuevaConsulta.getListaPasises():
        if db.mostrarPais(pais[0]) == None:  # si no existe el pais
            db.ingresarPais(pais[0], pais[1], pais[2],
                            pais[3], pais[4], pais[5])
        else:
            db.mostrarPais(pais[0])
            revisar = db.mostrarPais(pais[0])
            if revisar[5] != pais[5]:  # revisar la fecha
                db.modificarPais(pais[0], pais[2], pais[3], pais[4], pais[5])
                print("Actualizado")

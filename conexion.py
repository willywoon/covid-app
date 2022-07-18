import mysql.connector


class Conexion:

    def __init__(self):
        self.__conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="covid_app"
        )
        self.__cursor = self.__conexion.cursor()
        if self.__conexion.is_connected():
            print("Conexion exitosa")

    def mostrarPais(self, codigoPais):
        sql = 'select *from paises where pai_codigo = "{}"'.format(codigoPais)
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchone()
        except Exception as e:
            print("Error al mostrar el pais", e)

    def mostrarPaisPorNombre(self, nombrePais):
        sql = 'select *from paises where pai_nombre = "{}"'.format(nombrePais)
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchone()
        except Exception as e:
            print("Error al mostrar el pais", e)

    def mostrarTodos(self):
        sql = 'select *from paises'
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except Exception as e:
            print("Error al mostrar los paises", e)

    def ingresarPais(self, codigo, nombre, confirmados, muertos, nuevosMuertos, fecha):
        sql = "INSERT INTO paises (pai_codigo, pai_nombre, pai_total_confirmados, pai_total_muertos, pai_nuevos_muertos, fecha) VALUES ('{}', '{}', {}, {}, {}, '{}')".format(
            codigo, nombre, confirmados, muertos, nuevosMuertos, fecha)
        try:
            self.__cursor.execute(sql)
            self.__conexion.commit()
        except Exception as e:
            print("Error al ingresar el pais", e)

    def eliminarPais(self, codigoPais):
        sql = "DELETE FROM paises WHERE pai_codigo = '{}'".format(
            codigoPais)
        try:
            self.__cursor.execute(sql)
            self.__conexion.commit()
        except Exception as e:
            print("Error al eliminar el pais", e)

    def modificarPais(self, codigoPais, confirmados, muertos, nuevosMuertos, fecha):
        sql = "UPDATE paises SET pai_total_confirmados = {}, pai_total_muertos = {}, pai_nuevos_muertos = '{}', fecha = '{}' WHERE pai_codigo = '{}'".format(
            confirmados, muertos, nuevosMuertos, fecha, codigoPais)
        try:
            self.__cursor.execute(sql)
            self.__conexion.commit()
        except Exception as e:
            print("Error al modificar el pais", e)

    def cerrar(self):
        self.__cursor.close()
        self.__conexion.close()

import mysql.connector


class Conexion:

    def __init__(self):
        self.__conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="compa"
        )
        self.cursor = self.__conexion.cursor()
        if self.__conexion.is_connected():
            print("Conexion exitosa")

    def insertar(self, id, pais, idPais, paisMinus, nuevosConfirm, totalConfirm, nuevasMuertes, totalMuertes, nuevosRecup, totalRecup, fecha):
        sql = "INSERT INTO paises (id, pais, idPais, paisMinus, nuevosConfirm, totalConfirm, nuevasMuertes, totalMuertes, nuevosRecup, totalRecup, fecha) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            id, pais, idPais, paisMinus, nuevosConfirm, totalConfirm, nuevasMuertes, totalMuertes, nuevosRecup, totalRecup, fecha)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise


x = Conexion()
#x.insertar(1, "Argentina", "AR", "Argentina", "10", "20", "10", "20", "10", "20", "2020-01-01")
x.insertar("3e90baa0-57be-43b3-81b8-ae3bd1181b61", "Afghanistan", "AF",
           "afghanistan", 0, 183572, 0, 7731, 0, 0, "2022-07-18T18:58:00.69Z")

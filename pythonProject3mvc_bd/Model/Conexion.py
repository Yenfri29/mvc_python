import pymysql

class Conexion:

    def __init__(self):
        self.servidor="localhost"
        self.bd="senati_bd"
        self.user="root"
        self.clave=""

    def conectar(self):
        try:
            self.Conexion=pymysql.connect(self.servidor,self.user,self.clave,self.bd)
            self.cn=self.Conexion.cursor()
            print("Se conecto a la BD")

        except Exception as e:
            print("Error: ",e)

        #insert, update, delete
    def setEjecutarQuery(self,sql):
        try:
            respuesta=self.cn.execute(sql)
            print("respuesta -->: ", respuesta)
            self.Conexion.commit()
            self.Conexion.close()
            return 1
        except Exception as ex:
            print("Error: ",ex)
            self.Conexion.rollback()
            return 0

        #select
    def getEjecutarQuery(self,sql):
        try:
            self.cn.execute(sql)
            registros=self.cn.fetchall()
            return registros
        except Exception as ex:
            print("Error: ", ex)
            return 0



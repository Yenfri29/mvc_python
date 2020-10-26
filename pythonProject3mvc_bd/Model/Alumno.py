from .Conexion import Conexion
from .Persona import Persona

class Alumno(Persona):
    codigo=""
    ciclo=""

    def __init__(self):
        pass

    def setDatospersonales(self,nombre,apellido,dni,sexo):
        Persona.__init__(self,nombre,apellido,dni,sexo)

    def setMatricula(self,codigo,ciclo):
        self.codigo=codigo
        self.ciclo=ciclo

    def setCodigo(self,codigo):
        self.codigo=codigo

    def setCiclo(self,ciclo):
        self.ciclo=ciclo

    def getCodigo(self):
        return self.codigo

    def getCiclo(self):
        return self.ciclo

    def insertarAlumno(self):
        conecta=Conexion()
        conecta.conectar()
        SQL="INSERT INTO alumno(codigo,nombres,apellidos,dni,sexo,ciclo) VALUES('"+self.codigo+"','"+self.nombre+"','"+self.apellido+"','"+self.dni+"','"+self.sexo+"',"+str(self.ciclo)+")"
        print(SQL)
        resp=conecta.setEjecutarQuery(SQL)
        if (resp):

            return 1
        else:
            return 0
#******************************************************************
    def mostrarAlumnos(self):
        conecta = Conexion()
        conecta.conectar()
        SQL ="SELECT *FROM alumno"
        registros=conecta.getEjecutarQuery(SQL)
        return registros
#******************************************************************
    def actualizarAlumno(self,codigo):
        pass

    def eliminarAlumno(self):
        pass


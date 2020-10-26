from Model.Alumno import Alumno

class PersonaController:

    def __init__(self):
        pass

    #********************** CREAR REGISTROS *************************
    def crearRegistro(self,lista):
        self.enlace=Alumno()
        self.enlace.setDatospersonales(lista[0],lista[1],lista[2],lista[3])
        self.enlace.setMatricula(lista[4],lista[5])
        self.enlace.insertarAlumno()
        if (resp):
            print("registro correcto")
          #  return 1
        else:
            print("registro incorrecto")
          #  return 0
    #********************** LEER REGISTROS *************************
    def listarRegistros(self):
        self.enlace =Alumno()
        lista=self.enlace.mostrarAlumnos()


    #********************** ACTUALIZAR REGISTRO *************************
    def actualizarRegistro(self,codigo):
        pass
    #********************** ELIMINAR REGISTRO *************************
    def eliminarRegistro(self):
        pass
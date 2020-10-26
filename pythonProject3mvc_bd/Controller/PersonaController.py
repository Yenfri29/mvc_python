from Model.Alumno import Alumno

class PersonaController:

    def __init__(self):
        pass

    #******* CREAR REGISTROS *******
    def crearRegistro(self,lista):
        self.enlace=Alumno()
        self.enlace.setDatosPersonales(lista[0],lista[1],lista[2],lista[3])
        self.enlace.setMatricula(lista[4],lista[5])
        resp=self.enlace.insertarAlumno()
        if(resp):
            print("registro correcto")
        else:
            print("registro incorrecto")

    #******* LEER REGISTROS *******
    def listarRegistros(self):
        self.enlace=Alumno()
        lista=self.enlace.mostrarAlumnos()
        return lista

    #******* ACTUALIZAR REGISTROS *******
    def actualizarRegistro(self,codigo):
        pass
    #******* ELIMINAR REGISTROS *******
    def eliminarRegistro(selfself,codigo):
        pass
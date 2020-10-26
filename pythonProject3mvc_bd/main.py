from Controller.PersonaController import PersonaController

lista=["Maria", "Salaz","76993563 ", "M","0012",2]
enlace=PersonaController()
#enlace.crearRegistro(lista)
listaRegistros=enlace.listarRegistros() #Se obtienen los registros
for i in range(len(listaRegistros)):
    print("Cod: ",listaRegistros[i][0])
    print("Nombre: ",listaRegistros[i][1])
    print("Apellidos: ",listaRegistros[i][2])
    print("Dni: ",listaRegistros[i][3])
    print("Sexo: ",listaRegistros[i][4])
    print("Ciclo: ",listaRegistros[i][5])
    print("**************************")

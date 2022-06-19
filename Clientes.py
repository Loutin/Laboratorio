class Clientes(): 
    
<<<<<<< HEAD
    list = []
    #Lector de archivos
    Lista_clientes = open("C://Users//fatim//Documents//Laboratorio_SO//Lab_SO//Listas//Lista_clientes.txt")
    Lines = Lista_clientes.readlines()
    print(Lista_clientes)
=======
    def __init__(self, id, name, nombre_proyecto):
        self.id = id
        self.name = name
        self.nombre_proyecto = nombre_proyecto
    
    def proyectos(self, nro_proyectos):
        nombre_proyecto = input("Introdusca el nombre del proyecto: ")
        descripcion_proyecto = input("Defina las caracteristicas del proyecto")
>>>>>>> 1440fefa0ac3a465af8628578f27e3a071c006a8

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Clientes.list.append(self)
    
    def BuscarCliente(lista, id):
        for cliente in lista:
            if cliente.id == id:
                return cliente

    for line in Lines:
        x = line.split(", ")
        c = Clientes(x[0], x[1])
        print(c.name)

    
    

<<<<<<< HEAD
    
=======
    
>>>>>>> 1440fefa0ac3a465af8628578f27e3a071c006a8

from Proyectos import Proyectos


class Clientes(): 
    
    Lista = []
    
    #Lector de archivos
    Lista_clientes = open("Lista_clientes.txt")
    Lines = Lista_clientes.readlines()

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Clientes.Lista.append(self)
        self.listaProyectos = []
    
    def BuscarCliente(id):
        for cliente in Clientes.Lista:
            if cliente.id == id:
                return cliente

    def CargarClientes():
        for line in Clientes.Lines:
            x = line.split(", ")
            c = Clientes(int(x[0]), x[1])

    def __str__(self):
        stringCliente =  "Id: " + str(self.id) + "    Nombre : " + self.name + "\n"
        for i in self.listaProyectos:
            stringCliente += "Proyectos" + str(i) + "\n"   #No se ven los proyectos que estan asociados a cada cliente
        return stringCliente
    
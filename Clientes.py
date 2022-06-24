class Clientes(): 
    
    list = []
    #Lector de archivos
    Lista_clientes = open("C://Users//fatim//Documents//Laboratorio_SO//Lab_SO//Listas//Lista_clientes.txt")
    Lines = Lista_clientes.readlines()

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

    
    

    
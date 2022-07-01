class Clientes(): 
    
    Lista = []
    
    #Lector de archivos
    Lista_clientes = open("Listas//Lista_clientes.txt")
    Lines = Lista_clientes.readlines()

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Clientes.Lista.append(self)
    
    def BuscarCliente(lista, id):
        for cliente in lista:
            if cliente.id == id:
                return cliente

    def CargarClientes(self):
        for line in Clientes.Lines:
            x = line.split(", ")
            c = Clientes(x[0], x[1])


    
    

    
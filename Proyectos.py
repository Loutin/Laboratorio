class Proyectos:
    
    Lista = []

    #Lector de archivos
    Lista_proyectos = open("Lista_proyectos.txt")
    Lines = Lista_proyectos.readlines()

    def __init__(self, id, name, time, Id_cliente):
        self.id = id
        self.name = name
        self.time = time
        self.Id_cliente = Id_cliente
        self.tareas = []
        Proyectos.Lista.append(self)
        from Clientes import Clientes
        self.cliente = Clientes.BuscarCliente(Id_cliente)
        self.cliente.listaProyectos.append(self)


    def BuscarProyecto(self, id):
        for proyecto in Proyectos.Lista:
            if proyecto.id == id:
                return proyecto
    
    def CargarProyectos():
        for line in Proyectos.Lines:
            x = line.split(", ")
            c = Proyectos(int(x[0]), x[1], int(x[2]), int(x[3]))
   
    def AgregarTarea(self, tarea):
        self.append(tarea)

    def duracionTotal(self):
        TiempoTotal = 0
        for tarea in self.tareas:
            TiempoTotal += tarea.tiempo
        return TiempoTotal
    
    def tiempoRestante(self):
        TiempoRestante = 0
        for tarea in self.tareas:
            if not tarea.finalizada:
                TiempoRestante += tarea.tiempo
        return TiempoRestante

    def __str__(self):
        datos = "Id: " + str(self.id) + "    Nombre : " + self.name + "    Duracion total: " + str(Proyectos.duracionTotal) + "    Tiempo restante: " + str(Proyectos.tiempoRestante)
        return datos
    
    





   
    

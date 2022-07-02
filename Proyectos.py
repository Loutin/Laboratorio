from Lab_SO.Clientes import Clientes


class Proyectos:
    
    Lista = []

    #Lector de archivos
    Lista_proyectos = open("C:\Users\fatim\Documents\Laboratorio_SO\Lab_SO\Listas\Lista_proyectos.txt")
    Lines = Lista_proyectos.readlines()

    def __init__(self, id, name, time, Id_cliente):
        self.id = id
        self.name = name
        self.time = time
        self.Id_cliente = Id_cliente
        self.tareas = []
        Proyectos.Lista.append(self)
        self.cliente = Clientes.BuscarCliente(Id_cliente)
        self.cliente.Lista_proyectos.append(self)

    def BuscarProyecto(self, id):
        for proyecto in Proyectos.Lista:
            if proyecto.id == id:
                return proyecto
    
    def CargarProyectos(self):
        for line in Proyectos.Lines:
            x = line.split(", ")
            c = Proyectos(int(x[0]), x[1], int(x[2]))
   
    def AgregarTarea(self, tarea):
        self.append(tarea)

    def duracionTotal(self):
        TiempoTotal = 0
        for tarea in self.tareas:
            TiempoTotal += tarea.timepo
        return TiempoTotal
    
    def tiempoRestante(self):
        TiempoRestante = 0
        for tarea in self.tareas:
            if not tarea.finalizada:
                TiempoRestante += tarea.tiempo
        return TiempoRestante

    def __str__(self):
        return "Id: " + str(self.id) + " Nombre : " + self.name + " Duracion total" + Proyectos.duracionTotal + " T restante" + Proyectos.tiempoRestante
    
    
   
    






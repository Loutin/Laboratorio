class Proyectos:
    
    Lista = []

    #Lector de archivos
    Lista_prooyectos = open("C:\Users\fatim\Documents\Laboratorio_SO\Lab_SO\Listas\Lista_proyectos.txt")
    Lines = Lista_prooyectos.readlines()

    def __init__(self, id, name, time):
        self.id = id
        self.name = name
        self.time = time
        self.tareas = []
        Proyectos.Lista.append(self)
        

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


    
    
   
    






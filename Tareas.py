from Proyectos import Proyectos


class Tareas:

    Lista = []
    
    #Lector de archivos
    Lista_tareas = open("Lista_tareas.txt")
    Lines = Lista_tareas.readlines()

    def __init__(self, name, prioridad, timepo, ID_Proyecto):
        self.name = name
        self.prioridad = prioridad
        self.tiempo = timepo
        self.ID_Proyecto = ID_Proyecto
        self.finalizada = False
        p = Proyectos.BuscarProyecto(ID_Proyecto)
        if p:
            p.AgregarTarea(self)
        

    def CargarTarea():
        for line in Tareas.Lines:
            x = line.split(", ")
            c = Tareas(x[0], int(x[1]), int(x[2]), int(x[3]))

    def BuscarTareas(self, name):
        for tareas in Tareas.Lista:
            if tareas.name == name :
                return tareas
    
    def __str__(self):
        stringTareas =  "Nombre: " + self.name + "     Prioridad : " + str(self.prioridad)  + "     Tiempo: " + str(self.tiempo) + "     ID de proyecto: " + str(self.ID_Proyecto)
        return stringTareas   

    
    
    
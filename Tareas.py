from typing import List

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
        

    def CargarTarea(self):
        for line in Tareas.Lines:
            x = line.split(", ")
            c = Tareas(x[0], x[1], x[2], x[3])

    def BuscarTareas(self, Nombre):
        for tareas in Tareas.Lista:
            if tareas.Nombre == Nombre :
                return tareas
    
    def __str__(self):
        stringTareas =  "Nombre: " + self.name + "     Prioridad : " + str(self.prioridad)  + "     Tiempo: " + str(self.tiempo) + "     ID de proyecto: " + self.ID_Proyecto
        return stringTareas   

    

    
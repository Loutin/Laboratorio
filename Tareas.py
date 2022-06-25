from typing import List

from Laboratorio.Proyectos import Proyectos


class Tareas:

    List = []
    
    #Lector de archivos
    Lista_tareas = open("C:\Users\fatim\Documents\Laboratorio_SO\Lab_SO\Listas\Lista_tareas.txt")
    Lines = Lista_tareas.readlines()

    def __init__(self, name, prioridad, timepo, ID_Proyecto):
        self.name = name
        self.prioridad = prioridad
        self.tiempo = timepo
        self.finalizada = False
        p = Proyectos.BuscarProyecto(ID_Proyecto)
        if p:
            p.AgregarTarea(self)
        

    def CargarTarea(self):
        for line in Tareas.Lines:
            x = line.split(", ")
            c = Tareas(x[0], x[1], x[2], x[3])

    

    

    
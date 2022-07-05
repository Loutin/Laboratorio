from typing import List


class Desarrolladores():
    
    List = []

    #Lector de archivos
    Lista_desarrolladores = open("Lista_desarrolladores.txt")
    Lines = Lista_desarrolladores.readlines()


    def __init__(self, id, nombre, horas, conocimiento):
        self.id = id
        self.nombre = nombre
        self.horas = horas
        self.conocimiento = conocimiento
        Desarrolladores.List.append(self)

    def CargarDesarrolladores(self):
        for line in Desarrolladores.Lines:
            x = line.split(", ")
            c = Desarrolladores(int(x[0]), x[1], int(x[2]), x[3])
            

    
    
    
from typing import List


class Desarrolladores():
    
    Lista = []

    #Lector de archivos
    Lista_desarrolladores = open("Lista_desarrolladores.txt")
    Lines = Lista_desarrolladores.readlines()


    def __init__(self, id, nombre, horas, conocimiento):
        self.id = id
        self.nombre = nombre
        self.horas = horas
        self.conocimiento = conocimiento
        Desarrolladores.Lista.append(self)

    def BuscarDesarrolladores(id):
        for desarrollador in Desarrolladores.Lista:
            if desarrollador.id == id:
                return desarrollador

    def CargarDesarrolladores():
        for line in Desarrolladores.Lines:
            x = line.split(", ")
            c = Desarrolladores(int(x[0]), x[1], int(x[2]), x[3])
            
    def __str__(self):
        stringDesarrollador =  "Id: " + str(self.id) + "     Nombre : " + self.nombre  + "     Horas: " + str(self.horas) + "     Conocimientos: " + self.conocimiento
        return stringDesarrollador
    
    
    
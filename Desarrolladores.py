from typing import List


class Desarrolladores():
    List = []

    #Lector de archivos
    Lista_desarrolladores = open("C://Users//fatim//Documents//Laboratorio_SO//Lab_SO//Listas//Lista_desarrolladores.txt")
    Lines = Lista_desarrolladores.readlines()
    print(Lista_desarrolladores)

    def __init__(self, id, nombre, horas, conocimiento):
        self.id = id
        self.nombre = nombre
        self.horas = horas
        self.conocimiento = conocimiento
        Desarrolladores.List.append(self)

    def horasDeTrabajo(self, horas):
        for line in Lines:
            x = line.split(", ")
            c = Desarrolladores(x[0], x[1], [2], x[3])
            print(horas)


    def conocimientos(self, lenguajes):
        lenguajes = """lenguaje que maneja"""
    
    
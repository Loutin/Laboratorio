class Tareas:

    def __init__(self, name):
        self.name = name

    def funcionalidad(self, implementacion):
        implementacion = """funcionalidad implementada por el programador"""

    def duracion_estimada(self, duracion_de_tarea):
        duracion_de_tarea = """tiempo que durara la tarea"""

    def prioridad(self, nivel_de_prioridad):
        nivel_de_prioridad = """prioridad que tendra la tarea"""

    #Lector de archivos
    Lista_tareas = open("C:\Users\fatim\Documents\Laboratorio_SO\Lab_SO\Listas\Lista_tareas.txt")
    Lines = Lista_tareas.readlines()
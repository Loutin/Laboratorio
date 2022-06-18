from random import randint, random


class Clientes(): 
    
    def __init__(self, id):
        self.id = id
    
    def proyectos(self, nro_proyectos):
        nombre_proyecto = input("Introdusca el nombre del proyecto: ")
        descripcion_proyecto = input("Defina las caracteristicas del proyecto")

      

    def añadir_aclientes(self):
        nombre_cliente = input("Introdusca el nombre del cliente: ")
        numero_aleatorio = randint(1, 2147483647)
        lista_clientes =  []
        while numero_aleatorio in lista_clientes:
                numero_aleatorio += 1  
        lista_clientes.append(numero_aleatorio)


    

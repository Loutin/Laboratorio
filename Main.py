from Clientes import Clientes
from Desarrolladores import Desarrolladores
from Tareas import Tareas
from Proyectos import Proyectos

def CargarDatos():
    Clientes.CargarClientes()
    Desarrolladores.CargarDesarrolladores()
    Proyectos.CargarProyectos()
    Tareas.CargarTarea()
    
CargarDatos()
opcion = '0'
while not(opcion=='5'):
    print(' 1. Clientes actuales ')
    print(' 2. Desarrolladores disponibles ')
    print(' 3. Proyectos actuales ')
    print(' 4. Tareas de un proyecto ')
    print(' 5. Salir')

    opcion = input('  --- ¿Elegir opcion?: ')
    
    if (opcion=='3'):
        for i in Proyectos.Lista:
            print(i)
        
    elif (opcion=='4'):
        Id_proyecto = input("Ingrese el Id del proyecto:  ")
        p = Proyectos.BuscarProyecto(int(Id_proyecto))
        if p:
            p.ImprimirTareas()
        else:
            print("No existe el proyecto")

        
    elif (opcion=='2'): 
        for i in Desarrolladores.Lista:
            print(i)
        
    elif (opcion=='1'):     
        for i in Clientes.Lista:
            print(i)
                
    elif (opcion=='5'):
        print('El menu se cerro correctamente')        
    elif (opcion not in [1, 2, 3, 4 , 5]):
        print('Opcion no existente ')
        print('Favor de ingresar nuevamente')
        
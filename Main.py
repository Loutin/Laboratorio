from Clientes import Clientes
from Desarrolladores import Desarrolladores
from Tareas import Tareas
from Proyectos import Proyectos

opcion = '0'
while not(opcion=='5'):
    print(' 1. Proyectos actuales ')
    print(' 2. Tareas de un proyecto ')
    print(' 3. Desarrolladores disponibles ')
    print(' 4. Clientes actuales ')
    print(' 5. Salir')

    opcion = input('  --- ¿Elegir opcion?: ')
    
    if (opcion=='1'):
        Proyectos.CargarProyectos()
        for i in Proyectos.Lista:
            print(i)
        
    elif (opcion=='2'):
        Tareas.CargarTarea()
        for i in Tareas.Lista:
            print(i)
        
    elif (opcion=='3'):
        Desarrolladores.CargarDesarrolladores()
        for i in Desarrolladores.Lista:
            print(i)
        
    elif (opcion=='4'):
        Clientes.CargarClientes()
        for i in Clientes.Lista:
            print(i)
                
    elif (opcion=='5'):
        print('El menu se cerro correctamente')        
    elif (opcion not in [1, 2, 3, 4 , 5]):
        print('Opcion no existente ')
        print('Favor de ingresar nuevamente')
        
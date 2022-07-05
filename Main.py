from Clientes import Clientes
from Proyectos import Proyectos

def CargaDeDatos():
    Clientes.CargarClientes()
    Proyectos.CargarProyectos()

CargaDeDatos()

opcion = '0'
while not(opcion=='6'):
    print(' 1. Proyectos actuales 01')
    print(' 2. Tareas de un proyecto 02')
    print(' 3. Tiempo restante de un proyecto  03')
    print(' 4. Desarrolladores disponibles 04')
    print(' 5. Clientes actuales 05')
    print(' 6. Salir')

    opcion = input('  --- ¿Elegir opcion?: ')
    
    if (opcion=='1'):
        for i in Proyectos.Lista:
            print(i)
        
    elif (opcion=='2'):
        print('')
        
    elif (opcion=='3'):
        print('Tiempo restante de un proyecto')
        
    elif (opcion=='4'):
        print('Desarrolladores disponibles')
        
    elif (opcion=='5'):
        for i in Clientes.Lista_clientes:
            print(i)
                
    elif (opcion=='6'):
        print('El menu se cerro correctamente')        
    elif (opcion not in [1, 2, 3, 4 , 5, 6]):
        print('Opcion no existente ')
        print('Favor de ingresar nuevamente')
        
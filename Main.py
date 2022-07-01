from Lab_SO.Clientes import Clientes
from Lab_SO.Proyectos import Proyectos


opcion = '0'
while not(opcion=='6'):
    print(' 1. Proyectos actuales 01')
    print(' 2. Tareas de un proyecto 02')
    print(' 3. Tiempo restante de un proyecto  03')
    print(' 4. Desarrolladores disponibles 04')
    print(' 5. Clientes actuales 05')
    print(' 6. Salir')

    opcion=input('  --- ¿Cuál opcion?: ')
    
    if (opcion=='1'):
        print(ProyectosActuales = Proyectos.BuscarProyecto(Proyectos.Lista_prooyectos, "2"))
        
    elif (opcion=='2'):
        print('')
        
    elif (opcion=='3'):
        print('Tiempo restante de un proyecto')
        
    elif (opcion=='4'):
        print('Desarrolladores disponibles')
        
    elif (opcion=='5'):
        print(ClientesActuales = Clientes.BuscarCliente(Clientes.Lista, "1"))
                
    elif (opcion=='6'):
        print('El menu se cerro correctamente')        
    else:
        print('Opcion no existente')
        print('Favor de ingresar nuevamente')
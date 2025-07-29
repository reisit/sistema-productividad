from funciones.Conexion import Conexion
from funciones.tareas import Tareas
from datetime import datetime


def bisiesto(a):
    return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)

def diasMes(m, a):
    if m == 2:return 29 if bisiesto(a) else 28
    elif m in [4, 6, 9, 11]: return 30
    elif m in [1, 3, 5, 7, 8, 10, 12]: return 31
    return 0  # Mes inválido

def validarFecha(fecha):
    try:
        partes = fecha.strip().split("-")
        if len(partes) != 3:
            return False, "Formato inválido. Usa 'yyyy-mm-dd'."

        a, m, d = map(str, partes)
        if int(m) < 1 or int(m) > 12 or len(m) != 2:
            return False, f"Mes inválido: {m}."

        maxDias = diasMes(int(m), int(a))
        if int(d) < 1 or int(d) > maxDias or len(d) != 2:
            return False, f"Día inválido: {d} para el mes {m} en el año {a}."
        
        if len(a) != 4: return False, f'Formato invalido para el año: {a}'
        
        return True, fecha
    
    except ValueError:
        return False, "Error: Asegúrate de ingresar solo números en formato 'dd-mm-yyyy'."

def validarEmpleadoID():
    from funciones.empleadosDAO import EmpleadosDAO
    while True:
        empleadoId = int(input('Ingresar id del empleado: '))
        if empleadoId in [e.id for e in EmpleadosDAO.Seleccionar()]: return empleadoId
        else: print('Valor invalido')

def obtenerFecha():
    while True:
        entrada = input('Ingresa la fecha de asignación (yyyy-mm-dd): ')
        salida, fecha = validarFecha(entrada)
        if salida: return fecha
        print('Error al ingresar fecha') 

def validacionesValores():
    d = input('Insertar descripcion de la tarea: ')

    while True:
        fechaAsignacion = obtenerFecha()
        fechaEntrega = obtenerFecha()
        if datetime(*map(int, fechaAsignacion.strip().split('-'))) > datetime(*map(int, fechaEntrega.strip().split('-'))): 
            print('Error: La fecha de asignacion no puede ser mayor que la fecha de entrega')
        else: break

    while True:
        estado = input('Insertar estado de la tarea: ')
        if estado not in ['pendiente','en progreso','completada']: print('Valor invalido')
        else: break

    empleadoId = validarEmpleadoID()

    return d, fechaAsignacion, fechaEntrega, estado, empleadoId


class TareasDAO:
    SELECCIONAR = 'SELECT * FROM tareas'
    INSERTAR = 'INSERT INTO tareas(descripcion,fechaAsignacion,fechaEntrega,estado,empleadoId) VALUES(%s,%s,%s,%s,%s)'
    ACTUALIZAR = 'UPDATE tareas SET descripcion=%s,fechaAsignacion=%s,fechaEntrega=%s,estado=%s,empleadoId=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM tareas WHERE id =%s'
    ELIMINAR_EMPLEADOID = 'DELETE FROM tareas WHERE empleadoId=%s'

    @classmethod
    def Seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            tareas = [Tareas(t[0],t[1],t[2],t[3],t[4],t[5]) for t in cursor.fetchall()]
            return tareas
        
        except Exception as e:
            print(f'Error: {e}') 

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def Insertar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            
            d, fechaAsignacion, fechaEntrega, estado, empleadoId = validacionesValores()

            values = (d,fechaAsignacion,fechaEntrega,estado,empleadoId)
            cursor.execute(cls.INSERTAR,values)
            t = Tareas(descripcion=d,fechaAsignacion=fechaAsignacion,fechaEntrega=fechaEntrega,estado=estado,empleadoId=empleadoId)
            print(f'Tarea creada satisfactoriamente!: \n{t}')
            conexion.commit()

        except Exception as e:
            print(F'Error: {e}')
        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion) 
    
    @classmethod
    def Actualizar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            i = int(input('Ingresar id de la tarea a modificar: '))

            d, fechaAsignacion, fechaEntrega, estado, empleadoId = validacionesValores()

            values = (d,fechaAsignacion,fechaEntrega,estado,empleadoId, i)
            cursor.execute(cls.ACTUALIZAR,values)
            t = Tareas(id=i,descripcion=d,fechaAsignacion=fechaAsignacion,fechaEntrega=fechaEntrega,estado=estado,empleadoId=empleadoId)
            print(f'Cliente modificado satisfactoriamente!: \n{t}')
            conexion.commit()
        
        except Exception as e:
            print(f'Error: {e}') 

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def Eliminar(cls):
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            i = int(input('Insertar id a eliminar: '))
            values = (i,)
            cursor.execute(cls.ELIMINAR,values)
            print('Eliminado exitosamente')
            conexion.commit()
        
        except Exception as e:
            print(f'Error: {e}') 

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def EliminarEmpleadoID(cls, id = None):
        from funciones.empleadosDAO import EmpleadosDAO
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            if id is None:
                id = validarEmpleadoID()
            elif id not in [e.id for e in EmpleadosDAO.Seleccionar()]:
                return f'Valor invalido, insertar id'
            
            values = (id,)
            cursor.execute(cls.ELIMINAR_EMPLEADOID,values)
            print('Tareas eliminadas exitosamente')
            conexion.commit()
        
        except Exception as e:
            print(f'Error: {e}') 

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)

#    @classmethod
#    def test(cls):
#        from empleadosDAO import EmpleadosDAO
#        from departamentosDAO import DepartamentoDAO
#        conexion = None
#        try:
#            conexion = Conexion.obtener_conexion()
#            cursor = conexion.cursor()
#            cursor.execute(cls.SELECCIONAR)
#            tareas = [Tareas(t[0],t[1],t[2],t[3],t[4],t[5]) for t in cursor.fetchall()]
#            for t in tareas: print(t)
#            empleados = EmpleadosDAO.Seleccionar()
#            for e in empleados: print(e)
#            departamentos = DepartamentoDAO.Seleccionar()
#            for d in departamentos: print(d)
#
#        except Exception as e:
#            print(f'Error: {e}') 
#
#        finally: 
#            if conexion is not None: 
#                cursor.close()
#                Conexion.liberar_conexion(conexion)


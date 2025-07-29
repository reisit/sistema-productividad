from funciones.Conexion import Conexion
from funciones.empleados import Empleados

def EmpleadosTabla():
    conexion = None
    try:
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM empleados')
        return ([e for e in cursor.fetchall()])

    except Exception as e:
        print(f'Error: {e}')

    finally: 
        if conexion is not None: 
            cursor.close()
            Conexion.liberar_conexion(conexion)


class Tareas:

    empleados = EmpleadosTabla()

    def __init__(self,id= None,descripcion = None,fechaAsignacion = None,fechaEntrega = None,
                 estado = None,empleadoId = None, empleados = empleados):

        if empleadoId not in [empleados[i][0] for i in range(len(empleados))] or estado not in ['pendiente','en progreso','completada']:
            raise ValueError('Valor invalido')

        self.id = id
        self.descripcion = descripcion
        self.fechaAsignacion = fechaAsignacion
        self.fechaEntrega = fechaEntrega
        self.estado = estado
        self.empleadoId = empleadoId

    def __str__(self):
        atributos = [self.id,self.descripcion,self.fechaAsignacion,self.fechaEntrega,self.estado,self.empleadoId]
        return ' - '.join([str(v) for v in atributos if v is not None])
    

    def empleado(self, empleados = empleados):
        e = [e for e in empleados if e[0] == self.id][0]
        empleado = Empleados(e[0], e[1], e[2],e[3],e[4])
        print (empleado)

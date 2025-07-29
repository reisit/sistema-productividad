from funciones.Conexion import Conexion
from funciones.empleados import Empleados


def validarDepartamento():
    from funciones.departamentosDAO import DepartamentoDAO
    while True:
        id = int(input('Insertar id del departamento: '))
        if id not in [d.id for d in DepartamentoDAO.Seleccionar()]: print('id del departamento invalido')
        else: break
    return id


class EmpleadosDAO:
    SELECCIONAR = 'SELECT * FROM empleados'
    INSERTAR = 'INSERT INTO empleados(nombre,cargo,salario,depId) VALUES(%s,%s,%s,%s)'
    ACTUALIZAR = 'UPDATE empleados SET nombre=%s, cargo=%s, salario=%s, depId=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM empleados WHERE id =%s'
    ELIMINAR_DEPID = 'DELETE FROM empleados WHERE depId=%s'

    @classmethod
    def Seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            empleados = [Empleados(e[0],e[1],e[2],e[3],e[4]) for e in cursor.fetchall()]
            return empleados
        
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
            n = input('Insertar nombre del empleado: ')
            c = input('Insertar el cargo: ')
            s = int(input('Insertar el salario: '))
            d = validarDepartamento()
            values = (n,c,s,d)
            cursor.execute(cls.INSERTAR,values)
            e = Empleados(nombre=n,cargo=c,salario=s,depId=d)
            input(f'Empleado creado satisfactoriamente!: \n{e}')
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
            i = int(input('Ingresar id del empleado a modificar: '))
            n = input('Insertar nombre del empleado: ')
            c = input('Insertar el cargo: ')
            s = int(input('Insertar el salario: '))
            d = validarDepartamento()
            values = (n,c,s,d,i)
            cursor.execute(cls.ACTUALIZAR,values)
            e = Empleados(id=i,nombre=n,cargo=c,salario=s,depId=d)
            print(f'Cliente modificado satisfactoriamente!: \n{e}')
            conexion.commit()
        
        except Exception as e:
            print(f'Error: {e}') 

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def Eliminar(cls):
        from funciones.tareasDAO import TareasDAO
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            i = int(input('Insertar id a eliminar: '))

            TareasDAO.EliminarEmpleadoID(id=i)

            values = (i,)
            cursor.execute(cls.ELIMINAR,values)
            print('Empleado eliminado exitosamente')
            conexion.commit()
        
        except Exception as e:
            print(f'Error: {e}') 

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def EliminarDepID(cls, id = None):
        from funciones.tareasDAO import TareasDAO
        from funciones.departamentosDAO import DepartamentoDAO
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            if id is None:
                id = validarDepartamento()
            elif id not in [d.id for d in DepartamentoDAO.Seleccionar()]:
                return f'Valor invalido, insertar id correctamente'

            for e in EmpleadosDAO.Seleccionar():
                if (e.depId == id): TareasDAO.EliminarEmpleadoID(id=e.id)
            
            values = (id,)
            cursor.execute(cls.ELIMINAR_DEPID,values)
            print('Empleados eliminados correctamente exitosamente')
            conexion.commit()
        
        except Exception as e:
            print(f'Error: {e}') 

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)


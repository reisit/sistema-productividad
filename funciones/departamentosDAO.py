from funciones.Conexion import Conexion
from funciones.departamentos import Departamento

class DepartamentoDAO:
    SELECCIONAR = 'SELECT * FROM departamentos'
    INSERTAR = 'INSERT INTO departamentos(nombre) VALUES(%s)'
    ACTUALIZAR = 'UPDATE departamentos SET nombre=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM departamentos WHERE id =%s'

    @classmethod
    def Seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            departamentos = [Departamento(d[0],d[1]) for d in cursor.fetchall()]
            return departamentos
        
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
            n = input('Insertar nombre del departamento: ')
            values = (n,)
            cursor.execute(cls.INSERTAR,values)
            d = Departamento(nombre=n)
            print(f'Departamento creado satisfactoriamente!: \n{d}')
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
            i = int(input('Ingresar id del departamento a modificar: '))
            n = input('Insertar nombre: ')
            values = (n,i)
            cursor.execute(cls.ACTUALIZAR,values)
            d = Departamento(id=i,nombre=n)
            print(f'Cliente modificado satisfactoriamente!: \n{d}')
            conexion.commit()
        
        except Exception as e:
            print(f'Error: {e}') 

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def Eliminar(cls):
        from funciones.empleadosDAO import EmpleadosDAO
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            i = int(input('Insertar id a eliminar: '))

            EmpleadosDAO.EliminarDepID(id = i)

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
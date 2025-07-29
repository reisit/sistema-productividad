from funciones.Conexion import Conexion
from funciones.departamentos import Departamento

def Departamentos():
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM departamentos')
            return [d for d in cursor.fetchall()]

        except Exception as e:
            print(f'Error: {e}')

        finally: 
            if conexion is not None: 
                cursor.close()
                Conexion.liberar_conexion(conexion)


class Empleados:

    departamentos = Departamentos()
    
    def __init__(self, id=None, nombre=None, cargo=None, salario=None, depId=None, dep = departamentos):

        if depId not in [d[0] for d in dep]: raise ValueError('Dato invalido')

        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.depId = depId

    def __str__(self):
        atributos = [self.id,self.nombre,self.cargo,self.salario,self.depId]
        return ' - '.join([str(v) for v in atributos if v is not None])
    
    def departamento(self, departamentos = departamentos):
        dep = [d for d in departamentos if d[0] == self.depId][0]
        d = Departamento(dep[0], dep[1])
        print(d)

    
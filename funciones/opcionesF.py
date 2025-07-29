from funciones.departamentosDAO import DepartamentoDAO
from funciones.empleadosDAO import EmpleadosDAO, validarDepartamento
from funciones.tareasDAO import TareasDAO, validarEmpleadoID

def ejecutar(dao):
    def decorador(func):
        def wrapper(cls):
            datos = dao.Seleccionar()
            if datos: func(cls)
            else: print(f"No hay datos en la base de datos")
            input("Presione Enter para continuar...")
        return wrapper
    return decorador

def eEmpleado(id = None):
    empleados = EmpleadosDAO.Seleccionar()
    for e in empleados: print(e)
    
    if id == None:
        for e in empleados: print(e)
        id = validarEmpleadoID()

    empleado = next(e for e in empleados if e.id == id)
    completadas, enProgreso, pendientes = [], [], []
    [completadas.append(t) if t.estado == 'completada' else enProgreso.append(t) if t.estado == 'en progreso' else pendientes.append(t) for t in TareasDAO.Seleccionar() if t.empleadoId == empleado.id]

    efectividad = ((len(completadas) * 1) + (len(enProgreso) * 0.5) + (len(pendientes) * 0)) / (len(completadas) + len(enProgreso) + len(pendientes)) * 100

    print(f"Efectividad - {empleado.nombre}: {efectividad}%")
    return efectividad


def eDepartamento():
    departamentos = DepartamentoDAO.Seleccionar()
    for d in departamentos: print(d)
    id = validarDepartamento()

    l = [eEmpleado(empleado.id) for empleado in EmpleadosDAO.Seleccionar() if empleado.depId == id]
    efectividad = sum(l) / len(l) if l else 0

    print(f"Efectividad - {next(d.nombre for d in DepartamentoDAO.Seleccionar() if d.id == id)}: {efectividad}%")
    return efectividad


class Mostrar:

    @classmethod
    @ejecutar(DepartamentoDAO)
    def _departamentos(cls):
        for d in DepartamentoDAO.Seleccionar(): print(d)

    @classmethod
    @ejecutar(EmpleadosDAO)
    def _empleados(cls):
        for e in EmpleadosDAO.Seleccionar(): print(e)

    @classmethod
    @ejecutar(TareasDAO)
    def _tareas(cls):
        for t in TareasDAO.Seleccionar(): print(t)

class Insertar:

    @classmethod
    def _departamentos(cls):
        DepartamentoDAO.Insertar()

    @classmethod
    def _empleados(cls):
        EmpleadosDAO.Insertar()

    @classmethod
    def _tareas(cls):
        TareasDAO.Insertar()

class Actualizar:

    @classmethod
    @ejecutar(DepartamentoDAO)
    def _departamentos(cls):
        for d in DepartamentoDAO.Seleccionar(): print(d)
        DepartamentoDAO.Actualizar()

    @classmethod
    @ejecutar(EmpleadosDAO)
    def _empleados(cls):
        for e in EmpleadosDAO.Seleccionar(): print(e)
        EmpleadosDAO.Actualizar()

    @classmethod
    @ejecutar(TareasDAO)
    def _tareas(cls):
        for t in TareasDAO.Seleccionar(): print(t)
        TareasDAO.Actualizar()

class Eliminar:

    @classmethod
    @ejecutar(DepartamentoDAO)
    def _departamentos(cls):
        for d in DepartamentoDAO.Seleccionar(): print(d)
        DepartamentoDAO.Eliminar()

    @classmethod
    @ejecutar(EmpleadosDAO)
    def _empleados(cls):
        for e in EmpleadosDAO.Seleccionar(): print(e)
        EmpleadosDAO.Eliminar()

    @classmethod
    @ejecutar(TareasDAO)
    def _tareas(cls):
        for t in TareasDAO.Seleccionar(): print(t)
        TareasDAO.Eliminar()

class Efectividad:
    
    @classmethod
    @ejecutar(DepartamentoDAO)
    def _departamentos(cls):
        eDepartamento()

    @classmethod
    @ejecutar(EmpleadosDAO)
    def _empleados(cls):
        eEmpleado(id = None)

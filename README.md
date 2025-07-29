# Sistema de Productividad

Este es mi primer proyecto en GitHub, desarrollado con **Python** y **MySQL**. El objetivo es administrar información relacionada con departamentos, empleados y tareas, permitiendo operaciones CRUD completas y un cálculo personalizado de efectividad.

---

## Características principales

- **Base de datos MySQL** con tres tablas:
  - `departamentos`
  - `empleados`
  - `tareas`
- **Inicializador con menú interactivo**
  - Configuración manual o automática (`config.json`)
  - Creación de esquema y tablas vacías o precargadas
  - Opción para borrar completamente el esquema
- **Menú principal con interfaz modular**
  - Mostrar / Insertar / Actualizar / Eliminar datos
  - Cálculo de efectividad por empleados y departamentos
- **Control de claves foráneas**
  - Borrado en cascada entre empleados y tareas, y entre departamentos y empleados

---

## Estructura del proyecto

sistema_productividad/ ├── inicializador/ │ ├── config.json │ ├── init1.sql │ ├── init2.sql │ └── opciones.py ├── menu/ │ ├── Conexion.py │ ├── departamentos.py │ ├── empleados.py │ ├── tareas.py │ ├── departamentosDAO.py │ ├── empleadosDAO.py │ ├── tareasDAO.py │ └── opciones.py


---

## Cálculo de efectividad

- **Empleados**:  
  

Efectividad = ((#Completadas × 1) + (#En Progreso × 0.5)) / (Total de tareas) × 100


- **Departamentos**:  
  Promedio del porcentaje de efectividad individual de sus empleados.

---

## Cómo iniciar el proyecto

1. Asegúrate de tener **Python 3.10+** y **MySQL Server** instalado.
2. Instala las dependencias necesarias:

   ```bash
   pip install ansiwrap console-menu mysql-connector-python sasl2 six textwrap

## Ejecuta el menú inicializador:
   ```
    python inicializador/opciones.py
   ```

Opción 1: Cargar o modificar configuración de conexión
Elegir entre valores predeterminados o personalizados

Opción 2: Crear la base de datos
Vacía o precargada con usuarios y datos

Opción 3: Eliminar el esquema completamente

## Ejecutar el menú principal
  ```
    python menu/opciones.py
  ```
Los valores de host, usuario, contraseña y puerto se almacenan en config.json. Puedes generarlos automáticamente desde el inicializador.

## Valores predeterminados:
{
  "host": "localhost",
  "user": "root",
  "password": "admin",
  "port": 3306
}


## Notas importantes


- Al eliminar un empleado, sus tareas se eliminan automáticamente.
- Al eliminar un departamento, se eliminan sus empleados y las tareas asociadas.
- La efectividad solo se calcula para empleados y departamentos.

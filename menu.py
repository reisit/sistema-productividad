from consolemenu import ConsoleMenu
from consolemenu.items import SubmenuItem, FunctionItem
from funciones.opcionesF import *


clasesOperaciones = {
    "Mostrar datos": Mostrar,
    "Insertar datos": Insertar,
    "Actualizar datos": Actualizar,
    "Eliminar datos": Eliminar,
}

categorias  = ["departamentos", "empleados", "tareas"]

submenus = []

for nombre, clase in clasesOperaciones.items():
    submenu = ConsoleMenu(nombre, "Opciones")

    for tabla in categorias:
        funcion = getattr(clase, f"_{tabla}")
        submenu.append_item(FunctionItem(tabla.capitalize(), funcion))
    
    submenus.append(SubmenuItem(nombre, submenu))

submenu = ConsoleMenu("Efectividad", "Opciones")
submenu.append_item(FunctionItem("Departamentos", Efectividad._departamentos))
submenu.append_item(FunctionItem("Empleados", Efectividad._empleados))
submenus.append(SubmenuItem("Efectividad",submenu))


menu = ConsoleMenu("Menú Principal")

for item in submenus: 
    menu.append_item(item)

menu.show()


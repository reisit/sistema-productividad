from consolemenu import ConsoleMenu
from consolemenu.items import SubmenuItem, FunctionItem
from inicializacion.opcionesI import *

opciones = []

submenu = ConsoleMenu("Cargar/Actualizar Datos", "Opciones")
submenu.append_item(FunctionItem(f"Datos Default\n\t[host: localhost,\n\tuser: root,\n\tpassword: admin,\n\tport: 3306]", cargarDefault))
submenu.append_item(FunctionItem("Datos Personalizados", cargarDatos))
opciones.append(SubmenuItem("Cargar/Actualizar Datos",submenu))

submenu = ConsoleMenu("Crear Base de Datos", "Opciones")
submenu.append_item(FunctionItem(f"Crear sin usuarios", lambda: init(1)))
submenu.append_item(FunctionItem(f"Crear con usuarios ya creados", lambda: init(2)))
opciones.append(SubmenuItem("Crear Base de Datos",submenu))

opciones.append(FunctionItem(f"Borrar bases de datos ", drop))

menu = ConsoleMenu("Inicializador")

for item in opciones: 
    menu.append_item(item)

menu.show()
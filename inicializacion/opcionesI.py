import json
import mysql.connector


def init(v):

    with open("inicializacion/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    host = config["host"]
    user = config["user"]
    password = config["password"]
    port = config["port"]

    if config["Inicializador"] == 0:
        while True:
            op = input(f"Los datos no han sido cargados\nDesea crear la tabla con los datos default?\n\thost: {host},\n\tuser: {user},\n\tpassword: {password},\n\tport: {port}\nOpcion (Y/N): ")
            if op.capitalize() not in ['Y','N']: print('Error al ingresar la opcion')
            else: break
        
        if op.capitalize() == 'N': return 0

    conexion = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    cursor = conexion.cursor()

    with open(f"inicializacion/init{v}.sql", "r", encoding="utf-8") as archivo_sql:
        script = archivo_sql.read()

    for sentencia in script.split(";"):
        if sentencia.strip(): 
            try:
                cursor.execute(sentencia)
            except Exception as e:
                print(f"Error ejecutando sentencia:\n{sentencia}\n→ {e}")

    conexion.commit()
    cursor.close()
    conexion.close()

    print("Base de datos inicializada.")
    input("Presione Enter para continuar...")

def guardarConfigJson(ruta, host, user, password, port):
    config = {
        "host": host,
        "user": user,
        "password": password,
        "database": "sistema_productividad",
        "port": port,
        "Inicializador": 1
    }
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(config, f)
    print('Datos guardados')
    input("Presione Enter para continuar...")

def cargarDatos():
    host = input("Ingrese el host (default - localhost): ")
    user = input("Ingrese el usuario (default - root): ")
    password = input("Ingrese la contraseña (default - admin): ")
    port = input("Ingresar port (default - 3306): ")

    guardarConfigJson("inicializacion/config.json", host, user, password, port)

def cargarDefault():
    config = {
        "host": "localhost",
        "user": "root",
        "password": "admin",
        "database": "sistema_productividad",
        "port": "3306",
        "Inicializador": 0
    }
    with open("inicializacion/config.json", "w", encoding="utf-8") as f:
        json.dump(config, f)
    print('Datos reseteados')
    input("Presione Enter para continuar...")

def drop():

    with open("inicializacion/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    conexion = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"]
    )

    cursor = conexion.cursor()
    try:
        cursor.execute("SHOW DATABASES LIKE 'sistema_productividad'")
        if cursor.fetchone():
            cursor.execute("DROP DATABASE `sistema_productividad`;")
        else:
            print("La base de datos no existe.")
    except Exception as e:
        print(f"Error: {e}")
    conexion.commit()
    cursor.close()
    conexion.close()

    input("Base de datos borrada exitosamente")

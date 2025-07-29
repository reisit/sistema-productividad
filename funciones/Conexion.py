from mysql.connector import pooling
from mysql.connector import Error
import json

with open("inicializacion/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

class Conexion:
    DATABASE = config["database"]
    USERNAME = config["user"]
    PASSWORD = config["password"]
    DB_PORT = config["port"]
    HOST = config["host"]
    POOL_SIZE = 5
    POOL_NAME = 'sistemaPool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                print(f'Nombre del pool: {cls.pool.pool_name}')
                print(f'Tamaño del pool: {cls.pool.pool_size}')
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al inicializar el pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls,conexion):
        conexion.close()

if __name__ == '__main__':
    #pool = Conexion.obtener_pool()
    #print(pool)
    cnx1 = Conexion.obtener_conexion()
    print(cnx1)
    Conexion.liberar_conexion(cnx1)
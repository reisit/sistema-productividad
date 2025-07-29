class Departamento:

    def __init__(self,id=None,nombre=None):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        atributos = [self.id,self.nombre]
        return ' - '.join([str(v) for v in atributos if v is not None])
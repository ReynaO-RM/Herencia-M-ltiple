class Departamento:
    def __init__(self):
        self._nombreDepa = ""
        self._direccion = ""
        self._id = 0

    # Getters y Setters
    def getNombreDepa(self):
       return self._nombreDepa

    def setNombreDepa(self, nombreDepa):
        self._nombreDepa = nombreDepa

    def getDireccion(self):
        return self._direccion

    def setDireccion(self, direccion):
        self._direccion = direccion

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def mostrarInfoDepartamento(self):
        return f"Nombre del departamento: {self._nombreDepa},Id: {self._id}, Direccion: {self._direccion}"
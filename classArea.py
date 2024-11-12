from classDepartamento import Departamento

class Area(Departamento):
    def __init__(self):
        super().__init__()
        self._nombreA = ""
        self._ubicacion = ""
        self._turno = ""

    # Getter y Setter
    def getNombreA(self):
        return self._nombreA

    def setNombreA(self, nombreA):
        self._nombreA = nombreA

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getTurno(self):
        return self._turno

    def setTurno(self, turno):
        self._turno = turno

    def mostrarInfoArea(self):
        parent2Info = super().mostrarInfoDepartamento()
        return f"{parent2Info}, Nombre del área: {self._nombreA}, Ubicacion: {self._ubicacion}, Turno: {self._turno}"
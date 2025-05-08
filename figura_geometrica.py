class FiguraGeometrica:
    def __init__(self, alto=0, ancho=0):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        self._alto = valor

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor

    def __str__(self):
        return f"Figura Geometrica: {self.__dict__.__str__()}"

if __name__ == "__main__":
    fg1 = FiguraGeometrica(alto=4, ancho=6)
    print(fg1)
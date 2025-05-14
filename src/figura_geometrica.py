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

    def area(self):
        return (self.alto * self.ancho)

    def perimetro(self):
        return (2 * self.alto + 2 * self.ancho)

    def __str__(self):
        return f"Figura Geometrica: {self.__dict__.__str__()}"

if __name__ == "__main__":
    fg1 = FiguraGeometrica(alto=4, ancho=6)
    print(fg1)
    print(f'Area: {fg1.area()}')
    print(f'Perimetro: {fg1.perimetro()}')
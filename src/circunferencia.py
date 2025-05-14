import math

from src.color import Color
from src.figura_geometrica import FiguraGeometrica


class Circunferencia(FiguraGeometrica, Color):
    def __init__(self, radio=0, color=None):
        FiguraGeometrica.__init__(self, ancho=radio, alto=0)
        Color.__init__(self, nombre=color)

    def __str__(self):
        return f'Circunferencia-> [radio={self.ancho}, color: {self._color}]'

    def area(self):
        return math.pi * self.ancho * self.ancho

    def perimetro(self):
        return math.pi * 2 * self.ancho

if __name__ == '__main__':
    c1 =  Circunferencia(color='red', radio=5)
    print(c1)
    print(f'Area: {c1.area()}')
    print(f'Perimetro: {c1.perimetro()}')
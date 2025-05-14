from src.circunferencia import Circunferencia
from src.cuadrado import Cuadrado
from src.rectangulo import Rectangulo

c1 = Cuadrado(lado=6, color= "Rojo")
c2 = Cuadrado(lado=7, color= "Amarillo")
c3 = Cuadrado(lado=8, color= "Blanco")
c4 = Cuadrado(lado=9, color= "Verde")
c5 = Cuadrado(lado=4, color= "Negro")
r1 = Rectangulo(alto=8, ancho=7, color= "Negro")
r2 = Rectangulo(alto=2, ancho=6, color= "Verde")
r3 = Rectangulo(alto=1, ancho=6, color= "Blanco")
r4 = Rectangulo(alto=4, ancho=5, color= "Rojo")
r5 = Rectangulo(alto=7, ancho=9, color= "Amarillo")
circ = Circunferencia(radio=9, color='Rojo')


def calcular_dimensiones(lista):
    for fg in lista:
        if isinstance(fg, Rectangulo):
            print('Rectangulo')
        elif isinstance(fg, Cuadrado):
            print('Cuadrado')
        print(fg)
        print(f'Area: {fg.area()}')
        print(f'Perimetro: {fg.perimetro()}')
        print('*'.center(50, '*'))



lista_fg = [c1, r1, c2, c3, c4, c5, r2, r3, r4, r5, circ]
calcular_dimensiones(lista_fg)


class Color:
    def __init__(self, nombre):
        self._color = nombre

    def __str__(self):
        return f'Color: {self.__dict__.__str__()}'

    @property
    def nombre(self):
        return self._color

    @nombre.setter
    def nombre(self, nombre):
        self._color = nombre

if __name__ == '__main__':
    c1 = Color('Rojo')
    print(c1)
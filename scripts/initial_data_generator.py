from automoviles.models import Automovil, Marca

import random
import string
from random import randint


def random_polarizado():
    return bool(random.getrandbits(1))


def random_modelo():
    return randint(1975, 2016)


def random_color():
    colores = [
        'AliceBlue',
        'AntiqueWhite',
        'Aqua',
        'Aquamarine',
        'Azure',
        'Beige',
        'Bisque',
        'Black',
        'BlanchedAlmond',
        'Blue',
        'BlueViolet',
        'Brown',
        'BurlyWood',
        'CadetBlue',
        'Chartreuse',
        'Chocolate',
        'Coral',
        'CornflowerBlue',
        'Cornsilk',
        'Crimson',
        'Cyan',
        'DarkBlue',
        'DarkCyan',
        'DarkGoldenRod',
        'DarkGray',
        'DarkGrey',
        'DarkGreen',
        'DarkKhaki',
        'DarkMagenta',
        'DarkOliveGreen',
        'DarkOrange',
        'DarkOrchid',
        'DarkRed',
        'DarkSalmon',
        'DarkSeaGreen',
        'DarkSlateBlue',
        'DarkSlateGray',
        'DarkSlateGrey',
        'DarkTurquoise',
        'DarkViolet',
        'DeepPink',
        'DeepSkyBlue',
        'DimGray',
        'DimGrey',
        'DodgerBlue',
        'FireBrick',
        'FloralWhite',
        'ForestGreen',
        'Fuchsia',
        'Gainsboro',
        'GhostWhite',
        'Gold',
        'GoldenRod',
        'Gray',
        'Grey',
        'Green',
        'GreenYellow',
        'HoneyDew',
        'HotPink'
    ]
    return colores[randint(0, 58)]


def random_linea_mazda():
    lineas = [
        'Mazda 2',
        'Mazda 3',
        'Mazda 5',
        'Mazda 6',
        'CX-5',
        'CX-7',
        'CX-9'
    ]
    return random.choice(lineas)


def random_linea_toyota():
    lineas = [
        'Yaris',
        'Corolla',
        'Hilux',
        'Scion',
        'Lexus',
        'Rav4',
        'Prado',
        'Fortuner'
    ]
    return random.choice(lineas)


def random_placa():
    l1 = random.choice(string.ascii_uppercase)
    l2 = random.choice(string.ascii_uppercase)
    l3 = random.choice(string.ascii_uppercase)
    n1 = str(randint(0, 9))
    n2 = str(randint(0, 9))
    n3 = str(randint(0, 9))
    return 'P' + l1 + l2 + l3 + n1 + n2 + n3


m1 = Marca(
    nombre='Toyota',
    pais='Japon',
    fechaOrigen='1937-08-28'
)

m2 = Marca(
    nombre='Mazda',
    pais='Japon',
    fechaOrigen='1920-01-30'
)

m1.save()
m2.save()

for i in range(1000):
    if i < 100:
        a = Automovil(
            marca=m2,
            color=random_color(),
            modelo=random_modelo(),
            linea=random_linea_mazda(),
            placa=random_placa(),
            polarizado=random_polarizado()
        )
        a.save()
        continue
    a = Automovil(
        marca=m1,
        color=random_color(),
        modelo=random_modelo(),
        linea=random_linea_toyota(),
        placa=random_placa(),
        polarizado=random_polarizado()
    )
    a.save()

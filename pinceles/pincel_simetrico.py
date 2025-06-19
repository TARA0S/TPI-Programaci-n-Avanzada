import random
from .pincel_base import Pincel

class PincelSimetrico(Pincel):
    def dibujar(self, lienzo):
        mitad = lienzo.ancho // 2
        for y in range(lienzo.alto):
            fila = [random.choice(self.caracteres) for _ in range(mitad)]
            reflejo = fila[::-1]
            if lienzo.ancho % 2 != 0:
                fila.append(random.choice(self.caracteres))
            completa = fila + reflejo
            for x, char in enumerate(completa):
                lienzo.pintar_pixel(x, y, char)

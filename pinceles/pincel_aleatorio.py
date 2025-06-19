import random
from .pincel_base import Pincel

class PincelAleatorio(Pincel):
    def dibujar(self, lienzo):
        for y in range(lienzo.alto):
            for x in range(lienzo.ancho):
                char = random.choice(self.caracteres)
                lienzo.pintar_pixel(x, y, char)

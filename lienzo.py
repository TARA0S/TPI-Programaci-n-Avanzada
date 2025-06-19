from colorama import Fore, Style

color_map = {
    "░": Fore.RED,
    "▒": Fore.BLUE,
    "▓": Fore.GREEN,
    "█": Fore.YELLOW
}

class Lienzo:
    def __init__(self, ancho: int, alto: int):
        self.ancho = ancho
        self.alto = alto
        self.grilla = [[" " for _ in range(ancho)] for _ in range(alto)]

    def pintar_pixel(self, x: int, y: int, char: str):
        if 0 <= x < self.ancho and 0 <= y < self.alto:
            self.grilla[y][x] = char

    def mostrar(self):
        for fila in self.grilla:
            for char in fila:
                color = color_map.get(char, Fore.WHITE)
                print(color + char, end="")
            print(Style.RESET_ALL)

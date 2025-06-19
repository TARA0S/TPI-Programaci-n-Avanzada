from abc import ABC, abstractmethod

class Pincel(ABC):
    def __init__(self, caracteres=None):
        self.caracteres = caracteres or ["░", "▒", "▓", "█"]

    @abstractmethod
    def dibujar(self, lienzo):
        pass

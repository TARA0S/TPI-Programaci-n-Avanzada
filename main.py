from lienzo import Lienzo
from colorama import init
from pinceles.pincel_aleatorio import PincelAleatorio
from pinceles.pincel_simetrico import PincelSimetrico

init(autoreset=True)

def main():
    ancho = int(input("Ancho del lienzo: "))
    alto = int(input("Alto del lienzo: "))

    print("\nElegí el tipo de pincel:")
    print("1. Aleatorio")
    print("2. Simétrico")
    opcion = input("> ")

    if opcion == "2":
        pincel = PincelSimetrico()
    else:
        pincel = PincelAleatorio()

    lienzo = Lienzo(ancho, alto)
    pincel.dibujar(lienzo)
    lienzo.mostrar()

    print("Generación completada con éxito.")

if __name__ == "__main__":
    main()

from funciones import *

def main():
    ingresando = True
    while ingresando:
        elementos, potencia = ingresar()
        print('\nLa ecuacion es:')
        imprimir_ecuacion(elementos, imprimir_potencia=True ,potencia = potencia)
        text = '1.- Si\n2.- No\n'
        res = input(text)
        if res == '1': 
            ingresando = False
    solucion = resolver(elementos, potencia)
    print()
    print('La solucion es: ', end='')
    imprimir_ecuacion(solucion)

if __name__ == '__main__':
    main()
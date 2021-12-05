from modulo_font import *
import os

color = ColorFont()
def MenuInicio():
    os.system("clear")
    print(color.AMARILLO + "++++++++++++++++++++++++++++++++")
    print("+                              +")
    print("+  BIENVENIDO A LA APLICACION  +")
    print("+  DE MANIPULACION DE ARBOLES  +")
    print("+                              +")
    print("++++++++++++++++++++++++++++++++")    
    print()
    print(color.UNDERLINE + "MENU DE OPCIONES:" + color.RESET)
    print()
    print(color.AMARILLO + "1-CARGAR DATOS")
    print("2-IMPRIMIR DATOS")
    print("3-COMPARAR ESTRUCTURAS")
    print("4-CONTAR HOJAS")
    print("5-NODO HERMANO")
    print("6-NODO PADRE")
    print("7-SALIR" + color.RESET)
    print()
    
def MenuImpresion():
    print()
    print(color.AMARILLO + color.UNDERLINE + color.UNDERLINE + "IMPRESION DE DATOS:" + color.RESET)
    print()
    print(color.AMARILLO + "1-IMPRIMIR PRE-ORDEN")
    print("2-IMPRIMIR POST-ORDEN")
    print("3-IMPRIMIR IN-ORDEN")
    print("4-VOLVER MENU" + color.RESET)
    
def VolverMenu():
    char = ''
    while char != 'M':
        char = input(color.BOLD + "Presione ['M'] y [ENTER] para volver al Menu... => " + color.RESET)
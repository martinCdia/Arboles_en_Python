from modulo_arbol import * #IMPORTA EL MODULO QUE CONTIENE CLASE ARBOL
from modulo_menu import * #IMPORTA MODULO QUE CONTIENE LOS MENUES
from modulo_font import * #IMPORTA MODULO CON LOS FORMATOS DE IMPRESION
import os

def OpcionesCargar(arbol):
    #LLAMA AL METODO PARA AGREGAR DATOS AL ARBOL
    cant = int(input(color.BOLD + color.GRIS + color.GRIS + color.CURSIVA + "CANTIDAD DE DATOS A INGRESAR: " + color.RESET))
    for i in range (cant):
        print()
        dato = int(input("DATO => "))
        arbol.AgregarDatos(dato)
        i += 1
            
def MenuImprimir(arbol):
    #DEPENDIENDO DE LA OPCION ELEJIDA, LLAMA AL METODO CORRESPONDIENTE PARA IMPRIMIR
    os.system("clear")
    color = ColorFont()
    salir = False
    print(color.AMARILLO + "[2-IMPRIMIR DATOS]" + color.RESET)
    print()
    MenuImpresion()
    while not salir:
        print()
        print()
        try:
            opc = int(input(color.CURSIVA + color.BOLD + color.GRIS + "OPCION => " + color.RESET))
            print()
            if opc == 1:
                print(color.BOLD + color.UNDERLINE + "PRE-ORDEN:" + color.RESET)
                arbol.ImprimirPreOrden(arbol)
            elif opc == 2:
                print(color.BOLD + color.UNDERLINE + "POST-ORDEN:" + color.RESET)
                arbol.ImprimirPostOrden(arbol)
                
            elif opc == 3:
                print(color.BOLD + color.UNDERLINE + "IN-ORDEN:" + color.RESET)
                arbol.ImprimirInOrden(arbol)
                
            elif opc == 4:
                salir = True
            else:
                print("OPCION INCORRECTA")
        except ValueError:
            print("OPCION NO VALIDA!!")
            
def CompararArboles(arbol_a, arbol_b):
    #LLAMA AL METODO QUE DETERMINA SI DOS ARBOLES SON ISOMORFOS
    os.system("clear")
    print(color.AMARILLO + "[3-COMPARAR ESTRUCTURAS]" + color.RESET)
    print()
    print()
    print(color.CURSIVA + "ARBOL 1:" + color.RESET)
    print("=======")
    print(color.CURSIVA + color.GRIS + "NODO RAIZ => " + "[" + str(arbol_a.NodoRaiz(arbol_a)) + "]" + color.RESET)
    arbol_a.ImprimirInOrden(arbol_a)
    print()
    print()
    print(color.CURSIVA + "ARBOL 2:" + color.RESET)
    print("========")
    print(color.CURSIVA + color.GRIS + "NODO RAIZ => " + "[" + str(arbol_b.NodoRaiz(arbol_b)) + "]" + color.RESET)
    arbol_b.ImprimirInOrden(arbol_b)
    print()
    print()
    if arbol_a.Isomorfos(arbol_a, arbol_b):
        print(color.AMARILLO + color.GRIS + color.BOLD + "SON ISOMORFOS" + color.RESET)
    else:
        print(color.AMARILLO + color.GRIS + color.BOLD + "NO SON ISOMORFOS" + color.RESET)
        
def ContarHojas(arbol):
    #LLAMA AL METODO PARA DETERMINAR LA CANTIDAD DE HOJAS DE UN ARBOL
    print()
    print(color.CURSIVA + "ARBOL:")
    print("======" + color.RESET)
    print(color.GRIS + "NODO RAIZ => " + "[" + str(arbol.NodoRaiz(arbol)) + "]" + color.RESET)
    arbol.ImprimirInOrden(arbol)
    print()
    print()
    if arbol.dato != None:
        print(color.AMARILLO + color.GRIS + color.CURSIVA + "CANTIDAD DE HOJAS => " + "[" + str(arbol.NodosHojas(arbol)) + "]" + color.RESET)
    else:
        print(color.ROJO + "EL ARBOL ESTA VACIO" + color.RESET)
        print()
    
def DeterminaHermano(arbol):
    #LLAMA AL METODO PARA DETERMINAR EL HERMANO DE UN NODO CUALQUIERA
    print()
    print(color.CURSIVA + "ARBOL:")
    print("======" + color.RESET)
    print(color.GRIS + "NODO RAIZ => " + "[" + str(arbol.NodoRaiz(arbol)) + "]" + color.RESET)
    arbol.ImprimirInOrden(arbol)
    print()
    print()
    if arbol.dato != None:
        nodo = int(input(color.BOLD + color.GRIS + color.CURSIVA + "INGRESE UN NODO PARA DETERMINAR SU HERMANO => " + color.RESET))
        print()
        print()
        print(color.AMARILLO + color.GRIS + color.CURSIVA)
        arbol.NodoHermano(arbol, nodo)
        print(color.RESET)
    else:
        print(color.ROJO + "EL ARBOL ESTA VACIO" + color.RESET)
        print()
    
def DeterminaPadre(arbol):
    #LLAMA AL METODO QUE DETERMINA EL PADRE DE UN NODO CUALQUIERA
    print()
    print(color.CURSIVA + "ARBOL:")
    print("======" + color.RESET)
    print(color.GRIS + "NODO RAIZ => " + "[" + str(arbol.NodoRaiz(arbol)) + "]" + color.RESET)
    arbol.ImprimirInOrden(arbol)
    print()
    print()
    if arbol.dato != None:
        nodo = int(input(color.BOLD + color.GRIS + color.CURSIVA + "INGRESE UN NODO PARA DETERMINAR SU PADRE => " + color.RESET))
        print()
        print(color.AMARILLO + color.GRIS + color.CURSIVA)
        arbol.NodoPadre(arbol, nodo)
        print(color.RESET)
    else:
        print(color.ROJO + "EL ARBOL ESTA VACIO" + color.RESET)
        print()
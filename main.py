from modulo_arbol import * #IMPORTA EL MODULO QUE CONTIENE CLASE ARBOL
from modulo_funciones import * #IMPORTA EL MODULO QUE CONTIENE TODAS LAS FUNCIONES 
from modulo_menu import * #IMPORTA MODULO QUE CONTIENE LOS MENUES
from modulo_font import * #IMPORTA MODULO CON LOS FORMATOS DE IMPRESION
import os


salir = False
arbol1 = Arbol(None)
MenuInicio()
color = ColorFont()
while not salir:
    try:
        opc = int(input(color.CURSIVA + color.BOLD + color.GRIS + "INGRESE UNA OPCION DEL MENU => " + color.RESET))
        if opc == 1:
            #CARGA DATOS AL ARBOL
            os.system("clear")
            print(color.AMARILLO + "[1-CARGAR DATOS]" + color.RESET)
            print()
            OpcionesCargar(arbol1)
            MenuInicio()
        elif opc == 2:
            #IMPRIME LOS DATOS DEL ARBOL
            MenuImprimir(arbol1)
            MenuInicio()
        elif opc == 3:
            #CREA OBJETO ARBOL2 PARA CARGAR DATOS Y COMPARAR ESTRUCTURAS DE ARBOLES
            arbol2 = Arbol(None)
            os.system("clear")
            print(color.AMARILLO + "[3-COMPARAR ESTRUCTURAS]" + color.RESET)
            print()
            print(color.AMARILLO + color.GRIS + "++++++++++++")
            print("+  ARBOL2  +")
            print("++++++++++++" + color.RESET)
            print()
            OpcionesCargar(arbol2)
            CompararArboles(arbol1, arbol2)
            print()
            VolverMenu()
            MenuInicio()        
        elif opc == 4:
            #CUENTA LAS CANTIDADES DE HOJAS DEL ARBOL
            os.system("clear")
            print(color.AMARILLO + "[4-CONTAR HOJAS]" + color.RESET)
            print()
            ContarHojas(arbol1)
            print()
            VolverMenu()
            MenuInicio()        
        elif opc == 5:
            #DETERMINA EL HERMANO DE UN NODO CUALQUIERA
            os.system("clear")
            print(color.AMARILLO + "[5-NODO HERMANO]" + color.RESET)
            DeterminaHermano(arbol1)
            print()
            VolverMenu()
            MenuInicio()
        elif opc == 6:
            #DETERMINA EL PADRE DE UN NODO CUALQUIER
            os.system("clear")
            print(color.AMARILLO + "[6-NODO PADRE]" + color.RESET)
            DeterminaPadre(arbol1)
            print()
            VolverMenu()
            MenuInicio()       
        elif opc == 7:
            #FIN DE LA APLICACION
            salir = True
        else:
            print()
            print(color.ROJO + "OPCION INCORRECTA!" + color.RESET)
            print()
            VolverMenu()
            print()
            MenuInicio()
    except ValueError:
        os.system("clear")
        print(color.ROJO + "LA OPCION INGRESADA NO ES VALIDA!!" + color.RESET) 
        print()
        VolverMenu()
        print()
        MenuInicio()
        
            
    
    
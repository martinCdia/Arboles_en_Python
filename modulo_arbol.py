class Arbol:
    def __init__(self, dato = None):
        if dato != None:
            self.dato = dato
        else:
            self.dato = None
        self.izquierdo = None
        self.derecho = None
    
    #AGREGAR DATOS AL ARBOL    
    def AgregarDatos(self, carga):
        if self.dato:
            if carga < self.dato:
                if self.izquierdo is None:
                    self.izquierdo = Arbol(carga)
                else:
                    self.izquierdo.AgregarDatos(carga)
            elif carga > self.dato:
                if self.derecho is None:
                    self.derecho = Arbol(carga)
                else:
                    self.derecho.AgregarDatos(carga)
        else:
            self.dato = carga
            print("NODO RAIZ => [" + str(carga) + "]")
    
    #IMPRIMIR PRE-ORDEN        
    def ImprimirPreOrden(self, arbol):
        if arbol == None:
            return
        else:
            print("[" + str(arbol.dato) + "]", end="")
            self.ImprimirPreOrden(arbol.izquierdo)
            self.ImprimirPreOrden(arbol.derecho)
    
    #IMPRIMIR POST-ORDEN
    def ImprimirPostOrden(self, arbol):
        if arbol == None:
            return
        else:
            self.ImprimirPreOrden(arbol.izquierdo)
            self.ImprimirPreOrden(arbol.derecho)
            print("[" + str(arbol.dato) + "]", end="")
    
    #IMPRIMIR IN-ORDEN                
    def ImprimirInOrden(self, arbol):
        if arbol == None:
            return
        else:
            self.ImprimirPreOrden(arbol.izquierdo)
            print("[" + str(arbol.dato) + "]", end="")
            self.ImprimirPreOrden(arbol.derecho)
    
    #DEVUELVE EL NODO RAIZ DEL ARBOL
    def NodoRaiz(self, arbol):
        if arbol is None:
            return
        else:
            return arbol.dato
    
    #DETERMINA SI DOS ARBOLES SON ISOMORFOS          
    def Isomorfos(self, arbol_a, arbol_b):
        self.iso = True
        if arbol_a is None and arbol_b is None:
            return
        else:
            if arbol_a.izquierdo is not None and arbol_b.izquierdo is None:    
                self.iso = False    
            if arbol_a.izquierdo is None and arbol_b.izquierdo is not None:    
                self.iso = False    
            if arbol_a.derecho is not None and arbol_b.derecho is None:    
                self.iso = False    
            if arbol_a.derecho is None and arbol_b.derecho is not None:
                self.iso = False 
            
            if self.iso is False: 
                return self.iso           
            else:
                self.Isomorfos(arbol_a.izquierdo, arbol_b.izquierdo)    
                self.Isomorfos(arbol_a.derecho, arbol_b.derecho)
                
            return self.iso    
    
    #DETERMINA CANTIDAD DE HOJAS DE UN ARBOL 
    def NodosHojas(self, arbol):
        cont = 0
        if arbol.izquierdo == None and arbol.derecho == None:
            cont = 1
        else:
            if arbol.izquierdo != None:
                cont += self.NodosHojas(arbol.izquierdo)
            if arbol.derecho != None:
                cont += self.NodosHojas(arbol.derecho)
        return cont        
    
    #DETERMINA EL HERMANO DE UN NODO CUALQUIERA
    def NodoHermano(self, arbol, nodo):
        if nodo < arbol.dato:
            if arbol.izquierdo is not None:
                if arbol.izquierdo.dato == nodo:
                    if arbol.derecho is not None:
                        print("NODO HERMANO DERECHO DE " + str(nodo) + " => " + "[" + str(arbol.derecho.dato) + "]")
                    else:
                        print("NO POSEE NODO HERMANO")
                else:
                    self.NodoHermano(arbol.izquierdo, nodo)
            else:
                print("NO SE ENCONTRO EL DATO INGRESADO")
        elif nodo > arbol.dato:
            if arbol.derecho is not None:
                if arbol.derecho.dato == nodo:
                    if arbol.izquierdo is not None:
                        print("NODO HERMANO IZQUIERDO DE " + str(nodo) + " => " + "[" + str(arbol.izquierdo.dato) + "]")
                    else:
                        print("NO POSEE NODO HERMANO")
                else:
                    self.NodoHermano(arbol.derecho, nodo)
            else:
                print("NO SE ENCONTRO EL DATO INGRESADO")
        elif nodo == arbol.dato:   
            print("EL DATO INGRESADO ES EL NODO RAIZ")
    
    #DETERMINA EL PADRE DE UN NODO CUALQUIERA        
    def NodoPadre(self, arbol, nodo):
        if arbol is None:
            return
        else:
            if nodo < arbol.dato:
                if arbol.izquierdo is not None:
                    if arbol.izquierdo.dato == nodo:
                        print("EL PADRE DEL NODO " + str(nodo) + " ES => " + "[" + str(arbol.dato) + "]")
                    else:
                        self.NodoPadre(arbol.izquierdo, nodo)
                else:
                    print("NO SE ENCONTRO EL DATO INGRESADO")
            elif nodo > arbol.dato:
                if arbol.derecho is not None:
                    if arbol.derecho.dato == nodo:
                        print("EL PADRE DEL NODO " + str(nodo) + " ES => " + "[" + str(arbol.dato) + "]")
                    else:
                        self.NodoPadre(arbol.derecho, nodo)
                else:
                    print("NO SE ENCONTRO EL DATO INGRESADO")
            elif nodo == arbol.dato:   
                print("EL DATO INGRESADO ES EL NODO RAIZ")   
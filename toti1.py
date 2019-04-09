import random
print("1. totito jugador vs jugador")
print("2. totito jugador vs computadora")
print("3. totito inverso jugador vs jugador")
seleccion = int(input("numero de modo de juego desea jugar? "))
if seleccion == 1:
    print ("")
    print ("")
    print ("_________________________________________________totito original__________________________________________________")
    print ("")
    nombre1= input("ingrese nombre del primer jugador: ")
    print ("")
    nombre2= input("ingrese nombre del segundo jugador: ")
    print ("")
    print ("")
    nombres= [nombre1,nombre2]
    tiraprimero = random.choice (nombres)
    partearri =[[" "],["w"],["|"],["e"],["|"],["r"]]
    partemed = [[" "],["s"],["|"],["d"],["|"],["f"]]
    parteaba = [[" "],["X"],["|"],["c"],["|"],["v"]]
    lista=[partearri,[["-------"]],partemed,[["-------"]],parteaba]
    posarri =["w","e","r"]
    posmed= ["s","d","f"]
    posaba = ["x","c","v"]
    posi=[posarri,posmed,posaba]
    posit = posaba+posmed+posarri



    def posiciones () :
        for i in posi:
            print ("                        ",i)
    def tablero() :
        
        for i in lista:
            parte =""
            for n in i:
                for r in n:
                    parte = parte + r
            print (parte)
    print (tiraprimero," es jugador 1")
    print ("")
    tablero()
    print("")
    win = 1
    while win == 1:
        print("es su turno jugador 1")
        
        selector = input("seleccione una casilla ")
        if selector not in posit:
            selector = ""
            print ("posicion invalida")
            selector = input("seleccione una casilla ")

        if selector == "w" :
            partearri[1].remove("w")
            partearri[1].insert(0,"x")
            posarri.remove("w")
            posarri.insert(0," ")
        if selector == "e" :
            partearri[3].remove("e")
            partearri[3].insert(0,"x")
            posarri.remove("e")
            posarri.insert(1," ")
        if selector == "r" :
            partearri[5].remove("r")
            partearri[5].insert(0,"x")
            posarri.remove("r")
            posarri.insert(2," ")
        #---------------------------------------parte1
        if selector == "s" :
            partemed[1].remove("s")
            partemed[1].insert(0,"x")
            posmed.remove("s")
            posmed.insert(0," ")
        if selector == "d" :
            partemed[3].remove("d")
            partemed[3].insert(0,"x")
            posmed.remove("d")
            posmed.insert(1," ")
        if selector == "f" :
            partemed[5].remove("f")
            partemed[5].insert(0,"x")
            posmed.remove("f")
            posmed.insert(2," ")
        #--------------------------------------parte 2
        if selector == "x" :
            parteaba[1].remove("X")
            parteaba[1].insert(0,"x")
            posaba.remove("x")
            posaba.insert(0," ")
        if selector == "c" :    
            parteaba[3].remove("c")
            parteaba[3].insert(0,"x")
            posaba.remove("c")
            posaba.insert(1," ")
        if selector == "v" :
            parteaba[5].remove("v")
            parteaba[5].insert(0,"x")
            posaba.remove("v")
            posaba.insert(2," ")
        tablero()
        
        print("")
        posit = posaba+posmed+posarri
        #--------------------------------------------------
        #----------------------------------------------jugador2
        #-------------------------------------------------------
        print("jugador 2 es su turno")
        
        selector2 = input("seleccione una casilla ")
        if selector2 not in posit:
            selector2 = ""
            print ("posicion invalida")
            selector2 = input("seleccione una casilla ")
        if selector2 == "w" :
            partearri[1].remove("w")
            partearri[1].insert(0,"o")
            posarri.remove("w")
            posarri.insert(0," ")
        if selector2 == "e" :
            partearri[3].remove("e")
            partearri[3].insert(0,"o")
            posarri.remove("e")
            posarri.insert(1," ")
        if selector2 == "r" :
            partearri[5].remove("r")
            partearri[5].insert(0,"o")
            posarri.remove("r")
            posarri.insert(2," ")
        #---------------------------------------parte1
        if selector2 == "s" :
            partemed[1].remove("s")
            partemed[1].insert(0,"o")
            posmed.remove("s")
            posmed.insert(0," ")
        if selector2 == "d" :
            partemed[3].remove("d")
            partemed[3].insert(0,"o")
            posmed.remove("d")
            posmed.insert(1," ")
        if selector2 == "f" :
            partemed[5].remove("f")
            partemed[5].insert(0,"o")
            posmed.remove("f")
            posmed.insert(2," ")
        #--------------------------------------parte 2
        if selector2 == "x" :
            parteaba[1].remove("X")
            parteaba[1].insert(0,"o")
            posaba.remove("x")
            posaba.insert(0," ")
        if selector2 == "c" :    
            parteaba[3].remove("c")
            parteaba[3].insert(0,"o")
            posaba.remove("c")
            posaba.insert(1," ")
        if selector2 == "v" :
            parteaba[5].remove("v")
            parteaba[5].insert(0,"o")
            posaba.remove("v")
            posaba.insert(2," ")
        if partearri [1] == partearri[3] and partearri[3] == partearri[5] and partearri[5] :
            win = 0
            if partearri[5] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
                
        if partemed [1] == partemed[3] and partemed[3] == partemed[5] :
            win = 0
            if partemed[5] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        if parteaba [1] == parteaba[3] and parteaba[3] == parteaba[5] :
            win = 0
            if parteaba[5] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        if partearri [1] == partemed[1] and partemed[1] == parteaba[1] :
            win = 0
            if partearri[1] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        if partearri [3] == partemed[3] and partemed[3] == parteaba[3] :
            win = 0
            if partearri[3] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        if partearri [5] == partemed[5] and partemed[5] == parteaba[5] :
            win = 0
            if partearri[5] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        if partearri [1] == partemed[3] and partemed[3] == parteaba[5] :
            win = 0
            if partearri[1] == ['x']:
                print("")
                print ("gano jugador 1")
                
            else:
                print("")
                print ("gano jugador 2")
        if partearri [5] == partemed[3] and partemed[3] == parteaba[1] :
            win = 0
            if partearri[5] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        tablero()

    #----------------------------------------------------
    #---------------------------------------------------
    #_-------------------------------------------------------
    #------------------------------------------------------
if seleccion == 2:
    print ("")
    print ("")
    print ("_________________________________________________totito vs compu__________________________________________________")
    print ("")
    nombre1= input("ingrese nombre del primer jugador: ")
    print ("")
    nombren = ["aqui lesbrinco","aqui lesvoy","benito carlos","armando casas"]
    nombre2 = random.choice(nombren)
    print ("")
    print ("")


    partearri =[[" "],["w"],["|"],["e"],["|"],["r"]]
    partemed = [[" "],["s"],["|"],["d"],["|"],["f"]]
    parteaba = [[" "],["X"],["|"],["c"],["|"],["v"]]
    lista=[partearri,[["-------"]],partemed,[["-------"]],parteaba]
    posarri =["w","e","r"]
    posmed= ["s","d","f"]
    posaba = ["x","c","v"]
    posi=[posarri,posmed,posaba]
    posit = posaba+posmed+posarri

    compu=random.choice(posit)

    def posiciones () :
        for i in posi:
            print ("                        ",i)
    def tablero() :
        
        for i in lista:
            parte =""
            for n in i:
                for r in n:
                    parte = parte + r
            print (parte)
    print (nombre1,"vs",nombre2)
    print ("")
    win = 1
    while win ==1:
        print("es su turno ",nombre1)
        
        selector = input("seleccione una casilla ")
        if selector not in posit:
            selector = ""
            print ("posicion invalida")
            selector = input("seleccione una casilla ")

        if selector == "w" :
            partearri[1].remove("w")
            partearri[1].insert(0,"x")
            posarri.remove("w")
            
        if selector == "e" :
            partearri[3].remove("e")
            partearri[3].insert(0,"x")
            posarri.remove("e")
            
        if selector == "r" :
            partearri[5].remove("r")
            partearri[5].insert(0,"x")
            posarri.remove("r")
            
        #---------------------------------------parte1
        if selector == "s" :
            partemed[1].remove("s")
            partemed[1].insert(0,"x")
            posmed.remove("s")
            
        if selector == "d" :
            partemed[3].remove("d")
            partemed[3].insert(0,"x")
            posmed.remove("d")
            
        if selector == "f" :
            partemed[5].remove("f")
            partemed[5].insert(0,"x")
            posmed.remove("f")
            
        #--------------------------------------parte 2
        if selector == "x" :
            parteaba[1].remove("X")
            parteaba[1].insert(0,"x")
            posaba.remove("x")
            
        if selector == "c" :    
            parteaba[3].remove("c")
            parteaba[3].insert(0,"x")
            posaba.remove("c")
            
        if selector == "v" :
            parteaba[5].remove("v")
            parteaba[5].insert(0,"x")
            posaba.remove("v")
        print("-----------------------------------------------------------")   
        tablero()
        print("")
        posit = posaba+posmed+posarri
        #--------------------------------------------------
        #----------------------------------------------jugador2
        #-------------------------------------------------------
        compu = random.choice(posit)
        while compu not in posit:
                compu= random.choice(posit)
        if compu == "w" :
            partearri[1].remove("w")
            partearri[1].insert(0,"o")
            posarri.remove("w")
            
        if compu == "e" :
            partearri[3].remove("e")
            partearri[3].insert(0,"o")
            posarri.remove("e")
            
        if compu == "r" :
            partearri[5].remove("r")
            partearri[5].insert(0,"o")
            posarri.remove("r")
            
        #---------------------------------------parte1
        if  compu == "s" :
            partemed[1].remove("s")
            partemed[1].insert(0,"o")
            posmed.remove("s")
            
        if compu == "d" :
            partemed[3].remove("d")
            partemed[3].insert(0,"o")
            posmed.remove("d")
            
        if compu == "f" :
            partemed[5].remove("f")
            partemed[5].insert(0,"o")
            posmed.remove("f")
            
        #--------------------------------------parte 2
        if compu == "x" :
            parteaba[1].remove("X")
            parteaba[1].insert(0,"o")
            posaba.remove("x")
            
        if compu == "c" :    
            parteaba[3].remove("c")
            parteaba[3].insert(0,"o")
            posaba.remove("c")
            
        if compu == "v" :
            parteaba[5].remove("v")
            parteaba[5].insert(0,"o")
            posaba.remove("v")
        if partearri [1] == partemed[1] and partemed[1] == parteaba[1] :
            win = 0
            if partearri[1] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        if partearri [3] == partemed[3] and partemed[3] == parteaba[3] :
            win = 0
            if partearri[3] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        if partearri [5] == partemed[5] and partemed[5] == parteaba[5] :
            win = 0
            if partearri[5] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        if partearri [1] == partemed[3] and partemed[3] == parteaba[5] :
            win = 0
            if partearri[1] == ['x']:
                print("")
                print ("gano jugador 1")
                
            else:
                print("")
                print ("gano jugador 2")
        if partearri [5] == partemed[3] and partemed[3] == parteaba[1] :
            win = 0
            if partearri[5] == ['x']:
                print("")
                print ("gano jugador 1")
            else:
                print("")
                print ("gano jugador 2")
        tablero()
        posit = posaba+posmed+posarri


if seleccion == 3:
    print ("")
    print ("")
    print ("_________________________________________________totito inverso__________________________________________________")
    print ("")
    nombre1= input("ingrese nombre del primer jugador: ")
    print ("")
    nombre2= input("ingrese nombre del segundo jugador: ")
    print ("")
    print ("")
    nombres= [nombre1,nombre2]
    tiraprimero = random.choice (nombres)
    partearri =[[" "],["w"],["|"],["e"],["|"],["r"]]
    partemed = [[" "],["s"],["|"],["d"],["|"],["f"]]
    parteaba = [[" "],["X"],["|"],["c"],["|"],["v"]]
    lista=[partearri,[["-------"]],partemed,[["-------"]],parteaba]
    posarri =["w","e","r"]
    posmed= ["s","d","f"]
    posaba = ["x","c","v"]
    posi=[posarri,posmed,posaba]
    posit = posaba+posmed+posarri



    def posiciones () :
        for i in posi:
            print ("                        ",i)
    def tablero() :
        
        for i in lista:
            parte =""
            for n in i:
                for r in n:
                    parte = parte + r
            print (parte)
    print (tiraprimero," es jugador 1")
    print ("")
    tablero()
    print("")
    win = 1
    while win == 1:
        print("es su turno jugador 1")
        
        selector = input("seleccione una casilla ")
        if selector not in posit:
            selector = ""
            print ("posicion invalida")
            selector = input("seleccione una casilla ")

        if selector == "w" :
            partearri[1].remove("w")
            partearri[1].insert(0,"x")
            posarri.remove("w")
            posarri.insert(0," ")
        if selector == "e" :
            partearri[3].remove("e")
            partearri[3].insert(0,"x")
            posarri.remove("e")
            posarri.insert(1," ")
        if selector == "r" :
            partearri[5].remove("r")
            partearri[5].insert(0,"x")
            posarri.remove("r")
            posarri.insert(2," ")
        #---------------------------------------parte1
        if selector == "s" :
            partemed[1].remove("s")
            partemed[1].insert(0,"x")
            posmed.remove("s")
            posmed.insert(0," ")
        if selector == "d" :
            partemed[3].remove("d")
            partemed[3].insert(0,"x")
            posmed.remove("d")
            posmed.insert(1," ")
        if selector == "f" :
            partemed[5].remove("f")
            partemed[5].insert(0,"x")
            posmed.remove("f")
            posmed.insert(2," ")
        #--------------------------------------parte 2
        if selector == "x" :
            parteaba[1].remove("X")
            parteaba[1].insert(0,"x")
            posaba.remove("x")
            posaba.insert(0," ")
        if selector == "c" :    
            parteaba[3].remove("c")
            parteaba[3].insert(0,"x")
            posaba.remove("c")
            posaba.insert(1," ")
        if selector == "v" :
            parteaba[5].remove("v")
            parteaba[5].insert(0,"x")
            posaba.remove("v")
            posaba.insert(2," ")
        tablero()
        
        print("")
        posit = posaba+posmed+posarri
        #--------------------------------------------------
        #----------------------------------------------jugador2
        #-------------------------------------------------------
        print("jugador 2 es su turno")
        
        selector2 = input("seleccione una casilla ")
        if selector2 not in posit:
            selector2 = ""
            print ("posicion invalida")
            selector2 = input("seleccione una casilla ")
        if selector2 == "w" :
            partearri[1].remove("w")
            partearri[1].insert(0,"o")
            posarri.remove("w")
            posarri.insert(0," ")
        if selector2 == "e" :
            partearri[3].remove("e")
            partearri[3].insert(0,"o")
            posarri.remove("e")
            posarri.insert(1," ")
        if selector2 == "r" :
            partearri[5].remove("r")
            partearri[5].insert(0,"o")
            posarri.remove("r")
            posarri.insert(2," ")
        #---------------------------------------parte1
        if selector2 == "s" :
            partemed[1].remove("s")
            partemed[1].insert(0,"o")
            posmed.remove("s")
            posmed.insert(0," ")
        if selector2 == "d" :
            partemed[3].remove("d")
            partemed[3].insert(0,"o")
            posmed.remove("d")
            posmed.insert(1," ")
        if selector2 == "f" :
            partemed[5].remove("f")
            partemed[5].insert(0,"o")
            posmed.remove("f")
            posmed.insert(2," ")
        #--------------------------------------parte 2
        if selector2 == "x" :
            parteaba[1].remove("X")
            parteaba[1].insert(0,"o")
            posaba.remove("x")
            posaba.insert(0," ")
        if selector2 == "c" :    
            parteaba[3].remove("c")
            parteaba[3].insert(0,"o")
            posaba.remove("c")
            posaba.insert(1," ")
        if selector2 == "v" :
            parteaba[5].remove("v")
            parteaba[5].insert(0,"o")
            posaba.remove("v")
            posaba.insert(2," ")
        if partearri [1] == partearri[3] and partearri[3] == partearri[5] and partearri[5] :
            win = 0
            if partearri[5] == ['x']:
                print("")
                print ("gano jugador 2")
            else:
                print("")
                print ("gano jugador 1")
                
        if partemed [1] == partemed[3] and partemed[3] == partemed[5] :
            win = 0
            if partemed[5] == ['x']:
                print("")
                print ("gano jugador 2")
            else:
                print("")
                print ("gano jugador 1")
        if parteaba [1] == parteaba[3] and parteaba[3] == parteaba[5] :
            win = 0
            if parteaba[5] == ['x']:
                print("")
                print ("gano jugador 2")
            else:
                print("")
                print ("gano jugador 1")
        if partearri [1] == partemed[1] and partemed[1] == parteaba[1] :
            win = 0
            if partearri[1] == ['x']:
                print("")
                print ("gano jugador 2")
            else:
                print("")
                print ("gano jugador 1")
        if partearri [3] == partemed[3] and partemed[3] == parteaba[3] :
            win = 0
            if partearri[3] == ['x']:
                print("")
                print ("gano jugador 2")
            else:
                print("")
                print ("gano jugador 1")
        if partearri [5] == partemed[5] and partemed[5] == parteaba[5] :
            win = 0
            if partearri[5] == ['x']:
                print("")
                print ("gano jugador 2")
            else:
                print("")
                print ("gano jugador 1")
        if partearri [1] == partemed[3] and partemed[3] == parteaba[5] :
            win = 0
            if partearri[1] == ['x']:
                print("")
                print ("gano jugador 2")
                
            else:
                print("")
                print ("gano jugador 1")
        if partearri [5] == partemed[3] and partemed[3] == parteaba[1] :
            win = 0
            if partearri[5] == ['x']:
                print("")
                print ("gano jugador 2")
            else:
                print("")
                print ("gano jugador 1")
        tablero()









        





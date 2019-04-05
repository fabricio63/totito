import random
print ("")
print ("")
print ("_________________________________________________totito__________________________________________________")
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
parteaba = [[" "],["x"],["|"],["c"],["|"],["v"]]
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
        parteaba[1].remove("x")
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
    if partearri [1] == partearri[3] and partearri[3] == partearri[5] :
        win = 0
        print ("termino1")
    if partemed [1] == partemed[3] and partemed[3] == partemed[5] :
        win = 0
        print ("termino2")
    if parteaba [1] == parteaba[3] and parteaba[3] == parteaba[5] :
        win = 0
        print ("termino3")
    if partearri [1] == partemed[1] and partemed[1] == parteaba[1] :
        win = 0
        print ("termino4")
    if partearri [3] == partemed[3] and partemed[3] == parteaba[3] :
        win = 0
        print ("termino5")
    if partearri [5] == partemed[5] and partemed[5] == parteaba[5] :
        win = 0
        print ("termino6")
    if partearri [1] == partemed[3] and partemed[3] == parteaba[5] :
        win = 0
        print ("termino7")
    if partearri [5] == partemed[3] and partemed[3] == parteaba[1] :
        win = 0
        print ("termino8")
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
        parteaba[1].remove("x")
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
    if partearri [1] == partearri[3] and partearri[3] == partearri[5] :
        win = 0
        print ("termino1")
    if partemed [1] == partemed[3] and partemed[3] == partemed[5] :
        win = 0
        print ("termino2")
    if parteaba [1] == parteaba[3] and parteaba[3] == parteaba[5] :
        win = 0
        print ("termino3")
    if partearri [1] == partemed[1] and partemed[1] == parteaba[1] :
        win = 0
        print ("termino4")
    if partearri [3] == partemed[3] and partemed[3] == parteaba[3] :
        win = 0
        print ("termino5")
    if partearri [5] == partemed[5] and partemed[5] == parteaba[5] :
        win = 0
        print ("termino6")
    if partearri [1] == partemed[3] and partemed[3] == parteaba[5] :
        win = 0
        print ("termino7")
    if partearri [5] == partemed[3] and partemed[3] == parteaba[1] :
        win = 0
        print ("termino8")
    tablero()










        





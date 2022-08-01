from itertools import product

def condicionLenguaje(cadena):
    ases=cadena.count('a')
    bses=cadena.count('b')
    condicion = ases==bses
    return condicion

A=[]
D=[]
F=[]
def alfabeto():
    nt=input("ingrene la cantidad N de elementos del Alfabeto ")
    for i in range(int(nt)):
        lee=input(f"elemento {i+1} de {nt}: " )
        A.append(lee)
    print(A)

def transiciones():
    nd=input("ingrene la cantidad N de transiciones ")
    for i in range(int(nd)):
        lee=input(f"elemento {i+1} de {nd}: " )
        split=lee.split("=")
        izq=split[0].split(",")
        pseudoDer=split[1].split(",")
        der=[]
        for j in range(len(pseudoDer)):
            der.append(pseudoDer[j].split("-"))
        trans=[izq,der]
        D.append(trans)
    print(D)
    return D

def digitosAProbar():
    dig=input("ingrese la cantidad de digitos a probar ")
    combinaciones=[]
    for i in range(int(dig)+1):
        temp = product(A, repeat=i)
        for j in list(temp):
            cadena="".join(j)
            combinaciones.append(cadena)
    return combinaciones

def estadosFinales():
    nt=input("ingrene la cantidad N de Estados finales ")
    for i in range(int(nt)):
        lee=input(f"elemento {i+1} de {nt}: " )
        F.append(lee)
    print(F)

alfabeto()
transiciones()
estadosFinales()
combinaciones=digitosAProbar()

def validarCadena(cadena, estado, pila, finales, cont):
    if cont>3:
        return bool(False)
    if cadena==''and estado in finales and pila=='Z':
        return bool(True)
    if cadena!=''and pila=='':
        return bool(False)
    
    aceptacion=bool(False)
    if cadena=='':
        letra=''
    else:
        letra=cadena[0]
    topePila=pila[0]
    for i in range(len(D)):                                                     
        izq=D[i][0]
        if izq[0]==estado and (izq[1]==letra or izq[1]=='') and izq[2]==topePila:
            pilaDerecha=pila[1:]
            for j in range(len(D[i][1])):
                pila=D[i][1][j][1]+pilaDerecha
                if izq[1]=='':
                    cont=cont+1
                    recursion=validarCadena(cadena,D[i][1][j][0],pila,finales,cont)
                else:
                    recursion=validarCadena(cadena[1:],D[i][1][j][0],pila,finales,cont)
                aceptacion=aceptacion or recursion
                
    return aceptacion

for i in range(len(combinaciones)):
    condicion=condicionLenguaje(combinaciones[i])
    valido=validarCadena(combinaciones[i],'q0','Z',F,0)
    resultado=not(condicion^valido)    
    if not resultado: 
        print(
        combinaciones[i],
        'Valido por el Lenguaje:',condicion,
        ' Valido por el Automata:',valido,
        '--> Discrepancia'
        )

print("Si no hay discrepancias todo bien")
    
    
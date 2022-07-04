from itertools import product
A=[]
D=[]
nt=input("ingrene la cantidad N de elementos del Alfabeto ")
for i in range(int(nt)):
    lee=input(f"elemento {i+1} de {nt}: " )
    A.append(lee)
print(A)
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

combinaciones=[]
for i in range(13):
    temp = product(A, repeat=i)
    for j in list(temp):
        cadena="".join(j)
        combinaciones.append(cadena)

def validarCadena(cadena, estado, pila):
    if cadena==''and pila=='':
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
                    recursion=validarCadena(cadena,D[i][1][j][0],pila)
                else:
                    recursion=validarCadena(cadena[1:],D[i][1][j][0],pila)
                aceptacion=aceptacion or recursion
                
    return aceptacion

for i in range(len(combinaciones)):
    ases=combinaciones[i].count('a')
    bses=combinaciones[i].count('b')
    condicion=ases<bses<2*ases
    valido=validarCadena(combinaciones[i],'q0','Z')
    resultado=not(condicion^valido)    
    print(
    combinaciones[i],
    valido,
    'Nro de As:',ases,
    ' Nro de Bs:',bses,
    condicion,
    valido,
    'resultado final= ',
    resultado,
    )
    
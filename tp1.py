import math
from fractions import Fraction

## Los datos estaticos (siempre los da el enunciado) son por ahora el intervalo (ej: 20-30)
## y el fai (numero correspondiente a al intervalo) (ej:1)
#-----------------------------------------------------
#Notas lógica:
#estructura de la lista = [[20,30,1],[30,40,10]]
#---------------------------------------------------
#Notas estadistica:
# n=cant datos //
# fi= fai/n   //
# Fai= sum de 1 hasta i (fai) //
# Fi = sum de 1 hasta i (fi)  //
# Gai=  sum de i hasta k (fai)
# Gi= sum de i hasa k (fi)
# Ci= (Li + Ld)/2 //
# Ai = Ld - Li
# Media = sum 1 hasta k (Ci.fi) (ci.fi puede ponerse en una columna aparte) //
# Mediana (x~) = Li + Ai [(n/2)-Fa(i-1)/fai]
# Varianza = sum i hasta k [(Ci-x~)^2.fi] //
# CuasiVarianza = 1/n-1 . Sum 1 hasta k ([Ci-x~]^2.fai) //


def tabla_guia1(lista):
    lista_copia = lista.copy()
    #calculo k
    k = len(lista_copia)

    # queda posicion indice=3
    calc_Fia(lista_copia)

    #asigno n ahora que ya esta calculado
    n = lista_copia[len(lista_copia)-1][3]

    # queda posicion indice=4
    calc_Ci(lista_copia)

    #queda en la posicion indice = 5
    calc_fi(lista_copia, n)

    #queda en la posicion indice = 6
    calc_Fi(lista_copia, n)

    #Queda en la posicion indice= 7 el Ci*fi
    media= round(float(calc_media(lista_copia)),4)


    # Queda en la posicion indice= 8 el (Ci-xˉ)^2 * fi
    varianza = round(float(calc_varianza(lista_copia, media)),4)


    #calculo cuasiVarianza
    cuasiVarianza= round(float(calc_cuasiVar(lista_copia, media,n)),4)


    # calculo cuasiVarianza
    medial= round(calc_mediana(lista_copia,n),4)


    return lista_copia, media, medial, varianza, cuasiVarianza

#funciones internas/privadas
#estructura de la lista = [[20,30,1],[30,40,10]]

def calc_Fia(lista):
    Fia_total=0
    for i in lista:
      Fia_total+= i[2]
      i.append(Fia_total)

def calc_Ci(lista):
    #preguntar al profe si Ci puede ser con coma !!!!!
    for i in lista:
        Ci = int((i[0]+ i[1])/2)
        i.append(Ci)

def calc_fi(lista, n):
    for i in lista:
        fi = Fraction(i[2] / n).limit_denominator()
        i.append(fi)

def calc_Fi (lista, n):
    for i in lista:
        fi = Fraction(i[3] / n).limit_denominator()
        i.append(fi)

def calc_media(lista):
    media= 0
    for i in lista:
        cifi = i[4] * i[5]
        media+= cifi
        i.append(cifi)
    return media

def calc_varianza(lista, media):
    varianza = 0
    for i in lista:
        calculo= round(((i[4]-media)**2)* i[5],4)
        varianza+= calculo
        i.append(calculo)
    return varianza

def calc_cuasiVar (lista, media, n):
    cuasiVar = 0
    for i in lista:
        calculo= round(((i[4]-media)**2)* i[2],4)
        cuasiVar+= calculo
    return cuasiVar/(n-1)

def calc_Ai(lista):
    for i in lista:
        Ai= i[1]-i[0]
        i.append(Ai)

def calc_mediana(lista,n):
    nro_medio= n/2
    lista_medial= []
    cont=0
    for i in lista:
        if (nro_medio > i[0] and nro_medio <= i[1]):
            lista_medial = i.copy()
            break
        cont+=1
    medial= lista_medial[0] + (lista_medial[1]-lista_medial[0])*(nro_medio-lista[cont-1][3])/lista_medial[2]
    return medial


def imprimir_tabla(encabezados, datos):
    # calcular el ancho máximo de cada columna
    anchos = []
    for i, enc in enumerate(encabezados):
        max_ancho = len(enc)
        for fila in datos:
            max_ancho = max(max_ancho, len(str(fila[i])))
        anchos.append(max_ancho + 2)

    # línea separadora
    def separador():
        linea = "+"
        for ancho in anchos:
            linea += "-" * ancho + "+"
        return linea

    # fila formateada
    def fila_str(valores):
        fila = "|"
        for i, val in enumerate(valores):
            fila += f" {str(val):<{anchos[i]-1}}|"
        return fila

    print(separador())
    print(fila_str(encabezados))
    print(separador())
    for fila in datos:
        print(fila_str(fila))
    print(separador())

def porcentajes_intervalos(lista,lista_intervalos):
    x_mayor, x_menor = lista_intervalos[0], lista_intervalos[1]
    contador=0

    #solamente tengo x>
    if x_menor == -1:
        for i in lista:
            if i[0]>=x_mayor:
                contador+=i[2]

    #solaente tengo x<
    if x_mayor == -1:
        for i in lista:
            if i[1]<=x_menor:
                contador+=i[2]

    #ambos
    else:
        for i in lista:
            if x_mayor <= i[0] and  i[1]<= x_menor:
                contador+=i[2]
    return contador/lista[len(lista)-1][3]

def calc_fractiles(lista,k,m):
    formula= (k*lista[len(lista)-1][3])/m
    lista_fractil= []
    cont=0
    for i in lista:
        if formula<=i[3]:
            lista_fractil = i.copy()
            break
        cont+=1
    fractil= lista_fractil[0] + (lista_fractil[1]-lista_fractil[0])*(formula-lista[cont-1][3])/lista_fractil[2]
    return fractil
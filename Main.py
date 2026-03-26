import ast
import math

from tp1 import tabla_guia1
from tp1 import imprimir_tabla
from tp1 import porcentajes_intervalos
from tp1 import calc_fractiles



def main():
    #[[20,30,1],[30,40,15],[40,50,39],[50,60,32],[60,70,11],[70,80,2]]
    tabla_valores= ["Li(0)", "Ld(1)", "fia(2)", "Fia(3)", "Ci(4)", "fi(5)", "Fi(6)", "Ci*fi (7)", "(Ci-xˉ)^2 * fi (8)"]

    while True:
        print( "\033[95m\033[1m "+ "="*130+" \033[0m")
        print("\033[96m\033[1m  ██████╗ ██████╗  ██████╗ ██████╗  \033[0m", end="")
        print(
            "\033[93m\033[1m ██╗   ██╗    ███████╗███████╗████████╗ █████╗ ██████╗ ██╗███████╗████████╗██╗ ██████╗ █████╗ \033[0m")
        print("\033[96m\033[1m  ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗ \033[0m", end="")
        print(
            "\033[93m\033[1m ╚██╗ ██╔╝    ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██║██╔════╝██╔══██╗\033[0m")
        print("\033[96m\033[1m  ██████╔╝██████╔╝██║   ██║██████╔╝ \033[0m", end="")
        print(
            "\033[93m\033[1m  ╚████╔╝     █████╗  ███████╗   ██║   ███████║██║  ██║██║███████╗   ██║   ██║██║     ███████║\033[0m")
        print("\033[96m\033[1m  ██╔═══╝ ██╔══██╗██║   ██║██╔══██╗ \033[0m", end="")
        print(
            "\033[93m\033[1m   ╚██╔╝      ██╔══╝  ╚════██║   ██║   ██╔══██║██║  ██║██║╚════██║   ██║   ██║██║     ██╔══██║\033[0m")
        print("\033[96m\033[1m  ██║     ██║  ██║╚██████╔╝██████╔╝ \033[0m", end="")
        print(
            "\033[93m\033[1m    ██║       ███████╗███████║   ██║   ██║  ██║██████╔╝██║███████║   ██║   ██║╚██████╗██║  ██║\033[0m")
        print("\033[96m\033[1m  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  \033[0m", end="")
        print(
            "\033[93m\033[1m    ╚═╝       ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝\033[0m")
        print( "\033[95m\033[1m "+ "="*130+" \033[0m") #violeta
        print("\033[97m Cosas a tener en cuenta: \033[0m") #blanco
        print("\033[97m         # Las fracciones son reducidas automaticamente y la biblioteca no me deja cambiarlo :,( \033[0m")
        print("\033[97m         # - \033[0m")
        print("\033[97m         # - \033[0m")
        print("")
        print("\033[95m\033[1m " +" ¿Que tipo de ejercicio queres hacer?"+ " \033[0m")
        print("\033[97m         - (1) Tp 1 (varianza, cuasivarianza, media, medial, etc) \033[0m")
        print("\033[97m         - (-1) Salir \033[0m")

        eleccion = input("\033[97m Escribir opcion: ")

        if eleccion == "1":
            lista=[]
            while True:
                fila= input( "\033[95m\033[1m Ingresa cada fila de valores con el formato [Li,Ld,fai] (-1 si ya cargaste todas): \033[0m")
                if fila.strip() == "-1":
                    break

                lista.append(ast.literal_eval(fila))
            lista_completa, media, mediana, varianza, cuasiVarianza = tabla_guia1(lista)

            print("")
            print( "\033[95m\033[1m Lista:  \033[0m")
            imprimir_tabla(tabla_valores,lista_completa)
            print("\033[95m\033[1m Datos:  \033[0m")
            print(f"\033[97m Media: {media} \033[0m")
            print(f"\033[97m Mediana: {mediana} \033[0m")
            print(f"\033[97m Varianza:{varianza} \033[0m")
            print(f"\033[97m Cuasivarianza: {cuasiVarianza} \033[0m")
            print(f"\033[97m Desvio: {round(math.sqrt(varianza),4)} \033[0m")
            print(f"\033[97m Cuasidesvio: {round(math.sqrt(cuasiVarianza),4)} \033[0m")
            print(f"\033[97m Coeficiente de variación (<%20 sirve / <%5 es totalmente representativo): %{round((math.sqrt(varianza)/media)*100,4)} \033[0m")
            print(f"\033[97m Cuasi-Coeficiente de variación (<%20 sirve / <%5 es totalmente representativo): %{round((math.sqrt(cuasiVarianza) / media) * 100, 4)} \033[0m")

            while True:
                print("")
                extra = input("\033[95m\033[1m ¿Queres calcular algo más?  (""si"" de ser afirmativo)\033[0m")
                if extra.lower() == "si":
                    print("")
                    print("\033[95m\033[1m " + "¿Que queres calcular?" + " \033[0m")
                    print("\033[97m         - (1) porcentajes de intervalos \033[0m")
                    print("\033[97m         - (2) calculo fractiles \033[0m")
                    print("\033[97m         - (-1) Salir \033[0m")
                    eleccion_extra = input("\033[97m Escribir opcion: ")
                    if eleccion_extra == "-1":
                        break
                    if eleccion_extra == "1":
                        intervalo = input("\033[95m\033[1m Ingresa en formato lista ambos valores del intervalo, EL PARAMETRO X> primero (-1 si no tiene restrcción en alguno)(ej: x>10 = [10,-1]): \033[0m")
                        lista_intervalos= ast.literal_eval(intervalo)

                        print("")
                        print(f"\033[97m\033[1m Porcentaje del intervalo = %{round(porcentajes_intervalos(lista_completa,lista_intervalos)*100,4)} \033[0m")
                    elif eleccion_extra == "2":
                        fractil = input("\033[95m\033[1m Ingresa en formato lista ambos valores del calculo del fractil (k=nro fractil, m=partes del fractil [cuartiles m=4 / deciles m=10 / percentiles m=100]) ([k,m]): \033[0m")
                        k= ast.literal_eval(fractil)[0]
                        m= ast.literal_eval(fractil)[1]
                        print("")
                        print(f"\033[97m\033[1m (D,C,P){k} = %{round(calc_fractiles(lista_completa,k,m), 4)} \033[0m")
                else:
                    break

            break
        else:
            print("Saliendo....")
            break
main()
import shutil
import os
import tkinter as tk
from tkinter import filedialog

# Definir y crear (si no existen) las carpetas del indice y las partidas guardadas.
nombre_partida = "DS30000.sl2"

carpeta_documentos = os.path.join(os.getenv('USERPROFILE'), 'Documents')

carpeta_index = os.path.join(carpeta_documentos, 'SoulsGameSaver', "IndexDs3")
index = os.path.join(carpeta_index, 'index.txt')

carpeta_partidas = os.path.join(carpeta_documentos, 'SoulsGameSaver', "PartidasDs3")
if not os.path.exists(index):
    os.makedirs(carpeta_index)
    with open(index, 'w') as f:
        pass
    os.makedirs(carpeta_partidas)


def seleccionar_carpeta():
    root = tk.Tk()
    root.withdraw()

    appdata_path = os.getenv('APPDATA')
    directorio_inicial = os.path.join(appdata_path, "DarkSoulsIII")

    carpeta_seleccionada = filedialog.askdirectory(initialdir=directorio_inicial)

    if carpeta_seleccionada:
        return carpeta_seleccionada
    else:
        print("No se seleccionó ninguna carpeta.")
        exit()


input("Pulsa Enter y selecciona la carpeta de los archivos de guardado.")
partida_juego = seleccionar_carpeta()




def guardarPartida(nompartida):
    try:
        os.mkdir(os.path.join(carpeta_partidas, nompartida))

        shutil.copy(partida_juego + "\\" + nombre_partida,
                    carpeta_partidas + "\\" + nompartida + "\\" + nombre_partida)

        with open(index, "a") as f:
            f.write(nompartida + "\n")
    except:
        print("ERR: La carpeta ya existe o el archivo no se puede crear")


def cargarPartida(numpartida):
    with open(index, "r") as f:
        try:
            car = f.readlines()[numpartida - 1].strip()
        except IndexError as e:
            print("El numero de partida no existe.")
            return

    partida_n = os.path.join(carpeta_partidas, car, nombre_partida)
    destino = os.path.join(partida_juego, nombre_partida)

    shutil.copy(partida_n, destino)


def mostrarCarpetas():
    f = open(index, "r")
    i = 1
    for p in f.readlines():
        print(str(i) + "- " + p, end="")
        i += 1


def borrarCarpeta(num):
    num -= 1
    res = ""
    with open(index, "r") as f:
        fichero = f.readlines()
        if num >= len(fichero) or num <= -1:
            raise IndexError("El numero de partida no existe.")
        for i, line in enumerate(fichero):
            if i != num:
                res += line.strip() + "\n"
            else:
                carpeta_a_borrar = os.path.join(carpeta_partidas, line.strip())
                shutil.rmtree(carpeta_a_borrar)
    with open(index, "w") as f:
        f.write(res)


while 1:
    print("\n\n1. Mostrar Partidas\n2. Cargar Partida\n3. Guardar Partida\n4. Borrar Partida\n0. Finalizar")

    try:
        op = int(input())
    except ValueError as e:
        print("Caracter no valido.")
        continue

    if op == 1:
        print()
        mostrarCarpetas()

    elif op == 2:
        print("\nQue partidas quieres cargar.")
        mostrarCarpetas()
        print("Introduce el numero de la partida: ", end="")
        try:
            num = int(input())
        except ValueError as e:
            print("Introduce un numero.")
            continue

        cargarPartida(num)

    elif op == 3:
        print("Introduce el nombre de la partida: ", end="")

        nom = input()
        if not nom.isalnum():
            print("Introduce un nombre valido.")
            continue


        guardarPartida(nom)

    elif op == 4:
        print("\nQue partidas quieres borrar.")
        mostrarCarpetas()
        print("Introduce el numero de la partida: ", end="")
        try:
            num = int(input())
        except ValueError as e:
            print("Introduce un numero.")
            continue

        try:
            borrarCarpeta(num)
        except IndexError as e:
            print("Error:", e)

    elif op == 0:
        print("Finalizando programa.")
        exit()

    else:
        print("Numero incorrecto")

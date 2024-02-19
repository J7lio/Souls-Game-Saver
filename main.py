import shutil
import os

index = "D:/Juegos/_partidasguardadas/IndexDs3/index.txt"
carpeta_partidas = "D:/Juegos/_partidasguardadas/Ds3"
partida_juego = "C:/Users/julio/AppData/Roaming/DarkSoulsIII/0110000134ba164c"
nombre_partida = "DS30000.sl2"


#Copia la partida actual con el nombre dado
def guardarPartida(nompartida):
    try:
        os.mkdir(carpeta_partidas + "\\" + str(nompartida))
        shutil.copy(partida_juego + "\\" + nombre_partida, carpeta_partidas + "\\" + str(nompartida) + "\\" + nombre_partida)

        f = open(index, "a")
        f.write(nompartida + "\n")
        f.close()
    except:
        print("ERR: La carpeta ya existe o el archivo no se puede crear")

def cargarPartida(numpartida):
    f = open(index, "r")
    car = f.readlines()[numpartida - 1][:-1]
    f.close()

    shutil.copy(carpeta_partidas + "\\" + car + "\\" + nombre_partida, partida_juego + "\\" + nombre_partida)


def mostrarCarpetas():
    f = open(index, "r")
    i = 1
    for p in f.readlines():
        print(str(i) + "- " + p, end="")
        i+=1


while 1:
    print("\n\n0. Mostrar Partidas\n1. Cargar Partida\n2. Guardar Partida\n3. Finalizar")
    op = input()

    if op == "0":
        mostrarCarpetas()
    elif op == "1":
        print("Introduce el numero de la partida: ", end="")
        num = input()
        cargarPartida(int(num))
    elif op == "2":
        print("Introduce el nombre de la partida: ", end="")
        nom = input()
        guardarPartida(nom)
    elif op == "3":
        print("Finalizando programa.")
        exit()
    else:
        print("Valor no valido")

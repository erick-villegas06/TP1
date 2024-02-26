import random as x
def jugarppt():
    print("******Bienvenido al juego de piedra, papel o tijera******")
    cantidadpartidas = int(input("Ingrese la cantidad de partidas a jugar: "))
    if(cantidadpartidas<=0 ):
        print("Error, ingresa un numero mayor a 0")
    else:   
        puntosordenador = 0
        puntosjugador = 0
        for i in  range(cantidadpartidas):
            opcionjugador=str(input("Ingresa una opcion: P(piedra, A(papel) o T(tijera)): ").upper())   
            if(opcionjugador == 'P' or opcionjugador == 'A' or opcionjugador == 'T'):
                opcionpc = x.choice(['P','A','T'])
                print(f'El ordenador eligio la opcion {opcionpc} y el jugador {opcionjugador}')
                if(opcionpc == opcionjugador):
                    print("Empate")
                elif(opcionjugador == 'P' and opcionpc == 'A'):
                    print("El ordenador gana")
                    puntosordenador += 1     
                elif(opcionjugador == 'P' and opcionpc == 'T'):
                    print("El jugador gana")
                    puntosjugador += 1
                elif(opcionjugador == 'A' and opcionpc == 'P' ):
                    print("El jugador gana")
                    puntosjugador += 1 
                elif(opcionjugador == 'A' and opcionpc == 'T'):
                    print("El ordenador gana")
                    puntosordenador += 1 
                elif(opcionjugador == 'T' and opcionpc == 'P'):
                    print("El ordenador gana")
                    puntosordenador += 1
                else:
                    print("El jugador gana")
                    puntosjugador += 1
            else:
                print("Error, debes ingresar P(piedra), A(papel) o T(tijera)")

        print(f'******************RESULTADO FINAL******************\nPuntos Usuario: {puntosjugador}\nPuntos Ordenador: {puntosordenador}' )
        if(puntosjugador > puntosordenador):
            print("Felicidades ganaste el Piedra, Papel o Tijera")
        elif(puntosjugador< puntosordenador):
            print("Ups, esta vez no fuiste el vencedor sigue intentando")
        else:
            print("Es un empate")

#jugarppt()
            
import random

def generar_tablero(filas, columnas, minas):
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    minas_generadas = 0
    while minas_generadas < minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if tablero[fila][columna] != '*':
            tablero[fila][columna] = '*'
            minas_generadas += 1
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

def contar_minas_alrededor(tablero, fila, columna):
    contador = 0
    for i in range(max(0, fila - 1), min(len(tablero), fila + 2)):
        for j in range(max(0, columna - 1), min(len(tablero[0]), columna + 2)):
            if tablero[i][j] == '*':
                contador += 1
    return contador

def actualizar_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] != '*':
                tablero[i][j] = str(contar_minas_alrededor(tablero, i, j))

def jugar(filas, columnas, minas):
    tablero = generar_tablero(filas, columnas, minas)
    imprimir_tablero(tablero)
    actualizar_tablero(tablero)
    print("\n¡Comienza el juego!\n")
    while True:
        imprimir_tablero(tablero)
        print()
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))
        if tablero[fila][columna] == '*':
            print("\n¡Has perdido!")
            break
        elif tablero[fila][columna] == '0':
            print("\n¡Casilla vacía!")
        else:
            print("\n¡Hay", tablero[fila][columna], "minas alrededor!")
    print("\nJuego terminado.")

# Ejemplo de juego con un tablero de 5x5 y 5 minas
jugar(5, 5, 5)

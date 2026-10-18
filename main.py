import chess
import random

def selector_pseudo_aleatorio_movimientos_legales(tablero):

    movimientos = list(tablero.legal_moves)
    movimiento = random.choice(movimientos)

    return movimiento

def main():

    tablero = chess.Board()

    print("WELCOME TO AICHESS")

    num_jugadas = 0
    lim_jugadas = 500

    while not tablero.is_game_over(claim_draw=True):

        if num_jugadas == lim_jugadas:

            print("El límite de jugadas ha sido alcanzado")

            break

        if tablero.turn == chess.WHITE:

            jugador = "BLANCAS"
            print("\nTurno de las piezas blancas")

        else:

            jugador = "NEGRAS"
            print("\nTurno de las piezas negras")

        movimiento = selector_pseudo_aleatorio_movimientos_legales(tablero)
        movimiento_algebraico = tablero.san(movimiento)
        tablero.push(movimiento)
        num_jugadas += 1

        print(f"{num_jugadas}. {jugador}: {movimiento_algebraico} ")

        print("\n Posicion Tablero")
        print(tablero)

        if tablero.is_game_over(claim_draw=True):

            print("Resultado:", tablero.result(claim_draw=True))
            print("Motivo:", tablero.outcome(claim_draw=True).termination)


if __name__ == '__main__':

    main()



 
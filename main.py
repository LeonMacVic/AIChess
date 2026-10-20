import chess
import random

from evaluacion_tablero import evaluar_tablero

def seleccion_movimiento(tablero): #mejor movimiento inmediato (one-ply search)

    movimientos = list(tablero.legal_moves)

    if not movimientos:

        return None

    random.shuffle(movimientos)

    juega_blancas = tablero.turn == chess.WHITE

    if juega_blancas:

        mejor_evaluacion = float("-inf")

    else:

        mejor_evaluacion = float("inf")

    mejor_movimiento = None

    for movimiento in movimientos:

        tablero.push(movimiento)

        evaluacion = evaluar_tablero(tablero)

        tablero.pop()

        if juega_blancas:

            if evaluacion > mejor_evaluacion:

                mejor_evaluacion = evaluacion
                mejor_movimiento = movimiento

        else:

            if evaluacion < mejor_evaluacion:

                mejor_evaluacion = evaluacion
                mejor_movimiento = movimiento


    return mejor_movimiento


#def selector_pseudo_aleatorio_movimientos_legales(tablero):

    #movimientos = list(tablero.legal_moves)
    #movimiento = random.choice(movimientos)

    #return movimiento

def main():

    tablero = chess.Board()

    print("WELCOME TO AICHESS v0.2.0 (Motor con evaluacion material)")

    num_jugadas = 0
    lim_jugadas = 500

    while not tablero.is_game_over(claim_draw=True):

        if num_jugadas >= lim_jugadas:

            print("El límite de jugadas ha sido alcanzado")

            break

        if tablero.turn == chess.WHITE:

            jugador = "BLANCAS"
            print("\nTurno de las piezas blancas")

        else:

            jugador = "NEGRAS"
            print("\nTurno de las piezas negras")

        movimiento = seleccion_movimiento(tablero)
        movimiento_algebraico = tablero.san(movimiento)
        tablero.push(movimiento)
        num_jugadas += 1

        print(f"{num_jugadas}. {jugador}: {movimiento_algebraico} ")

        print("\n Posicion Tablero")
        print(tablero)

        if tablero.is_game_over(claim_draw=True):

            print("\nFINAL")
            print(tablero)
            print("Resultado:", tablero.result(claim_draw=True))
            print("Motivo:", tablero.outcome(claim_draw=True).termination)


if __name__ == '__main__':

    main()



 
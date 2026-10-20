import chess

VALOR_PIEZAS = {

    chess.PAWN: 100,
    chess.QUEEN: 900,
    chess.BISHOP: 300,
    chess.KNIGHT: 300,
    chess.ROOK: 500,
    chess.KING: 0

} 

VALOR_JAQUEMATE = 100000

def evaluar_tablero(tablero):

    #positivo -> blancas
    #negativo -> negras
    
    if tablero.is_checkmate():

        if tablero.turn == chess.WHITE:

            return -VALOR_JAQUEMATE

        else:

            return VALOR_JAQUEMATE

    if tablero.is_game_over(claim_draw=True):

        return 0

    puntuacion_material = 0

    for tipo_pieza, valor in VALOR_PIEZAS.items():

        piezas_blancas = tablero.pieces(tipo_pieza, chess.WHITE)

        piezas_negras = tablero.pieces(tipo_pieza, chess.BLACK)

        diferencia = len(piezas_blancas) - len(piezas_negras)
        puntuacion_material += diferencia * valor

    return puntuacion_material
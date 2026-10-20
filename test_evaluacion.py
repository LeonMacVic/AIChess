import chess

from evaluacion_tablero import evaluar_tablero, VALOR_JAQUEMATE
from main import seleccion_movimiento



def test_tablero_posicion_inicial():

    tablero = chess.Board()

    assert evaluar_tablero(tablero) == 0

def test_ventaja_piezas_blancas():

    tablero = chess.Board()

    tablero.remove_piece_at(chess.E7)

    assert evaluar_tablero(tablero) == 100

def test_ventaja_piezas_negras():

    tablero = chess.Board()

    tablero.remove_piece_at(chess.D1)

    assert evaluar_tablero(tablero) == -900

def test_jaque_mate():

    tablero = chess.Board()

    tablero.push_san("f3")
    tablero.push_san("e5")
    tablero.push_san("g4")
    tablero.push_san("Qh4#")

    assert tablero.is_checkmate()
    assert evaluar_tablero(tablero) == -VALOR_JAQUEMATE

def test_tablas():

    tablero = chess.Board("7k/8/8/8/8/8/8/K7 w - - 0 1")

    assert tablero.is_insufficient_material()
    assert evaluar_tablero(tablero) == 0

def test_movimiento_legal():

    tablero = chess.Board()

    movimiento = seleccion_movimiento(tablero)

    assert movimiento in tablero.legal_moves

def test_dama_captura():

    #posicion del tablero en la cual se puede capturar una dama con el movimiento a2a7
    tablero = chess.Board("7k/q7/8/8/8/8/R7/K7 w - - 0 1") 

    movimiento = seleccion_movimiento(tablero)

    assert movimiento.uci() == "a2a7"

def test_modificacion_tablero():

    tablero = chess.Board()

    posicion_inicio = tablero.fen()

    seleccion_movimiento(tablero)

    assert posicion_inicio == tablero.fen()


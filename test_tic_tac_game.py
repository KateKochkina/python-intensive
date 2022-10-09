# coverage run --source=tic_tac_game -m pytest -v ./ ; coverage report -m > coverage_report.txt
import mock
import builtins

import pytest

from tic_tac_game import TicTacGame


def test_validate_move_returns_false_when_input_not_int():
    game = TicTacGame()
    assert not game.validate_move("abc")
    assert not game.validate_move("123-")
    assert not game.validate_move(" ")
    assert not game.validate_move("")
    assert game.validate_move("0")


def test_validate_move_returns_false_when_input_not_in_range_9():
    game = TicTacGame()
    assert not game.validate_move("-1")
    assert not game.validate_move("9")
    assert game.validate_move("5")


def test_validate_move_returns_false_when_board_cell_not_empty():
    game = TicTacGame()
    game.board[1] = 1
    assert not game.validate_move("1")
    assert game.validate_move("2")


def test_check_endgame_returns_0_on_draw():
    game = TicTacGame()
    game.board = [
        1, -1, 1,
        1, 1, -1,
        -1, 1, -1
    ]
    assert game.check_endgame() == 0


@pytest.mark.parametrize("side", [1, -1])
def test_check_endgame_returns_1_on_win_horizontal(side):
    game = TicTacGame()
    game.board = [
        side, side, side,
        side, -side, -side,
        -side, side, -side
    ]
    assert game.check_endgame() == side
    game.board = [
        side, -side, -side,
        side, side, side,
        -side, side, -side
    ]
    assert game.check_endgame() == side
    game.board = [
        -side, side, -side,
        side, -side, -side,
        side, side, side
    ]
    assert game.check_endgame() == side


@pytest.mark.parametrize("side", [1, -1])
def test_check_endgame_returns_1_on_win_vertical(side):
    game = TicTacGame()
    game.board = [
        side, -side, side,
        side, -side, side,
        side, side, -side
    ]
    assert game.check_endgame() == side
    game.board = [
        side, side, -side,
        side, side, -side,
        -side, side, side
    ]
    assert game.check_endgame() == side
    game.board = [
        side, -side, side,
        side, -side, side,
        -side, side, side
    ]
    assert game.check_endgame() == side


@pytest.mark.parametrize("side", [1, -1])
def test_check_endgame_returns_1_on_win(side):
    game = TicTacGame()
    game.board = [
        side, -side, side,
        side, side, -side,
        -side, side, side
    ]
    assert game.check_endgame() == side
    game.board = [
        side, -side, side,
        side, side, -side,
        -side, side, side
    ]
    assert game.check_endgame() == side
    game.board = [
        -side, -side, side,
        side, side, -side,
        side, side, -side
    ]
    assert game.check_endgame() == side


test_data = [
    ((x for x in ["4", "1", "3", "2", "5"]), "\nCrosses win!\n"),
    ((x for x in ["4", "0", "7", "1", "6", "2"]), "\nZeros win!\n"),
    ((x for x in ["4", "0", "1", "7", "8", "2", "6", "3", "5"]), "\nDraw!\n"),
]


@pytest.mark.parametrize("input_gen, output_str", test_data)
def test_start_game_prints_correct_result(input_gen, output_str, capsys):
    game = TicTacGame()
    with mock.patch.object(builtins, "input", lambda _: next(input_gen)):
        game.start_game(show_board=False)
    captured = capsys.readouterr()
    assert captured.out == output_str


def test_show_board_runs_wo_errors():
    game = TicTacGame()
    game.show_board()

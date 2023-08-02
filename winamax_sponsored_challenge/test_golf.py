from main import *
import main


BOARD_ONE = [[1, 'H']]  # [['>', -1]]
NEXT_BOARD_ONE_ONE = [['>', 'S']]
BOARD_ONE_SOLUTION = NEXT_BOARD_ONE_ONE
HOLE_POSITION_BOARD_ONE = (1, 0)
BALL_ONE_POSITION_BOARD_ONE = (0, 0)
BOARD_TWO = [[2, '.', 'X'], ['.', '.', 'H'], ['.', 'H', 1]]
NEXT_BOARD_ONE_OF_BOARD_TWO = [['v', '.', 'X'], ['v', '.', 'H'], [1, 'H', 1]]
NEXT_BOARD_TWO_OF_BOARD_TWO = [[2, '.', 'X'], ['.', '.', 'S'], ['.', 'H', '^']]
NEXT_BOARD_THREE_OF_BOARD_TWO = [[2, '.', 'X'], ['.', '.', 'H'], ['.', 'S', '<']]
LIST_OF_POSSIBLE_NEXT_BOARDS_FOR_BOARD_TWO = [
    NEXT_BOARD_ONE_OF_BOARD_TWO,
    NEXT_BOARD_TWO_OF_BOARD_TWO,
    NEXT_BOARD_THREE_OF_BOARD_TWO
]
SOLUTION_BOARD_BOARD_TWO = [['v', '.', 'X'], ['v', '.', 'S'], ['>', 'S', '^']]
HOLE_ONE_POSITION_BOARD_TWO = (2, 1)
HOLE_TWO_POSITION_BOARD_TWO = (1, 2)
LOWEST_BALL_POSITION_BOARD_TWO = (2, 2)
BALL_ONE_POSITION_BOARD_TWO = (0, 0)
BALL_TWO_POSITION_BOARD_TWO = (2, 2)
BOARD_THREE = [[4, '.', '.', 'X', 'X'], ['.', 'H', '.', 'H', '.'], ['.', '.', '.', 'H', '.'], ['.', 2, '.', '.', 2], ['.', '.', '.', '.', '.']]
BOARD_THREE_SOLUTION = [['v', '.', '.', '.', '<'], ['v', '^', '.', '.', '^'], ['v', '^', '.', '^', '^'], ['>', '>', '>', '^', '.']]
BOARD_FOUR = [[3, '.', '.', 'H', '.', 2], ['.', 2, '.', '.', 'H', '.'], ['.', '.', 'H', '.', '.', 'H'], ['.', 'X', '.', 2, '.', 'X'], ['.', '.', '.', '.', '.', '.'], [3, '.', '.', 'H', '.', '.']]
BOARD_FOUR_FIRST_NEXT_BOARD = [['v', '.', '.', 'H', '.', 2], ['v', 2, '.', '.', 'H', '.'], ['v', '.', 'H', '.', '.', 'H'], [2, 'X', '.', 2, '.', 'X'], ['.', '.', '.', '.', '.', '.'], [3, '.', '.', 'H', '.', '.']]
BOARD_FOUR_SOLUTION = [['>', '>', '>', '.', '.', 'v'], ['.', '>', '>', '>', '.', 'v'], ['>', '>', '.', '.', '.', '.'], ['^', '.', '.', 'v', '.', '.'], ['^', '.', '.', 'v', '.', '.'], ['^', '.', '.', '.', '.', '.']]


def test_new_iterative_backtrack_board_one():
    assert new_iterative_backtrack(BOARD_ONE) == BOARD_ONE_SOLUTION
    assert cleanup_board_for_codingame_output(new_iterative_backtrack(BOARD_ONE)) == cleanup_board_for_codingame_output(BOARD_ONE_SOLUTION)

def test_new_iterative_backtrack_board_two():
    assert new_iterative_backtrack(BOARD_TWO) == SOLUTION_BOARD_BOARD_TWO
    assert cleanup_board_for_codingame_output(new_iterative_backtrack(BOARD_TWO)) == cleanup_board_for_codingame_output(SOLUTION_BOARD_BOARD_TWO)

def test_new_iterative_backtrack_board_four():
    assert cleanup_board_for_codingame_output(new_iterative_backtrack(BOARD_FOUR)) == BOARD_FOUR_SOLUTION
    # assert cleanup_board_for_codingame_output(new_interative_backtrack(BOARD_TWO)) == cleanup_board_for_codingame_output(SOLUTION_BOARD_BOARD_TWO)

def test_iterative_backtrack():
#    assert iterative_backtrack(BOARD_ONE, None)[0] == BOARD_ONE_SOLUTION
    assert iterative_backtrack(BOARD_TWO, None)[0] == SOLUTION_BOARD_BOARD_TWO
    #assert iterative_backtrack(BOARD_FOUR, None)[0] == BOARD_FOUR_SOLUTION

def test_iterative_backtrack_board_three():
    assert cleanup_board_for_codingame_output(iterative_backtrack(BOARD_THREE, None)[0]) == BOARD_THREE_SOLUTION
def test_next_board_board_four():
    assert generate_next_boards(BOARD_FOUR)[0] == BOARD_FOUR_FIRST_NEXT_BOARD
#
# def test_backtrack():
#     #assert my_backtrack(BOARD_ONE, BOARD_ONE) == BOARD_ONE_SOLUTION
#     assert my_backtrack(BOARD_TWO, BOARD_TWO) == SOLUTION_BOARD_BOARD_TWO
#     #assert my_backtrack(BOARD_FOUR, BOARD_FOUR) == ''

# def test_recursive_main():
#     #assert recursive_main(BOARD_ONE) == NEXT_BOARD_ONE_ONE
#     #assert recursive_main(BOARD_TWO) == SOLUTION_BOARD_BOARD_TWO
#     assert recursive_main(BOARD_FOUR) == BOARD_FOUR_SOLUTION

def test_get_ball_positions():
    assert get_ball_positions(BOARD_ONE) == [BALL_ONE_POSITION_BOARD_ONE]
    assert get_ball_positions(BOARD_TWO) == [
        BALL_ONE_POSITION_BOARD_TWO,
        BALL_TWO_POSITION_BOARD_TWO
    ]


def test_generate_next_boards():
    assert generate_next_boards(BOARD_ONE) == [NEXT_BOARD_ONE_ONE]
    assert generate_next_boards(BOARD_TWO) == LIST_OF_POSSIBLE_NEXT_BOARDS_FOR_BOARD_TWO


def test_is_in_board():
    assert not is_in_board((0, -1), BOARD_ONE)
    assert is_in_board(HOLE_POSITION_BOARD_ONE, BOARD_ONE)
    assert is_in_board(LOWEST_BALL_POSITION_BOARD_TWO, BOARD_TWO)
    assert not is_in_board((7, 0), BOARD_TWO)

# def test_choose_direction_to_hit_ball():
#     assert choose_direction_to_hit_ball(BOARD_ONE, BALL_ONE_POSITION_BOARD_ONE) == '>'
#     assert choose_direction_to_hit_ball(BOARD_TWO, LOWEST_BALL_POSITION_BOARD_TWO) == ''


def test_get_lowest_number_ball_position_board_one():
    assert main.get_lowest_number_ball_position(BOARD_ONE) == BALL_ONE_POSITION_BOARD_ONE


def test_find_holes_on_board_one():
    assert find_holes_on_board(BOARD_ONE) == [HOLE_POSITION_BOARD_ONE]


def test_find_hole_on_board_two():
    assert find_holes_on_board(BOARD_TWO) == [
        HOLE_ONE_POSITION_BOARD_TWO,
        HOLE_TWO_POSITION_BOARD_TWO
    ]


# def test_choose_direction_to_hit_ball_board_one():
#     assert choose_direction_to_hit_ball(BOARD_ONE, BALL_ONE_POSITION_BOARD_ONE) == '>'


def test_get_lowest_number_ball_position_board_two():

    assert main.get_lowest_number_ball_position(BOARD_TWO) == LOWEST_BALL_POSITION_BOARD_TWO



# def test_choose_direction_to_hit_ball_board_two():
#     assert main.choose_direction_to_hit_ball(BOARD_TWO, LOWEST_BALL_POSITION_BOARD_TWO) == '^'


def test_parse_board():
    assert parse_board("""6 6
3..H.2
.2..H.
..H..H
.X.2.X
......
3..H..""") == [[3, '.', '.', 'H', '.', 2], ['.', 2, '.', '.', 'H', '.'], ['.', '.', 'H', '.', '.', 'H'], ['.', 'X', '.', 2, '.', 'X'], ['.', '.', '.', '.', '.', '.'], [3, '.', '.', 'H', '.', '.']]
    assert parse_board("""6 6
>>>..v
.>>>.v
>>....
^..v..
^..v..
^.....""") == [['>', '>', '>', '.', '.', 'v'], ['.', '>', '>', '>', '.', 'v'], ['>', '>', '.', '.', '.', '.'], ['^', '.', '.', 'v', '.', '.'], ['^', '.', '.', 'v', '.', '.'], ['^', '.', '.', '.', '.', '.']]

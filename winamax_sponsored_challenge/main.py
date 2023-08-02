import random

magic = 0.2
use_magic = True
ready_for_codingame = False


if not ready_for_codingame:
    from visualiser.visualiser import Visualiser as vs

from copy import deepcopy
# from test_golf import BOARD_TWO
DIRECTIONS = ['^', 'v', '<', '>']
MAX_WIDTH = 1000
MAX_HEIGHT = 1000



def board_list_to_board_string(board_list):
    return 'Z'.join(''.join('L' if cell=='<' else 'R' if cell=='>' else str(cell) for cell in row) for row in board_list)

def board_string_to_board_list(board_string):
    return [[int(e) if e.isnumeric() else '<' if e == 'L' else '>' if e=='R' else e for e in row] for row in board_string.split('Z')]

def cleanup_board_for_codingame_output(board):
    return [[x if x not in ['S', 'X'] else '.' for x in row] for row in board]





"""
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
        """


def reject_again(P, c):
    return is_invalid_board(c)

def accept_again(P, c):
    return is_complete_board(c)

def first_again(P, c):
    possible_boards = generate_next_boards(c)
    return possible_boards[0]

def next_again(P, s):
    possible_boards = generate_next_boards(s)
    found_match = False
    for board in possible_boards:
        if found_match:
            return board
        if board == s:
            found_match = True


def wiki_again_backtrack(P, c):
    if reject_again(P, c):
        return
    if accept_again(P, c):
        return P, c
    s = first_again(P, c)
    while s != None:
        wiki_again_backtrack(P, s)
        s = next_again(P, s)


def depth_print(s, depth):
    s = ' '*depth + s
    print(s)


@vs(ignore_args=['board'], node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def new_iterative_backtrack(board_string, depth=0, analysis_output=False):
    board = board_string_to_board_list(board_string)
    # print(f'analysis_output = {analysis_output}')
    if analysis_output:
        depth_print('---', depth)
        depth_print(f'In new_iterative_backtrack with depth = {depth}', depth)
        depth_print('board:\n' + print_board(board), depth)

    # depth += 1
    board = deepcopy(board)
    # if analysis_output:
    #     print('checking is_complete_board')
    if is_complete_board(board):
        if analysis_output:
            depth_print('is_complete_board was True', depth)
        # print(f'found_it at depth {depth}.', board)
        return board_list_to_board_string(board)
    # if analysis_output:
    #     print('checking is_invalid_board')
    elif is_invalid_board(board):
        # print(f'invalid board at depth {depth}.', board)
        if analysis_output:
            depth_print('found invalid board', depth)
        return False
    else:
        if analysis_output:
            depth_print('unknown if board is valid or invalid', depth)
    # if analysis_output:
    #     print('generating next boards')
    next_boards = generate_next_boards(board)
    depth_print(f'length of next boards = {len(next_boards)}', depth)

    for i, next_board in enumerate(next_boards):

        if analysis_output:
            depth_print(f'running new_iterative_backtrack on next_board {i + 1} of {len(next_boards)}', depth)
            depth_print(f'board:\n{print_board(board)}\nendboard', depth)

        board_string = board_list_to_board_string(next_board)
        next_next_board = new_iterative_backtrack(board_string=board_string, depth=depth + 1, analysis_output=analysis_output)
        if next_next_board:
            if analysis_output:
                depth_print(f'found that next_next_board is truthy at depth={depth}', depth)
            return next_next_board
        else:
            depth_print(f'that was board {i + 1} of {len(next_boards)}', depth)
    # return None

def iterative_backtrack(board, solved):
    if solved is False:
        return None, False
    if is_invalid_board(board):
        return None, False
    elif is_complete_board(board):
        return board, True
    next_boards = generate_next_boards(board)
    # results = []
    for next_board in next_boards:
        foo, bar = iterative_backtrack(next_board, None)
        if bar is True:
            return foo, bar
        elif bar is False:
            continue


        # return iterative_backtrack(next_board, None)
    # what to do with results











def accept(P, c):
    if is_complete_board(c):
        return True
    return False


def first(P, c):
    next_boards = deepcopy(generate_next_boards(c))
    if len(next_boards) == 0:
        return None
    else:
        return next_boards[0]




def backtrack(P, c):
    """
    so P is a board. What the heck is c?
    :param P:
    :param c:
    :return:
    """
    if reject(P, c):
        return
    if accept(P, c):
        print(P, c)
    s = first(P, c)
    while s != None:
        backtrack(P, s)
        s = next_(P, s)

def root(P):
    return P, P # !!! todo: not sure about this


def reject(board, c):
    for row in c:
        for cell in row:
            if cell == 0:  # if ball is out of strokes but not in hole
                return True
    return False



def my_backtrack(board, c):
    # print('my_backtrack')
    # print(print_board(c))
    if reject(board, c):
        return
    if accept(board, c):
        print('HI', print_board(c))
        # return board
    s = first(board, c)
    while s!= None:
        my_backtrack(c, s)
        s = next_(c, s)


def next_(board, c):
    possible_boards = generate_next_boards(board)
    found = False
    for board in possible_boards:
        if found:
            return board
        if board == c:
            found = True
    return None
def is_complete_board(board):
    for row in board:
        for cell in row:
            if type(cell) == int and cell >= 0 or cell == 'H':
                return False
    return True


def is_invalid_board(board):
    for row in board:
        for cell in row:
            if cell == 0:
                return True
    #if random.random() > magic:
    #    print('I think this is valid:\n' + print_board(board))

    # this is invalid. I can tell because there is no path
    # from ball with 3 shorts to any hole
    # v..XX
    # vH.S<
    # v..S^
    # v>>^^
    # 3....

    # this is invalid becuase 2 has nowhere to land
    # v..XX
    # vH.S <
    # v..S ^
    # v >> ^ ^
    # >> > 2.

    return False



def recursive_main(board=None):
    return False  # todo delte me
    board
    # for CodinGame: if board is None, read board from input
    if is_complete_board(deepcopy(board)):
        return board
    # if is_invalid_board(deepcopy(board)):
    #     return 'no'
    next_boards = generate_next_boards(deepcopy(board))
    if len(next_boards) == 0:
        pass  # back up and try again
    elif len(next_boards) == 1:
        next_board = next_boards[0]
        return recursive_main(next_board)
    else:
        return [recursive_main(board) for board in next_boards]
    # for next_board in next_boards:
    #     return recursive_main(next_board)

    return 'out-of-boards'

#

# def recursive_main_helper():







def get_ball_positions(board):
    ball_positions = []
    for h, row in enumerate(board):
        for w, cell in enumerate(row):
            if type(cell) == int:
                ball_positions.append((w, h))
    return ball_positions


def filter_boards_for_validity(param):
    pass


def avg_closest_distance_ball_to_hole(board):
    ball_positions = get_ball_positions(board)
    total = 0
    for ball_position in ball_positions:
        current = MAX_WIDTH + MAX_HEIGHT + 2
        hole_positions = get_locations_of_holes(board)
        for hole_position in hole_positions:
            distance = calculate_distance(hole_position, ball_position)
            if distance < current:
                current = distance
        total += current
    return total


def generate_next_boards(board):
    """
    Given a board, generate all valid next boards by hitting
    each ball in each of the possible directions.
    rule out boards that are invalid for the following reasons:
    - ball out of board
    - ball lands in water hazard
    - ball crosses path of other ball
    - anything else?
    - ball lands off hole with zero hits left
    :param board:
    :return:
    """
    new_boards = []
    ball_positions = get_ball_positions(board)
    ball_positions.sort(reverse=True)
    # ball_positions.sort(key=lambda ball_position:)
    directions = DIRECTIONS.copy()
    if use_magic:
        random.shuffle(directions)
    for ball_position in ball_positions:
        for direction in directions:
            new_board, new_position = hit_ball(board, ball_position, direction)
            if type(new_board) == str:
                # hit_ball found that new board was invalid
                continue
            else:
                new_boards.append(new_board)
    new_boards.sort(key=lambda board: avg_closest_distance_ball_to_hole(board))
    return new_boards




# def test():
#     board = [[2, '.', 'X'], ['.', '.', 'H'], ['.', 'H', 1]]
#
#     # position = get_lowest_number_ball_position(board)
#     # print_board(board)
#     direction = choose_direction_to_hit_ball(board, position)
#     print(direction)
#     assert direction == '^'
#
#     assert position == (2, 2)
#     board = hit_ball(board, position, direction='^')
#
#     expected_board = [[2, '.', 'X'], ['.', '.', 0], ['.', 'H', '^']]
#     assert board == expected_board, \
#         f"board: {print_board(board)} expected_board: {print_board(expected_board)}"
#
#     assert False, 'done testing for now, so far so good'


def main():
    # print('sanity check hello world')
    board = []
    width, height = [int(i) for i in input().split()]
    for i in range(height):
        board.append([])
        row = input()
        for char in row:
            try:
                char = int(char)
            except:
                pass
            board[-1].append(char)
    solution_board = new_iterative_backtrack(board)
    # print('sanity check solution board', solution_board)
    cleaned_up_solution_board = cleanup_board_for_codingame_output(solution_board)
    print(print_board(cleaned_up_solution_board))
def print_board(board):
    s = ''  # 'board: '  # print('board:')
    t = []
    for row in board:
        t.append(''.join([str(x) for x in row]))
        # print()
    s += '\n'.join(x for x in t)
    return s


def parse_board(s):
    board = [[int(x) if x.isnumeric() else x for x in line] for line in s.split("\n")[1:]]
    return board


def find_holes_on_board(board):
    positions = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'H':
                positions.append((j, i))
    return positions


def calculate_distance(position_one, position_two):
    return abs(position_two[0] - position_one[0]) + abs(position_two[1] - position_two[1])


def is_in_board(position, board):
    h = len(board)
    w = len(board[0])
    return 0 <= position[0] < w and 0 <= position[1] < h


# def choose_direction_to_hit_ball(board, ball_position):
#     """
#     assume baord has at least one hole
#
#     """
#     # chosen_hole_position = None
#     chosen_direction = None
#     # tentative_ball_position = list(ball_position)
#     smallest_distance_tentative_ball_to_hole = MAX_WIDTH + 1 + MAX_HEIGHT + 1
#     for direction in DIRECTIONS:
#         result_board, result_ball_position = hit_ball(board, ball_position, direction)
#         tentative_ball_position = result_ball_position
#         if result_board == 'out-of-board':
#             continue
#         # if not is_in_board(tentative_ball_position, board):
#         #     continue
#         for hole_position in find_holes_on_board(board):
#             distance_tentative_ball_to_hole = calculate_distance(tentative_ball_position, hole_position)
#             if distance_tentative_ball_to_hole < smallest_distance_tentative_ball_to_hole:
#                 smallest_distance_tentative_ball_to_hole = distance_tentative_ball_to_hole
#                 # chosen_hole_position = hole_position
#                 chosen_direction = direction
#     return chosen_direction
#




    pass
    # first, find closest hole
    positions_of_holes = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'H':
                positions_of_holes.append((i, j))
    smallest_d = 3000
    smallest_hole_position = None
    for position_of_hole in positions_of_holes:
        d = (abs(position_of_hole[0] - ball_position[0])
             + abs(position_of_hole[1] - ball_position[1]))
        if d < smallest_d:
            smallest_d = d
            smallest_hole_position = position_of_hole
    assert smallest_hole_position is not None
    # print(smallest_hole_position, 'smallest_hole_position')
    # print('ball_position', ball_position)
    direction = None
    if (abs(smallest_hole_position[0] - ball_position[0]) <
            abs(smallest_hole_position[1] - ball_position[1])):  # if horizontal distance is less
        # move in left/right motion
        if smallest_hole_position[0] < ball_position[0]:
            # hit left
            direction = '<'
        else:
            # hit right
            direction = '>'
    else:
        # move in up/down motion
        if smallest_hole_position[1] < ball_position[1]:
            # move up
            direction = '^'
        else:
            # move down
            direction = 'v'

    assert direction is not None
    return direction

    # calculate distance from ball position
    # to hole


def hit_ball(board, position=(0, 1), direction='v'):
    """
    :param board:
    :param position:
    :param direction:
    :return: board, position OR 'out-of-board', 'hello'

    given a board, a position, and a direction
    assuming the position contains a ball
    move the ball in direction by a number of
    spaces equal to the integer that represents
    the ball, and decrease the integer of the ball
    by one
    return the new board, with a direction arrow
    indicating where the ball was hit from
    """
    starting_position = position
    board = deepcopy(board)
    ball_integer = board[position[1]][position[0]]


    for step_number in range(ball_integer)[::-1]:
        board[position[1]][position[0]] = direction
        if direction == '^':
            up = -1 * 1
            right = 0
            position = (position[0] + right, position[1] + up)

        elif direction == 'v':
            up = 1
            right = 0
            position = (position[0] + right, position[1] + up)

        elif direction == '<':
            up = 0
            right = -1
            position = (position[0] + right, position[1] + up)

        elif direction == '>':
            up = 0
            right = 1
            position = (position[0] + right, position[1] + up)
        # check for crossing path of other ball
        if not is_in_board(position, board):
            return 'out-of-board', 'hello'
        if board[position[1]][position[0]] in DIRECTIONS:
            return 'crossed-ball-path', 'hello'
        if type(board[position[1]][position[0]]) == int:
            return 'crossed-path-of-ball', 'hello'
        if step_number > 0 and board[position[1]][position[0]] == 'H':
            return 'crossed-path-of-hole', 'hello'
        #board[position[1]][position[0]] = direction
    # beyond this point, "position" is the tentative new position

    if not is_in_board(position, board):
        return 'out-of-board', 'hello'
    # check water hazard
    elif board[position[1]][position[0]] == 'X':
        return 'water-hazard', 'hello'
    # check if ball is in hole
    elif board[position[1]][position[0]] == 'H':
        ball_integer = 'S'
    # # check if ball is out of shots but not in hole
    # elif ball_integer -1 == 0:
    #     return 'out-of-shots', 'hello'
    # to access position (w, h), use board[h][w]
    if ball_integer == 'S':
        board[position[1]][position[0]] = ball_integer
    else:
        board[position[1]][position[0]] = ball_integer - 1
    if ball_integer == 0:
        return 'ball is out of gas', 'hi'
    return board, position


def get_lowest_number_ball_position(board):
    """
    given a board, and assuming there is at least one
    ball on the board, retrieve the position of the ball
    with the smallest number interger.
    if there is more than one ball with the same smallest
    integer, simply take the first ball
    """
    lowest_int = 10
    position = None
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if type(cell) == int:
                if cell < lowest_int:
                    lowest_int = cell
                    position = (i, j)
    assert position is not None
    return position


def get_locations_of_holes(board):
    hole_positions = []
    for h, row in enumerate(board):
        for w, cell in enumerate(row):
            if cell == 'H':
                hole_positions.append((w, h))
    return hole_positions



def get_closest_hole(board):
    pass



if __name__ == '__main__':
    # test()

    if not ready_for_codingame:
        my_test = new_iterative_backtrack(board_string=board_list_to_board_string([[4, '.', '.', 'X', 'X'], ['.', 'H', '.', 'H', '.'], ['.', '.', '.', 'H', '.'], ['.', 2, '.', '.', 2], ['.', '.', '.', '.', '.']]), depth=0, analysis_output=True)
        #my_test = new_iterative_backtrack(baord='4..xx\n.H.H.')
        # my_test = new_iterative_backtrack(board_string=board_list_to_board_string([[2, '.', 'X'], ['.', '.', 'H'], ['.', 'H', 1]]), analysis_output=True)
        print('done')
        print(print_board(my_test))
        vs.make_animation("codingame.gif", delay=2)

    # my_test = wiki_again_backtrack([[2, '.', 'X'], ['.', '.', 'H'], ['.', 'H', 1]], [[2, '.', 'X'], ['.', '.', 'H'], ['.', 'H', 1]])
    # print(print_board((my_test[0])))
    if ready_for_codingame:
        main()



# 2.X
# ..H
# .H1

# intutively, start with the balls with lower numbers of shots available
# next, choose the "easiest" path for that ball towards a hole

# v..
# v..
# >.^
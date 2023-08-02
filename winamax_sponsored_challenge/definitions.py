# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Board is a list of lists, containing one of:
# [
#  [  ]
#  [  ]
#  [  ]
#      ]
# [[] [] []]
# - '.'
# - '{integer 1 through 9}', representing a ball with integer str
# - integer 0, representing a ball out of strokes and not in a hole
# 'S', representing a sunk ball in a hole
# - 'X'
# - 'H'

# ball is integer 1 through 9 inclusive
# the number represents that number of shots available
# and the power of the next shot
# or ball in 0, indicating a ball that is in a hole and out
# of shots

# position is a tuple(int, int)
# (width, height)
# indexed from 0. top left is zero
# so, for example (2, 0) is x
# and for example (0, 1) is y
# and
# [
#  [..x]
#  [y..]
#  [...]
#      ]
# furthermore, width is the index of the inner list
# height is the index of the outer list
# so the patter for accessing a board element as position (w, h)
# is board[h][w]

# def construct_board()
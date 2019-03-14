ALLOW_WRAPPING = False

def is_valid_robot_move(robot_pos, robot_move, board):
    """
    Rules for valid robot move:
        * Cannot go beyond map
        * Can only go 1 square from previous position (no wrapping)
        * Cannot go thru barrier objects on board
        * CAN go thru death objects on board
    """
    global ALLOW_WRAPPING

    max_row = len(board) - 1
    max_col = len(board[0]) - 1

    # move cannot be more than 1 unit in any direction
    if robot_move['row'] < -1 or robot_move['row'] > 1:
        return False
    if robot_move['col'] < -1 or robot_move['col'] > 1:
        return False

    # Check boundaries depending on whether WRAPPING is on or off
    if robot_move['row'] + robot_pos['row'] > max_row :
        return ALLOW_WRAPPING
    if robot_move['col'] + robot_pos['col'] > max_col :
        return ALLOW_WRAPPING
    if robot_move['row'] + robot_pos['row'] < 0 :
        return ALLOW_WRAPPING
    if robot_move['col'] + robot_pos['col'] < 0 :
        return ALLOW_WRAPPING

    # Check if landing on legal square
    ILLEGAL_BLOCKS = {}

    new_pos = { 'col': robot_pos['col'] + robot_move['col'],
                'row': robot_pos['row'] + robot_move['row'] }
    new_board_pos = board[new_pos['row']][new_pos['col']]

    if new_board_pos in ILLEGAL_BLOCKS:
        return False

    return True


def update_robot_pos(robot_pos, robot_move, board):
    global ALLOW_WRAPPING

    max_row = len(board) - 1
    max_col = len(board[0]) - 1

    # TODO check illegal chars


    if ALLOW_WRAPPING:
        pass
        # TODO: handle wrapping if necessary

    # new_col = (robot_pos['col'] + 1) % len(board[0])
    # robot_pos['col'] = new_col

    # print(new_col)

    # return robot_pos['row'], new_col
    robot_pos['col'] += robot_move['col']
    robot_pos['row'] += robot_move['row']


def update_score(robot_pos, board):
    """
    """
    cel = board[robot_pos['row']][robot_pos['col']]
    # if cel == -1:
    #     return 0

    return cel

def update_board(board, robot_pos):
    """
    """
    board[robot_pos['row']][robot_pos['col']] = 0

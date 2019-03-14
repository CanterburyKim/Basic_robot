"""
Initialization helper code
"""
import pygame
import csv

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def init_properties(prop_file):
    """
    read a properties file and put it into a dictionary.
    return the dictionary
    """
    props = dict()
    with open(prop_file) as inf:
        for line in inf:
            if len(line.strip())==0 or line.strip()[0]=='#':
                continue
            line_data = line.strip().split('=')
            prop_key = line_data[0]
            prop_value = line_data[1]
            if prop_value.isnumeric():
                prop_value = int(prop_value)
            props[prop_key]=prop_value
    return props


def init_screen(screen_size):
    size = (screen_size['x'], screen_size['y'])
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Canterbury Robot Game")
    return screen



def init_board(board_file):
    board = []

    with open(board_file) as inf:
        csvreader = csv.reader(inf)
        line_1 = next(csvreader)
        line_2 = next(csvreader)
        r = int(line_1[0])
        c = int(line_1[1])
        steps = int(line_2[0])
        print(r,c,steps)
        for row in csvreader:
            board_row = []
            for i, item in enumerate(row):
                board_row.append(int(item))
            board.append(board_row)
    return board, (r,c), steps

def load_robot_img(robot_img_file, cel_size):
    img = pygame.image.load(robot_img_file)
    img = pygame.transform.scale(img, (cel_size['x'], cel_size['y']) )
    return img

def load_robot_moves(robot_move_file):
    """
    """
    robot_moves = []
    with open(robot_move_file) as inf:
        first_line= next(inf)
        print(f'<{first_line}>')
        first_line = first_line.strip()
        if first_line != 'row,col':
            print('******* HEADER ROW IS MALFORMED *******')
        # row_title = first_line.split(',')[0].strip()
        row_title = 'row'
        # col_title = first_line.split(',')[1].strip()
        col_title = 'col'
        print(row_title, col_title)
        for line in inf:
            if len(line.strip()) ==0 or line[0].isalpha():
                pass
            else:
                foo = line.strip().split(',')
                robot_move = { row_title: int(foo[0]), col_title: int(foo[1]) }
                robot_moves.append(robot_move)
    return robot_moves

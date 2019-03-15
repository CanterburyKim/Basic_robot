import pygame

BLACK = 0,0,0
RED = 0xff, 0,0
GREEN = 0, 0xff, 0
BLUE = 0,0, 0x4f
BLUE_2 = 0,0, 0x9f
BLUE_3 = 0,0, 0xff
YELLOW = 0xff, 0xff, 0
WHITE = 0xff, 0xff, 0xff

COLOR_MAP = {
    0 : RED,
    1 : GREEN,
    2 : BLUE,
    3 : BLUE,
    4 : BLUE,
    5 : BLUE_2 ,
    6 : BLUE_2 ,
    7 : BLUE_2 ,
    8 : BLUE_3 ,
    9 : BLUE_3 ,

    -1 : YELLOW,
    -2 : YELLOW ,
    -3 : YELLOW ,
    -4 : YELLOW ,
    -5 : YELLOW ,
    -6 : YELLOW ,
    -7 : YELLOW ,
    -8 : YELLOW ,
    -9 : YELLOW

}

def clear_screen(screen):
    screen.fill( WHITE )

def draw_board(screen, board, cel_size):
    """
    """
    num_rows = len(board)
    num_cols = len(board[0])

    for row in range(num_rows):
        for col in range(num_cols):

            x_coord = cel_size['x'] * col
            y_coord = cel_size['y'] * row

            color = COLOR_MAP[ board[row][col] ]

            pygame.draw.rect(screen, color, (x_coord, y_coord, cel_size['x'], cel_size['y']))


def draw_robot(screen, robot_img, robot_pos, cel_size):
    coord = robot_pos['col'] * cel_size['x'], robot_pos['row'] * cel_size['y']
    screen.blit(robot_img, coord)


def draw_score(screen, my_font, score, robot_move, info_screen):
    info_rect = (info_screen['x.start'], info_screen['y.start'],
            info_screen['x.end'], info_screen['y.end']
            )
    pygame.draw.rect(screen, WHITE, info_rect)
    textsurface1 = my_font.render(f'Score: {score}', False, (0, 0, 0))
    textsurface2 = my_font.render(f'Move : {robot_move}', False, (0, 0, 0))

    text_x = info_screen['x.start'] + 10
    text_y = info_screen['y.start'] + 10
    screen.blit(textsurface1, (text_x, text_y) )
    screen.blit(textsurface2, (text_x, text_y+25) )

def do_game_over(screen, my_font, info_screen):
    # pygame.draw.rect(screen, WHITE, (0, 900, 900, 1100))

    textsurface = my_font.render('Game is now over', False, (0xff, 0, 0))
    x_coord = info_screen['x.start'] + 10
    y_coord = ( info_screen['y.end'] - info_screen['y.start'] ) // 2 - 20
    y_coord = info_screen['y.start'] + y_coord
    start_pos = x_coord, y_coord
    screen.blit(textsurface, start_pos )

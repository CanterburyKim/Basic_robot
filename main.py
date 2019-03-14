import pygame
import random as rnd
import os
from init_helper import *
from draw_helper import *
from move_helper import *


MY_DIR = os.path.dirname(os.path.realpath(__file__))
MY_PROPERTIES_FILE = 'robot.properties'
# MY_MAP_FILE = 'robot.map'
MY_MAP_FILE = ''
ROBOT_IMAGE_FILE = 'robot.png'
# ROBOT_MOVE_FILE = 'robot.moves'


MAX_NUM_MOVES = 0

def main():
    global ALLOW_WRAPPING
    global MAX_NUM_MOVES

    score = 0

    # Properties
    props = init_properties(MY_DIR + '/' + MY_PROPERTIES_FILE)
    screen_size ={ 'x':props['screen.size.x'] ,
        'y':props['screen.size.y'] }
    full_screen_size = { 'x':props['screen.size.x'] ,
        'y':props['screen.size.y'] + props['info.screen.height'] }
    info_screen_height = props['info.screen.height']

    info_screen = { 'x.start': 0, 'x.end': screen_size['x'],
                    'y.start': screen_size['y'], 'y.end': screen_size['y'] + info_screen_height }

    print(info_screen)

    # map_size = { 'row': props['map.num.rows'], 'col':props['map.num.cols'] }

    # robot_pos = { 'row': props['robot.start.row'], 'col': props['robot.start.col'] }
    ALLOW_WRAPPING = (props['allow.wrapping'] == 1)
    # MAX_NUM_MOVES = props['max.num.moves']
    MY_MAP_FILE = props['map.file']

    # Load Board
    board, pos, num_moves = init_board(MY_DIR + '/' + MY_MAP_FILE)

    robot_pos = { 'row': pos[0], 'col': pos[1] }
    MAX_NUM_MOVES = num_moves
    print('max is', MAX_NUM_MOVES)

    map_size = { 'row': len(board),
    'col': len(board[0])
    }
    cel_size = { 'x': screen_size['x'] // map_size['col'], 'y': screen_size['y']//map_size['row']}


    # get the points for the initial placement
    score += board[robot_pos['row']][robot_pos['col']]
    board[robot_pos['row']][robot_pos['col']] = 0

    # load the move file
    ROBOT_MOVE_FILE = props['move.file']

    robot_img = load_robot_img(MY_DIR + '/' + ROBOT_IMAGE_FILE, cel_size )
    robot_moves = load_robot_moves(MY_DIR + '/' + ROBOT_MOVE_FILE)
    print( robot_moves)

    # PyGame Init
    pygame.init()
    screen = init_screen(full_screen_size)
    pygame.font.init()

    font_name = props['font']
    # my_font = pygame.font.SysFont('Comic Sans MS', 30)
    # my_font = pygame.font.SysFont(font_name, 30)
    my_font = pygame.font.Font(MY_DIR + '/Comic Sans MS.ttf', 24)

    # my_font = pygame.font.get_default_font()
    clock = pygame.time.Clock()


    # foo = pygame.font.get_fonts()
    # print(foo)



    done = False

# do first draw
    clear_screen(screen)
    draw_board(screen, board, cel_size)
    draw_robot(screen, robot_img, robot_pos, cel_size)
    draw_score(screen, my_font, 0, 0, info_screen)

    pygame.display.flip()

    move_num = 0

    # Main loop
    while not done:

        pygame.time.delay(1000)

        # Handle any Events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if( move_num >= len(robot_moves) or move_num+1 > MAX_NUM_MOVES):
            # Game is Over
            print(move_num, MAX_NUM_MOVES)
            do_game_over(screen, my_font, info_screen)
            pygame.display.flip()
            continue

        # Get next move
        robot_move=robot_moves[move_num]
        is_valid = is_valid_robot_move(robot_pos, robot_move, board)

        if not is_valid:
            print('NOT VALID')
            # set move_num to max+1 if you want to auto-disqualify
            # for an illegal move
            # otherwise just ignore and keep going
            # move_num = MAX_NUM_MOVES + 1

        if is_valid:

            # Do the updates
            update_robot_pos(robot_pos, robot_move, board)
            score += update_score(robot_pos, board)
            update_board(board, robot_pos)

        move_num += 1

        # Do Drawing
        draw_board(screen, board, cel_size)
        draw_robot(screen, robot_img, robot_pos, cel_size)
        draw_score(screen, my_font, score, move_num, info_screen)

        # Blit
        pygame.display.flip()

        clock.tick(60)

        pass


if __name__ == '__main__' :
    main()

from random import randrange
import os

num_rows = 40
num_cols = 40
starting_pos = (19,19)
num_steps = 30


MY_DIR = os.path.dirname(os.path.realpath(__file__))
fname = f'robot.map.{num_rows}x{num_cols}.map'

with open(MY_DIR + '/' + fname, 'w') as outf:
    outf.write(f'{starting_pos[0]}, {starting_pos[1]}\n')
    outf.write(f'{num_steps}\n')
    for r in range(num_rows):
        for c in range(num_cols-1):
            position_val = randrange(10)
            outf.write( f'{position_val}, ' )

        position_val = randrange(10)
        outf.write( f'{position_val}, \n' )

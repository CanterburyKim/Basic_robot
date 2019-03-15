from random import randrange
import os

num_rows = 70
num_cols = 70
starting_pos = (5,5)
num_steps = 35

MY_DIR = os.path.dirname(os.path.realpath(__file__))
fname = f'robot.map.{num_rows}x{num_cols}.map'

with open(MY_DIR + '/' + fname, 'w') as outf:
    outf.write(f'{starting_pos[0]}, {starting_pos[1]}\n')
    outf.write(f'{num_steps}\n')
    for r in range(num_rows):
        for c in range(num_cols-1):
            do_special = ( randrange(10) < 2 )
            value = randrange(10) * (-1 if randrange(13) < 1 else 1)
            position_val = value if do_special else 1
            outf.write( f'{position_val}, ' )

        # do_special = ( randrange(10) > 8 )
        # position_val = randrange(10) if do_special else 1
        position_val = -1
        outf.write( f'{position_val} \n' )

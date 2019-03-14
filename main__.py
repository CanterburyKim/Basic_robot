if True:
    exit()

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Canterbury Robot Game")


# do_init('')
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # bgimage = pygame.image.load(MY_DIR + '/fractal.png')
    # screen.blit(bgimage, (0,0))
    # pygame.display.flip()
    # screen.fill(GREEN)

    # --- Drawing code should go here
    num_cells_x = 10
    num_cells_y = 10
    for j in range(num_cells_y):
        for i in range(num_cells_x):
            width = size[0] // num_cells_x
            height = size[1] // num_cells_y

            x_coord = width * i
            y_coord = height * j

            b = rnd.randrange(2)
            color = WHITE if b == 1 else BLACK
            pygame.draw.rect(screen, color, (x_coord, y_coord, width, height))



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick()

# Close the window and quit.
pygame.quit()


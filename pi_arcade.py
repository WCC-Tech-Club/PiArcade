import pygame
import pygame.key
import pygame.draw

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
running = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Used to test key input, joystick input, and framerate independence
framerate = 60
speed = 500
position = [int(size[0] / 2), int(size[1] / 2)]
deltaTime = 1 / framerate

# Joystick init
pygame.joystick.init()
hasJoystick = pygame.joystick.get_count() > 0

# -------- Main Program Loop -----------
while running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Game logic should go here

    # Key Input
    pressedKeys = pygame.key.get_pressed()

    if hasJoystick:
        # Use joystick if one exists
        joystick = pygame.joystick.Joystick(0)

        # It is unknown what axis will be x and what will be y
        # Experiment and swap them out once we have a joystick to test with
        position[0] += joystick.get_axis(0) * speed * deltaTime
        position[1] += joystick.get_axis(1) * speed * deltaTime
    else:
        # Use keyboard if joystick does not exist
        if pressedKeys[pygame.K_a] or pressedKeys[pygame.K_LEFT]:
            position[0] -= int(speed * deltaTime)

        if pressedKeys[pygame.K_d] or pressedKeys[pygame.K_RIGHT]:
            position[0] += int(speed * deltaTime)

        if pressedKeys[pygame.K_w] or pressedKeys[pygame.K_UP]:
            position[1] -= int(speed * deltaTime)

        if pressedKeys[pygame.K_s] or pressedKeys[pygame.K_DOWN]:
            position[1] += int(speed * deltaTime)

    # Clamp position to screen
    if position[0] < 0:
        position[0] = 0

    if position[0] > size[0]:
        position[0] = size[0]

    if position[1] < 0:
        position[1] = 0

    if position[1] > size[1]:
        position[1] = size[1]

    # Debug position and delta time
    print(str(position[0]) + " : " + str(position[1]) + " : " + str(deltaTime));

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here

    # Draw a circle at position
    pygame.draw.circle(screen, BLUE, position, 40)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    deltaTime = clock.tick_busy_loop(framerate) / 1000
 
# Close the window and quit.
pygame.quit()

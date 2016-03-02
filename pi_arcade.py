import math

import pygame
import pygame.key
import pygame.draw
import pygame.sprite

import spritesheet

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Player class with hard coded sprite
class Player(pygame.sprite.Sprite):

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        # Hard coded sprite loading
        self.spriteSheet = spritesheet.SpriteSheet("sphere.png")
        self.sprites = []
        self.animFramerate = 60.0

        self.reload_sprites()

        self.image = None
        self.rect = None
        self.set_image(0, center)

    def get_anim_framerate(self):
        return self.animFramerate

    def set_anim_framerate(self, anim_ramerate):
        self.animFramerate = anim_ramerate

    def reload_sprites(self):
        # Hard coded sprite loading
        self.sprites = self.spriteSheet.images_at(
            [
                (0, 0, 64, 64),
                (64, 0, 64, 64),
                (128, 0, 64, 64),
                (192, 0, 64, 64),
                (256, 0, 64, 64),
                (320, 0, 64, 64),
                (384, 0, 64, 64),
                (448, 0, 64, 64),
                (0, 64, 64, 64),
                (64, 64, 64, 64),
                (128, 64, 64, 64),
                (192, 64, 64, 64),
                (256, 64, 64, 64),
                (320, 64, 64, 64),
                (384, 64, 64, 64),
                (448, 64, 64, 64),
                (0, 128, 64, 64),
                (64, 128, 64, 64),
                (128, 128, 64, 64),
                (192, 128, 64, 64),
                (256, 128, 64, 64),
                (320, 128, 64, 64),
                (384, 128, 64, 64),
                (448, 128, 64, 64),
                (0, 192, 64, 64),
                (64, 192, 64, 64),
                (128, 192, 64, 64),
                (192, 192, 64, 64),
                (256, 192, 64, 64),
                (320, 192, 64, 64),
                (384, 192, 64, 64),
                (448, 192, 64, 64),
            ], [255, 0, 255]  # Color Key for alpha
        )

    def set_image(self, sprite_index, center):
        self.image = self.sprites[sprite_index]
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self, *args):
        image_index = int((pygame.time.get_ticks() / 1000.0) * self.animFramerate) % 32
        self.set_image(image_index, args[0])

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
background = pygame.image.load("background.jpg").convert()

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Used to test key input, joystick input, and framerate independence
position = [size[0] / 2, size[1] / 2]
player = pygame.sprite.GroupSingle(Player(position))
circleRadius = 32
framerate = 60
speed = 500
deltaTime = 1 / framerate
joyTolerance = 0.2

# Joystick initialization
pygame.joystick.init()
hasJoystick = False
joystick = None

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    hasJoystick = joystick.get_numaxes() >= 2

print("Has Joystick: " + str(hasJoystick))

# -------- Main Program Loop -----------
while running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Game logic should go here

    # Input
    movement = [0.0, 0.0]

    if hasJoystick:
        # Use joystick if one exists

        # D-Pad (digital joystick)
        # hat = joystick.get_hat(0)
        # movement[0] = hat[0]
        # movement[1] = -hat[1]

        # Actual Joystick (analog joystick)
        movement[0] = joystick.get_axis(0)
        movement[1] = joystick.get_axis(1)

        # Tolerance check to correct hardware imprecision
        if abs(movement[0]) < joyTolerance:
            movement[0] = 0

        if abs(movement[1]) < joyTolerance:
            movement[1] = 0

    else:
        # Use keyboard if joystick does not exist
        pressedKeys = pygame.key.get_pressed()

        # Input logic for keys designed to zero out movement when
        # both keys on axis are pressed (up/down or left/right)
        if pressedKeys[pygame.K_a] or pressedKeys[pygame.K_LEFT]:
            movement[0] -= 1

        if pressedKeys[pygame.K_d] or pressedKeys[pygame.K_RIGHT]:
            movement[0] += 1

        if pressedKeys[pygame.K_w] or pressedKeys[pygame.K_UP]:
            movement[1] -= 1

        if pressedKeys[pygame.K_s] or pressedKeys[pygame.K_DOWN]:
            movement[1] += 1

    # Normalize movement
    sqMagnitude = (movement[0] * movement[0]) + (movement[1] * movement[1])
    if sqMagnitude > 1:
        magnitude = math.sqrt(sqMagnitude)
        movement[0] /= magnitude
        movement[1] /= magnitude

    # Apply movement modified by speed and delta time to position
    position[0] += movement[0] * speed * deltaTime
    position[1] += movement[1] * speed * deltaTime

    # Clamp position to screen
    if position[0] < 0 + circleRadius:
        position[0] = 0 + circleRadius

    if position[0] > size[0] - circleRadius:
        position[0] = size[0] - circleRadius

    if position[1] < 0 + circleRadius:
        position[1] = 0 + circleRadius

    if position[1] > size[1] - circleRadius:
        position[1] = size[1] - circleRadius

    player.update(position)

    # Debug position and delta time
    # print(str(position[0]) + " : " + str(position[1]) + " : " + str(deltaTime));

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # screen.fill(WHITE)
    screen.blit(background, (0, 0))

    # --- Drawing code should go here

    # Draw a circle at position
    # pygame.draw.circle(screen, BLUE, [int(position[0]), int(position[1])], circleRadius)
    player.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    deltaTime = clock.tick_busy_loop(framerate) / 1000.0

# Close the window and quit.
pygame.quit()

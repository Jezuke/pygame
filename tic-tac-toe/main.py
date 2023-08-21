import pygame
import sys

# TODO clean up Grid by closing borders and centering grid at a smaller scale

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
GRID_SIZE = 3
CELL_SIZE = min(SCREEN_WIDTH, SCREEN_HEIGHT) // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Calculate grid position to center it
grid_x = (SCREEN_WIDTH - CELL_SIZE * GRID_SIZE) // 2
grid_y = (SCREEN_HEIGHT - CELL_SIZE * GRID_SIZE) // 2

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Centered 3x3 Grid")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw vertical lines
    for x in range(0, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (grid_x + x * CELL_SIZE, grid_y),
                         (grid_x + x * CELL_SIZE, grid_y + CELL_SIZE * GRID_SIZE), 2)

    # Draw horizontal lines
    for y in range(0, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (grid_x, grid_y + y * CELL_SIZE),
                         (grid_x + CELL_SIZE * GRID_SIZE, grid_y + y * CELL_SIZE), 2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

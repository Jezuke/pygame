import pygame
import math
import sys

# TODO clean up Grid by closing borders and centering grid at a smaller scale

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 750, 750
CELL_SIZE = 150
CENTER_CELL_X = (SCREEN_WIDTH-CELL_SIZE)//2
CENTER_CELL_Y = (SCREEN_HEIGHT-CELL_SIZE)//2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Centered 3x3 Grid")
font = pygame.font.Font(size=32)

# Functions
def print_grid():
    for x in range(math.ceil(SCREEN_WIDTH/CELL_SIZE)):
        for y in range(math.ceil(SCREEN_HEIGHT/CELL_SIZE)):
            pygame.draw.line(screen, BLACK, (x*CELL_SIZE, CELL_SIZE), (x*CELL_SIZE,SCREEN_HEIGHT-CELL_SIZE))
            pygame.draw.line(screen, BLACK, (CELL_SIZE, y*CELL_SIZE), (SCREEN_WIDTH-CELL_SIZE,y*CELL_SIZE))
   
            text = font.render(str((x,y)),True, BLACK, WHITE)
            textRect = text.get_rect()
            textRect.center = (x*CELL_SIZE+(CELL_SIZE/2), y*CELL_SIZE+(CELL_SIZE/2))
            screen.blit(text, textRect)

# Main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)
        
        print_grid()

        """
            if user clicks on box:
                if box is empty:
                    if state is 'x':
                        render 'x' in box
                    else:
                        render 'o' in box
            
            if winning state:
                end game declare winner
        """
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



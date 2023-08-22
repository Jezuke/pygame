import pygame
import math
import sys

# TODO Bind click events to grid and alter 'X' and 'O'

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
font = pygame.font.Font(size=64)

# Global variables
clicked = False
markers = []
# Functions
def print_grid():
    for x in range(math.ceil(SCREEN_WIDTH/CELL_SIZE)):
        for y in range(math.ceil(SCREEN_HEIGHT/CELL_SIZE)):
            pygame.draw.line(screen, BLACK, (x*CELL_SIZE, CELL_SIZE), (x*CELL_SIZE,SCREEN_HEIGHT-CELL_SIZE))
            pygame.draw.line(screen, BLACK, (CELL_SIZE, y*CELL_SIZE), (SCREEN_WIDTH-CELL_SIZE,y*CELL_SIZE))

            # REVIEW: Remove, using for grid debugging purposes
            # text = font.render(str((x,y)),True, BLACK, WHITE)
            # textRect = text.get_rect()
            # textRect.center = (x*CELL_SIZE+(CELL_SIZE/2), y*CELL_SIZE+(CELL_SIZE/2))
            # screen.blit(text, textRect)

def print_markers():
    for mark in markers:
        text = font.render("X", True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = (mark[0]*CELL_SIZE+(CELL_SIZE/2), mark[1]*CELL_SIZE+(CELL_SIZE/2))
        screen.blit(text, textRect)

def add_marker():
    global clicked
    if clicked == True:
        x,y = pygame.mouse.get_pos()
        row = 0
        column = 0

        # Determine column
        if(x < CELL_SIZE*2):
            column = 1
        elif(x < CELL_SIZE*3):
            column = 2
        elif(x < CELL_SIZE*4):
            column = 3

        # Determine row
        if(y < CELL_SIZE*2):
            row = 1
        elif(y < CELL_SIZE*3):
            row = 2
        elif(y < CELL_SIZE*4):
            row = 3
        
        if row and column:
            markers.append((column, row))

        
# Main loop
def main():
    global clicked
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False

        # Clear the screen
        screen.fill(WHITE)
        
        print_grid()
        print_markers()
        add_marker()
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



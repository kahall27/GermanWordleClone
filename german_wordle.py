from re import L
from turtle import write_docstringdict
import pygame
from pygame.locals import *

WINDOW_HEIGHT, WINDOW_WIDTH = 800, 500
BACKGROUND = (144, 238, 144)
GRAY = (100, 100, 100)

def draw_boxes(screen):
    for i in range(6):
        from_top = (i * 60) + ((i + 1) * 30)   # equal spacing between boxes
        for j in range(5):
            from_left = ((WINDOW_WIDTH - 300) / 6)* (j + 1) + (j * 60)  # equal spacing between boxes
            pygame.draw.rect(screen, GRAY, pygame.Rect(from_left, from_top, 60, 60), border_radius=3)

def draw_keyboard(screen):
    row_one = ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü"]
    row_two = ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä"]
    row_three = ["Y", "X", "C", "V", "B", "N", "M"]
    rows = [row_one, row_two, row_three]

    font = pygame.font.Font('freesansbold.ttf', 26)
    row_idx = 0
    for row in rows:

        for i in range(len(row)):

            from_top = 600 + (60 * row_idx)
            from_left = (((WINDOW_WIDTH - len(row_one) * 30)) / (len(row_one) + 1)) * (i + 1) + (i * 30)    # use row_one length to ensure consistent spacing
            if row == row_three:
                from_left += (WINDOW_WIDTH - 324) / 2    # center bottom row of keys

            pygame.draw.rect(screen, GRAY, pygame.Rect(from_left, from_top, 30, 40), border_radius=3)

            text = font.render(row[i], True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (from_left + 15, from_top + 20)
            screen.blit(text, textRect)
    
        row_idx += 1
    

def main():
    # Initialize screen
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Wordle in German!')

    # Fill background
    screen.fill(BACKGROUND)


    # Event loop
    while True:

        # clock.tick(75)
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            # if event.type == pygame.KEYDOWN:

        screen.fill(BACKGROUND)
        draw_boxes(screen)
        draw_keyboard(screen)
        pygame.display.update()

if __name__ == '__main__': main()
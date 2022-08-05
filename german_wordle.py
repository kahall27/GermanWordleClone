from re import L
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
        pygame.display.update()

if __name__ == '__main__': main()
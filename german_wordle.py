import pygame
from pygame.locals import *

WINDOW_HEIGHT, WINDOW_WIDTH = 800, 500
BACKGROUND = (144, 238, 144)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

row_one = ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü"]
row_two = ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä"]
row_three = ["Y", "X", "C", "V", "B", "N", "M"]
rows = [row_one, row_two, row_three]

list_of_guesses = []
# initially all letters are gray
letter_colors = {letter: GRAY for letter in row_one + row_two + row_three}
letter_colors["backspace"] = GRAY
letter_colors["enter"] = GRAY
letter_locations = {letter: () for letter in row_one + row_two + row_three}

def draw_boxes(screen, current_word, current_guess_idx):
    font = pygame.font.Font('freesansbold.ttf', 32)
    for i in range(6):
        from_top = (i * 60) + ((i + 1) * 30)   # equal spacing between boxes
        for j in range(5):
            from_left = ((WINDOW_WIDTH - 300) / 6)* (j + 1) + (j * 60)  # equal spacing between boxes
            pygame.draw.rect(screen, GRAY, pygame.Rect(from_left, from_top, 60, 60), border_radius=3)
            if len(list_of_guesses) > i and len(current_word) > j:
                text = font.render(current_word[j], True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (from_left + 30, from_top + 30)
                screen.blit(text, textRect)


def draw_keyboard(screen):

    font = pygame.font.Font('freesansbold.ttf', 26)
    row_idx = 0
    from_top = 0
    from_left = 0
    for row in rows:

        for i in range(len(row)):

            from_top = 600 + (60 * row_idx)
            from_left = (((WINDOW_WIDTH - len(row_one) * 30)) / (len(row_one) + 1)) * (i + 1) + (i * 30)    # use row_one length to ensure consistent spacing
            if row == row_three:
                from_left += (WINDOW_WIDTH - 324) / 2    # center bottom row of keys

            pygame.draw.rect(screen, letter_colors[row[i]], pygame.Rect(from_left, from_top, 30, 40), border_radius=3)
            letter_locations[row[i]] = (from_left, from_top)

            text = font.render(row[i], True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (from_left + 15, from_top + 20)
            screen.blit(text, textRect)
    
        row_idx += 1
    # enter
    font = pygame.font.Font('freesansbold.ttf', 20)
    pygame.draw.rect(screen, letter_colors["enter"], pygame.Rect((((WINDOW_WIDTH - len(row_one) * 30)) / (len(row_one) + 1)), from_top, 75, 40), border_radius=3)
    letter_locations["enter"] = ((((WINDOW_WIDTH - len(row_one) * 30)) / (len(row_one) + 1)), from_top)
    text = font.render("ENTER", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = ((((WINDOW_WIDTH - len(row_one) * 30)) / (len(row_one) + 1)) + 37.5, from_top + 20)
    screen.blit(text, textRect)

    # backspace
    pygame.draw.rect(screen, letter_colors["backspace"], pygame.Rect(from_left + 45, from_top, 75, 40), border_radius=3)
    letter_locations["backspace"] = (from_left + 45, from_top)
    text = font.render("BACK", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (from_left + 45 + 37.5, from_top + 20)
    screen.blit(text, textRect)
    

def main():
    # Initialize screen
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Wordle in German!')

    # Fill background
    screen.fill(BACKGROUND)

    current_word = "" 
    current_guess_idx = 0
    # Event loop
    while True:

        # clock.tick(75)
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[1] >= 600 and pos[1] <= 640:
                    for letter in row_one:
                        if (pygame.Rect(letter_locations[letter][0], letter_locations[letter][1], 30, 40).collidepoint(pos[0], pos[1])):
                            if len(current_word) < 5:
                                current_word += letter
                                letter_colors[letter] = WHITE
                elif pos[1] >= 660 and pos[1] <= 700:
                    for letter in row_two:
                        if (pygame.Rect(letter_locations[letter][0], letter_locations[letter][1], 30, 40).collidepoint(pos[0], pos[1])):
                            if len(current_word) < 5:
                                current_word += letter
                                letter_colors[letter] = WHITE
                elif pos[1] >= 720 and pos[1] <= 760:
                    for letter in row_three:
                        if (pygame.Rect(letter_locations[letter][0], letter_locations[letter][1], 30, 40).collidepoint(pos[0], pos[1])):
                            if len(current_word) < 5:        
                                current_word += letter
                                letter_colors[letter] = WHITE
            # if event.type == pygame.KEYDOWN:

        
        if current_word:
            if current_guess_idx >= len(list_of_guesses):
                list_of_guesses.append(current_word)
            else:
                list_of_guesses[current_guess_idx] = current_word
                

        screen.fill(BACKGROUND)
        draw_boxes(screen, current_word, current_guess_idx)
        draw_keyboard(screen)
        pygame.display.update()

if __name__ == '__main__': main()
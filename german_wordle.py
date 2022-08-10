from ast import Pass
from tkinter import FALSE
import pygame
from pygame.locals import *

WINDOW_HEIGHT, WINDOW_WIDTH = 800, 500
BACKGROUND = (144, 238, 144)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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

box_colors = {i:[GRAY for j in range(5)] for i in range(6)}
def draw_boxes(screen, box_colors):
    
    for i in range(6):
        from_top = (i * 60) + ((i + 1) * 30)   # equal spacing between boxes
        for j in range(5):
            from_left = ((WINDOW_WIDTH - 300) / 6)* (j + 1) + (j * 60)  # equal spacing between boxes
            pygame.draw.rect(screen, box_colors[i][j], pygame.Rect(from_left, from_top, 60, 60), border_radius=3)

def draw_current_word(screen, current_word, current_guess_idx):
    font = pygame.font.Font('freesansbold.ttf', 32)
    from_top = (current_guess_idx * 60) + ((current_guess_idx + 1) * 30) 
    for i in range(len(current_word)):
        from_left = ((WINDOW_WIDTH - 300) / 6) * (i + 1) + (i * 60)
    
        write_text(screen, current_word[i], 32, from_left + 30, from_top + 30)

def draw_past_guesses(screen, list_of_guesses):
    font = pygame.font.Font('freesansbold.ttf', 32)
    for i in range(len(list_of_guesses) - 1):
        from_top = (i * 60) + ((i + 1) * 30) 
        for j in range(5):
            from_left = ((WINDOW_WIDTH - 300) / 6) * (j + 1) + (j * 60)
    
            write_text(screen, list_of_guesses[i][j], 32, from_left + 30, from_top + 30)

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

            write_text(screen, row[i], 26, from_left + 15, from_top + 20)
    
        row_idx += 1
    # enter
    font = pygame.font.Font('freesansbold.ttf', 20)
    pygame.draw.rect(screen, letter_colors["enter"], pygame.Rect((((WINDOW_WIDTH - len(row_one) * 30)) / (len(row_one) + 1)), from_top, 75, 40), border_radius=3)
    letter_locations["enter"] = ((((WINDOW_WIDTH - len(row_one) * 30)) / (len(row_one) + 1)), from_top)
    write_text(screen, "ENTER", 20, (((WINDOW_WIDTH - len(row_one) * 30)) / (len(row_one) + 1)) + 37.5, from_top + 20)

    # backspace
    pygame.draw.rect(screen, letter_colors["backspace"], pygame.Rect(from_left + 45, from_top, 75, 40), border_radius=3)
    letter_locations["backspace"] = (from_left + 45, from_top)
    write_text(screen, "BACK", 20, from_left + 45 + 37.5, from_top + 20)

    
def check_word(word_to_guess, current_guess, current_guess_idx, box_colors, keyboard_colors):
    for i in range(5):
        if word_to_guess[i] == current_guess.lower()[i]:
            box_colors[current_guess_idx][i] = GREEN
            keyboard_colors[current_guess[i]] = GREEN
        elif current_guess.lower()[i] in word_to_guess:
            box_colors[current_guess_idx][i] = YELLOW
            keyboard_colors[current_guess[i]] = YELLOW
        else:
            keyboard_colors[current_guess[i]] = BLACK

def write_text(screen, message, font_size, x_center, y_center):
    font = pygame.font.Font('freesansbold.ttf', font_size)

    text = font.render(message, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (x_center, y_center)
    screen.blit(text, textRect)

def end_of_game(screen, win, word):
    message_width = WINDOW_WIDTH - 100
    message_height = 300
    pygame.draw.rect(screen, WHITE, pygame.Rect(50, 50, message_width, message_height), border_radius=3)
    
    font = pygame.font.Font('freesansbold.ttf', 30)
    if win:
        text = "Congrats, you win!"
    else:
        text = "Sorry, you lose!"

    write_text(screen, text, 30, WINDOW_WIDTH // 2, 350 // 2)
    write_text(screen, "The correct word is " + word + "!", 30, WINDOW_WIDTH // 2, 350 // 2 + 40)

    block_width = message_width - 50 - (message_width // 2) - 10
    pygame.draw.rect(screen, GREEN, pygame.Rect(50 + (message_width // 2) - block_width,  250, block_width, 50), border_radius=3)
    pygame.draw.rect(screen, RED, pygame.Rect(50 + (message_width // 2) + 10, 250, block_width, 50), border_radius=3)

    write_text(screen, "PLAY AGAIN!", 20, 50 + (message_width // 2) - (block_width / 2), 275)
    write_text(screen, "END GAME!", 20, 50 + (message_width // 2) + (block_width // 2) + 10, 275)
    
        
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

    word_to_guess = "hello"
    game_on = True
    game_over = False
    win = False
    # Event loop
    while game_on:
        pos = [0, 0]
        # clock.tick(75)
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[1] >= 600 and pos[1] <= 640:
                    for letter in row_one:
                        if pygame.Rect(letter_locations[letter][0], letter_locations[letter][1], 30, 40).collidepoint(pos[0], pos[1]):
                            if len(current_word) < 5:
                                current_word += letter
                                letter_colors[letter] = WHITE
                elif pos[1] >= 660 and pos[1] <= 700:
                    for letter in row_two:
                        if pygame.Rect(letter_locations[letter][0], letter_locations[letter][1], 30, 40).collidepoint(pos[0], pos[1]):
                            if len(current_word) < 5:
                                current_word += letter
                                letter_colors[letter] = WHITE
                elif pos[1] >= 720 and pos[1] <= 760:
                    if (pygame.Rect(letter_locations["backspace"][0], letter_locations["backspace"][1], 75, 40).collidepoint(pos[0], pos[1])) and current_word:
                        removed_letter = current_word[-1]
                        current_word = current_word[:-1]
                        if current_word.count(removed_letter) == 0:
                            letter_colors[removed_letter] = GRAY
                    elif (pygame.Rect(letter_locations["enter"][0], letter_locations["enter"][1], 75, 40).collidepoint(pos[0], pos[1])) and (len(current_word) == 5):
                        check_word(word_to_guess, current_word, current_guess_idx, box_colors, letter_colors)
                        if current_word.lower() == word_to_guess:
                            win = True
                            game_over = True
                        elif current_guess_idx == 5:
                            game_over = True
                        else:
                            current_word = ""
                            current_guess_idx += 1
                    else:
                        for letter in row_three:
                            if pygame.Rect(letter_locations[letter][0], letter_locations[letter][1], 30, 40).collidepoint(pos[0], pos[1]):
                                if len(current_word) < 5:        
                                    current_word += letter
                                    letter_colors[letter] = WHITE
                elif game_over:
                    message_width = WINDOW_WIDTH - 100
                    block_width = message_width - 50 - (message_width // 2) - 10
                    if (pygame.Rect(50 + (message_width // 2) - block_width,  250, block_width, 50).collidepoint(pos[0], pos[1])):
                        while current_guess_idx >= 0:
                            for i in range(5):
                                box_colors[current_guess_idx][i] = GRAY
                            current_guess_idx -= 1
                        current_guess_idx = 0

                        for key in letter_colors.keys():
                            letter_colors[key] = GRAY
                        current_word = ""

                        while len(list_of_guesses) > 0:
                            list_of_guesses.pop()

                        game_over = False

                    elif (pygame.Rect(50 + (message_width // 2) + 10, 250, block_width, 50).collidepoint(pos[0], pos[1])):
                        game_on = False

        
        
        if current_guess_idx >= len(list_of_guesses):
            list_of_guesses.append(current_word)
        else:
            list_of_guesses[current_guess_idx] = current_word
                
        if not game_over:
            screen.fill(BACKGROUND)
            draw_boxes(screen, box_colors)
            if len(list_of_guesses) > 1:
                draw_past_guesses(screen, list_of_guesses)
            draw_current_word(screen, current_word, current_guess_idx)
            draw_keyboard(screen)
        else:
            end_of_game(screen, win, word_to_guess)

        pygame.display.update()


if __name__ == '__main__': main()
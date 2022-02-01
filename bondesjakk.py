from __future__ import annotations

import pygame

from enum import Enum, auto


class Player(Enum):
    NONE = auto()
    CROSS = auto()
    CIRCLE = auto()


def check_for_win():
    # Straight wins
    for i in range(3):
        win_row = True
        win_col = True

        player_row = board[i][0]
        player_col = board[0][i]
        
        if player_row is Player.NONE:
            win_row = False
        else:
            for col in range(1, 3):
                if board[i][col] is not player_row:
                    win_row = False
                    break

        if player_col is Player.NONE:
            win_col = False
        else:
            for row in range(1, 3):
                if board[row][i] is not player_col:
                    win_col = False
                    break
            
        if win_row or win_col:
            return True

    # Diaginal from top left win
    win_diag_top = True
    player_diag_top = board[0][0]

    for i in range(1,3):
        if board[i][i] is not player_diag_top:
            win_diag_top = False
            break
        
    if player_diag_top is Player.NONE:
        win_diag_top = False
    
    if win_diag_top:
        return True

    # Diagonal from bottom left win
    win_diag_bottom = True
    player_diag_bottom = board[2][0]

    for i in range(1,3):
        if board[2-i][i] is not player_diag_bottom:
            win_diag_bottom = False
            break
        
    if player_diag_bottom is Player.NONE:
        win_diag_bottom = False
    
    if win_diag_bottom:
        return True

    return False


def reset_game():
    global game_over
    game_over = False
    
    for row in range(3):
        for col in range(3):
            board[row][col] = Player.NONE


def full_board():
    for row in range(3):
        for col in range(3):
            if board[row][col] is Player.NONE:
                return False
    return True


def draw_board():
    window.fill(background_color)
    
    # Draw borders
    half_border_thickness = border_thickness * 0.5
    
    for i in range(2):
        
        x = cell_width * (i + 1) - half_border_thickness
        pygame.draw.rect(window, border_color, (x, 0, border_thickness, height))
        
        y = cell_height * (i + 1) - half_border_thickness
        pygame.draw.rect(window, border_color, (0, y, width, border_thickness))
    
    mark_width = cell_width * 0.9
    mark_height = cell_height * 0.9

    # Draw marks
    for row in range(3):
        for col in range(3):
            cell_content = board[row][col]

            pos_x = cell_width * col + cell_width * 0.5 - mark_width * 0.5
            pos_y = cell_height * row + cell_height * 0.5 - mark_height * 0.5
            
            if cell_content is Player.CROSS:
                img_cross_scaled = pygame.transform.scale(img_cross, (mark_width, mark_height))
                window.blit(img_cross_scaled, (pos_x, pos_y))
            elif cell_content is Player.CIRCLE:
                img_circle_scaled = pygame.transform.scale(img_circle, (mark_width, mark_height))
                window.blit(img_circle_scaled, (pos_x, pos_y))

    pygame.display.flip()


width = 500
height = 500

cell_width = width / 3
cell_height = height / 3

border_thickness = 5

background_color = (255, 88, 89)
border_color = (0, 0, 0)

board = [
    [Player.NONE,   Player.NONE,    Player.NONE],
    [Player.NONE,   Player.NONE,    Player.NONE],
    [Player.NONE,   Player.NONE,    Player.NONE]
]

turn = Player.CROSS

game_over = False

app_running = True

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bondesjakk')

img_cross = pygame.image.load("resources/cross.png")
img_circle = pygame.image.load("resources/circle.png")

# Main game loop
while app_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
            break
        
        # Game logic
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_over:
                    reset_game()

        # Any mouse button pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse button 1 pressed
            if event.button == 1:
                if not game_over:
                    mouse_pos = pygame.mouse.get_pos()

                    row = int(mouse_pos[1] // cell_width)
                    col = int(mouse_pos[0] // cell_height)
                    
                    # Validate selection
                    if board[row][col] is Player.NONE:
                        if turn is Player.CROSS:
                            board[row][col] = Player.CROSS
                            turn = Player.CIRCLE
                        elif turn is Player.CIRCLE:
                            board[row][col] = Player.CIRCLE
                            turn = Player.CROSS

                        if check_for_win():
                            game_over = True
                            print("Tre på rad!")
                            
                        elif full_board():
                            game_over = True
                else:
                    print("Trykk escape for å spille igjen!")

    # Exit early if the app should shut down
    if not app_running:
        break

    draw_board()

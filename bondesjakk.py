import pygame


# Constants
width = 500
height = 500

border_thickness = 5

background_color = (255, 88, 89)
border_color = (0, 0, 0)


pygame.init()
window = pygame.display.set_mode((width, height))

board = [
    [1,0,0],
    [0,0,0],
    [0,0,0]
]

app_running = True


# Main game loop
while app_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        
        # Game logic
        elif event.type == pygame.KEYDOWN:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

    # Exit early if the app should shut down
    if not app_running:
        break

    # Draw
    window.fill(background_color)

    # Draw borders
    cell_width = width / 3
    cell_height = height / 3
    
    for i in range(2):
        half_border_thickness = border_thickness * 0.5
        
        x = cell_width * (i + 1) - half_border_thickness
        pygame.draw.rect(window, border_color, (x, 0, border_thickness, height))
        
        y = cell_height * (i + 1) - half_border_thickness
        pygame.draw.rect(window, border_color, (0, y, width, border_thickness))
    
    # Draw marks
    for row in range(3):
        for col in range(3):
            state = board[row, col]

    pygame.display.flip()

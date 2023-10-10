import pygame

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Lets draw')
clock = pygame.time.Clock()

drawing = False
erasing = False
last_pos = None


button_width = 100
button_height = 40
button_x = 700
button_y = 10
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)


pen_width = 20  
erase_width = 3  

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    erasing = not erasing
                else:
                    drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                last_pos = None

        if drawing:
            current_pos = pygame.mouse.get_pos()
            if last_pos:
                if erasing:
                    color = WHITE
                    width = erase_width
                else:
                    color = BLACK
                    width = pen_width
                pygame.draw.line(screen, color, last_pos, current_pos, width)
            last_pos = current_pos

        
        pygame.draw.rect(screen, RED if not erasing else GREEN, button_rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render('Erase', True, WHITE)
        screen.blit(text, (button_x + 20, button_y + 10))

        pygame.display.flip()
        clock.tick(60)
except SystemExit:
    pass








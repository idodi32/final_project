import pygame
from pygame_function import Init_pygame, Button, Text, Text_input

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

WIDTH, HEIGHT, name = 800, 600, "log in"
start = Init_pygame(blue, WIDTH, HEIGHT, name)
screen = start.get_screen()

text_col = white
title_font = pygame.font.SysFont("arielblack", 70)
font = pygame.font.SysFont("arielblack", 44)
title = Text("log in", title_font, text_col, 300, 50, screen)
username = Text("username", font, text_col, 275, 150, screen)
username_input = Text_input(250, 225, 200, 50, black, white)
password = Text("password", font, text_col, 275, 325, screen)
password_input = Text_input(250, 400, 200, 50, black, white)
approval = Button(275, 500, 200, 50, "approval", white, black, None)

title.draw_text(screen)
username.draw_text(screen)
username_input.draw(screen)
password.draw_text(screen)
password_input.draw(screen)

running = True
approval_flag = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if approval.rect.collidepoint(event.pos):
                approval_flag = True

        username_input.handle_key_event(event)
        password_input.handle_key_event(event)

    approval.is_hovered = approval.rect.collidepoint(pygame.mouse.get_pos())

    approval.draw(screen)
    if approval_flag:
        break

    username_input.draw(screen)
    if username_input.get_quit():
        break

    password_input.draw(screen)
    if password_input.get_quit():
        break

    pygame.display.update()

if approval_flag:
    username_client = username_input.get_text()
    password_client = password_input.get_text()
    import main_menu
pygame.quit()

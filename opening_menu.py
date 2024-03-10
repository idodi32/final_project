import pygame
from pygame_function import Init_pygame, Button, Text

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

WIDTH, HEIGHT, name = 800, 600, "openning menu"
start = Init_pygame(blue, WIDTH, HEIGHT, name)
screen = start.get_screen()

text_col = white
font = pygame.font.SysFont("arielblack", 70)
title = Text("Isnake", font, text_col, 325, 100, screen)
title.draw_text(screen)
sign_up_Button = Button(100, 500, 100, 50, "sign up", white, black, "on_button_click")
log_in_Button = Button(600, 500, 100, 50, "log in", white, black, "on_button_click")
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        sign_up_flag = sign_up_Button.handle_event(event)
        log_in_flag = log_in_Button.handle_event(event)
    sign_up_Button.draw(screen)
    log_in_Button.draw(screen)
    pygame.display.update()
    if sign_up_flag:
        break
    if log_in_flag:
        break
if sign_up_flag:
    import sign_up
if log_in_flag:
    import log_in
pygame.quit()

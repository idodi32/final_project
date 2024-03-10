import pygame
from pygame_function import Init_pygame, Button, Text, Text_input
import data_player

def check_re_password(Text_input1, Text_input2):
    return Text_input1 == Text_input2

def check_password(Text_input1):
    remark = ""
    if len(Text_input1) < 8:
        remark += "You have not at least 8 chars\n"

    if not any(c.isupper() for c in Text_input1) or not any(c.islower() for c in Text_input1):
        remark += "You have not both uppercase and lowercase letters\n"

    if not any(c.isdigit() for c in Text_input1):
        remark += "You have not at least one digit\n"

    special_characters = re.compile('[@_!#$%^&*()<>?/|\}{~:]')
    if not special_characters.search(Text_input1):
        remark += "You have not at least one special character"
    return remark

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
Red = (255, 0, 0)

WIDTH, HEIGHT, name = 800, 600, "sign up"
start = Init_pygame(blue, WIDTH, HEIGHT, name)
screen = start.get_screen()

text_col = white
font = pygame.font.SysFont("arielblack", 70)
font_remark = pygame.font.SysFont("arielblack", 16)
title = Text("sign up", font, text_col, 300, 50, screen)
username = Text("username", font, text_col, 275, 125, screen)
username_input = Text_input(250, 175, 200, 50, black, white)
password = Text("password", font, text_col, 275, 250, screen)
password_input = Text_input(250, 300, 200, 50, black, white)
re_password = Text("re password", font, text_col, 275, 375, screen)
re_password_input = Text_input(250, 425, 200, 50, black, white)
approval = Button(275, 500, 200, 50, "approval", white, black, None)
title.draw_text(screen)
username.draw_text(screen)
username_input.draw(screen)
password.draw_text(screen)
password_input.draw(screen)
re_password.draw_text(screen)
re_password_input.draw(screen)


running = True
remark = ""
approval_clicked = False  # Flag to track if the approval button is clicked

while running and remark == "":
    approval.draw(screen)
    username_input.input_place(screen)
    if username_input.get_quit():
        break
    password_input.input_place(screen)
    if password_input.get_quit():
        break
    re_password_input.input_place(screen)
    if password_input.get_text():
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and approval.rect.collidepoint(event.pos):
            approval_clicked = True

    if approval_clicked:
        if not check_re_password(password_input.get_text(), re_password_input.get_text()):
            remark = "The password and the re password are not the same"
        else:
            remark = check_password(password_input.get_text())
            if remark == "":
                data = data_player(username_input.text, password_input.get_text())  # This line is commented as 'data_player' is not used in this code
                import log_in
                pygame.quit()
                exit()
            else:
                remarks = Text(remark, font_remark, Red, 30, 550, screen)
                remarks.draw_text(screen)
                remark = ""
                username_input.init_text()
                password_input.init_text()
                approval_clicked = False  # Reset the approval button flag



    pygame.display.update()


pygame.quit()

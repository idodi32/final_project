import socket
import pygame
from pygame_function import Init_pygame, Button, Text


def connect_server(IP,port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, port))
    message = "Hello, server!"
    client_socket.send(message.encode())
    echoed_message = client_socket.recv(1024)
    print(f"Received from server: {echoed_message.decode()}")
    client_socket.close()


white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

WIDTH, HEIGHT, name = 800, 600, "main menu"
start = Init_pygame(blue, WIDTH, HEIGHT, name)
screen = start.get_screen()
text_col = white
font = pygame.font.SysFont("arielblack", 70)
title = Text("Isnake", font, text_col, 325, 100, screen)
title.draw_text(screen)
play_Button = Button(350, 300, 100, 50, "play", white, black, "on_button_click")
stats_Button = Button(350, 400, 100, 50, "stats", white, black, "on_button_click")
running, play_Button_flag, stats_Button_flag = True, False, False

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        play_Button_flag = play_Button.handle_event(event)
        stats_Button_flag = stats_Button.handle_event(event)
    play_Button.draw(screen)
    stats_Button.draw(screen)
    pygame.display.update()
    if play_Button_flag:
        break
    if stats_Button_flag:
        break
if play_Button_flag:
    connect_server("127.0.0.1",12345)
if stats_Button_flag:
    print("stats")
pygame.quit()

import pygame


class Init_pygame:
    def __init__(self, color, WIDTH, HEIGHT, name):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(color)
        pygame.display.set_caption(name)

    def get_screen(self):
        return self.screen


class Text:
    def __init__(self, text, font, text_col, x, y, screen):
        self.font = font
        self.text = text
        self.text_col = text_col
        self.x = x
        self.y = y

    def draw_text(self, screen):
        img = self.font.render(self.text, True, self.text_col)
        screen.blit(img, (self.x, self.y))


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color,action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.action = action
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        if self.is_hovered:
            color = self.hover_color
        else:
            color = self.color
        pygame.draw.rect(screen, color, self.rect)

        text_surface = self.font.render(self.text, True, self.hover_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered and self.action:
                return True
        return False


class Text_input:
    def __init__(self, x, y, width, height, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 36)
        self.quit = False

    def get_quit(self):
        return self.quit

    def get_text(self):
        return self.text

    def handle_text(self, char):
        self.text += char

    def init_text(self):
        self.text = ""

    def handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                return False
            else:
                self.handle_text(event.unicode)
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.hover_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def input_place(self, screen):
        clock = pygame.time.Clock()
        flag = True
        while (not self.quit) and flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                flag = self.handle_key_event(event)
            self.draw(screen)
            pygame.display.flip()
            clock.tick(30)

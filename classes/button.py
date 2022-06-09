import pygame

class Button:
    def __init__(self, pos_x, pos_y, light_shader, dark_shader, font, text):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.light_shader = light_shader
        self.dark_shader = dark_shader
        self.font = font
        self.text = self.font.render(text, True, (255, 255, 255))

    def draw(self, win, mouse_on_top: bool):
        if mouse_on_top:
            pygame.draw.rect(win, self.light_shader, (self.pos_x, self.pos_y, 140, 40))
        else:
            pygame.draw.rect(win, self.dark_shader, (self.pos_x, self.pos_y, 140, 40))


        win.blit(self.text, (self.pos_x + 10, self.pos_y + 10))
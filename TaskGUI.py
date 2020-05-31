import pygame
from constants import *

class TaskGUI:
    font = None

    def __init__(self, task, x=0, y=0, width=400, height=200):
        if not self.__class__.font:
            self.__class__.font = pygame.font.Font(FONT_FILE, FONT_SIZE)

        task.set_gui(self)
        self.task = task

        self.width = width
        self.height = height
        self.progress_width = 0

        self.image = pygame.Surface((self.width, self.height,))
        self.rect = self.image.get_rect()

        self.set_pos(x, y)
        self.render_text()

    def update(self, time_since):
        self.progress_width = self.width * sorted((0, self.task.percent_complete(), 1))[1]
        self.render_text()

    def draw(self, screen):
        self.image.fill(GRAY)
        self.image.fill(RED, rect=((0, 1,),(self.progress_width, self.height-2)))
        screen.blit(self.image, self.rect)
        screen.blit(self.text_image, self.text_rect)

    def set_pos(self, x, y):
        self.pos = { 'x':x, 'y':y }
        self.rect.center = (self.pos["x"]+(self.width/2), self.pos["y"]+(self.height/2))

    def render_text(self):
        self.text = "{}: {:.2f}%".format(self.task.name, sorted((0, self.task.percent_complete(), 1))[1] * 100)
        self.text_image = self.__class__.font.render(self.text, True, BLACK)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.rect.center

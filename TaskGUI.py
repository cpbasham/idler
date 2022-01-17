import pygame
from Task import *
from constants import *


class TaskGUIPane:
    def __init__(self, taskGUIList=[], *, x=0, y=0, width=400, height=200):
        self.taskGUIs = taskGUIList

        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height,))
        self.rect = self.image.get_rect()

        self.set_pos(x, y)
        self.render_text()

    def add_taskgui(self, taskgui):
        self.taskGUIs.append(taskgui)

    def draw(self, screen):
        for tgui in self.taskGUIs:
            #tgui.draw(screen)
            tgui.draw(self.image)
        screen.blit(self.image, self.rect)

    def update(self, time_since):
        for tgui in self.taskGUIs:
            tgui.update(time_since)

    def set_pos(self, x, y):
        self.pos = { 'x':x, 'y':y }
        self.rect.center = (x+(self.width/2), y+(self.height/2))

    def render_text(self):
        for tgui in self.taskGUIs:
            tgui.render_text()


class TaskGUI:
    font = None

    def __init__(self, task, x=0, y=0, width=400, height=50):
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
        self.task.update(time_since)
        self.progress_width = self.width * sorted((0, self.task.percent_complete(), 1))[1]
        self.render_text()

    def draw(self, screen):
        self.image.fill(GRAY)
        self.image.fill(RED, rect=((0, 1,),(self.progress_width, self.height-2)))
        screen.blit(self.image, self.rect)
        screen.blit(self.text_image, self.text_rect)

    def set_pos(self, x, y):
        self.pos = { 'x':x, 'y':y }
        self.rect.center = (x+(self.width/2), y+(self.height/2))

    def render_text(self):
        self.text = "{}: {:.2f}%".format(self.task.name, sorted((0, self.task.percent_complete(), 1))[1] * 100)
        self.text_image = self.__class__.font.render(self.text, True, BLACK)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.rect.center

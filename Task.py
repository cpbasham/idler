import pygame
from constants import *

class Task:
    """
    This class represents a named task,
    which is fulfilled by reaching done_units.
    It does not implement a way to progress,
    it only holds state & updates an optional GUI.
    """

    def __init__(self, name, done_units, start_units=0):
        super().__init__()
        self.name = name
        self.done_units = done_units
        self.current_units = start_units
        self.gui = None

    def set_gui(self, gui):
        self.gui = gui

    def draw(self, *args):
        if self.gui:
            self.gui.draw(*args)

    def update(self, *args):
        if self.gui:
            self.gui.update(*args)

    def is_complete(self):
        return self.current_units >= self.done_units
    
    def percent_complete(self):
        return self.current_units / self.done_units

    def _complete(self):
        print("{} '{}' Complete!".format(self.__class__.__name__, self.name))


class TimedTask(Task):
    """
    This class represents a named task that takes a certain amount of time to complete.
    """

    def __init__(self, name, max_seconds, start_seconds=0):
        super().__init__(name, max_seconds, start_seconds)

    def update(self, time_since):
        previously_completed = self.is_complete()
        self.current_units += (time_since/1000)
        if not previously_completed and self.is_complete():
            self._complete()
        # Updates GUI, so should occur after our class's update logic.
        super().update(time_since)


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

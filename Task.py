import pygame
from constants import *

class Task:
    """
    This class represents a named task,
    which is fulfilled when 'current_units' reaches 'done_units'.
    It does not implement a way to progress,
    it only holds state & updates an optional GUI.
    """
    TASK_COMPLETE = pygame.event.Event(pygame.USEREVENT + 0)

    def __init__(self, name, done_units, start_units=0):
        super().__init__()
        self.name = name
        self.done_units = done_units
        self.current_units = start_units
        self.gui = None

    # Purely for the GUI's benefit. Task should otherwise not do stuff to the GUI
    def set_gui(self, gui):
        self.gui = gui

    def update(self, *args):
        pass

    def is_complete(self):
        return self.current_units >= self.done_units

    def percent_complete(self):
        return self.current_units / self.done_units

    def _complete(self):
        print("{} '{}' Complete!".format(self.__class__.__name__, self.name))
        pygame.event.post(self.__class__.TASK_COMPLETE)
        #print(self.__class__.EVENT)


class TimedTask(Task):
    """
    Represents a named task that takes a certain amount of time to complete.
    """

    def __init__(self, name, max_seconds, start_seconds=0):
        super().__init__(name, max_seconds, start_seconds)

    def update(self, time_since):
        previously_completed = self.is_complete()
        self.current_units += (time_since/1000)
        if not previously_completed and self.is_complete():
            self._complete()
        super().update(time_since)

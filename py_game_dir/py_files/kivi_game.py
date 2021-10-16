import kivy
import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import _ctypes
import ctypes

import pygame
from pygame import rect
import numpy as np

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding = 10)
        colors = [red, green, blue, purple]

        pygame.init()

        screen = pygame.display.set_mode((100, 400))
        screen.fill((0,0,255))
        pygame.display.flip()

        return layout



if __name__ == '__main__':
    app = HBoxLayoutExample()
    app.run()
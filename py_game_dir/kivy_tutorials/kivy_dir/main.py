import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.core.window import Window

from random import randint

class ActGame(Widget):
    pass

class DirApp(App):
    def build(self):
        scrn_obj = ActGame()
        return scrn_obj

def main():
    run_app = DirApp()
    run_app.run()

if __name__ == '__main__':
    main()
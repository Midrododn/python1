import kivy
import random

from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class MainApp(App):
    def build(self):
        label = Label(text = 'Hello from Kivy',
                        size_hint = (.5, .5),
                        pos_hint = {'center_x': .5, 'center_y': .98})
        img = Image(source = '/home/lock/Documents/pydir/py_game_dir/media_res/phone_icon.png',
                    pos_hint = {'center_x':.5, 'center_y':.4})
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)
        #return label
        #return img
        return button
    
    def on_press_button(self, instance):
        print('You pressed the button!')

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding = 10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text = "Button #%s" % (i + 1),
                        background_color = random.choice(colors)
                        )
            layout.add_widget(btn)
        return layout

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
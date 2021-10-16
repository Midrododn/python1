from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.core.window import Window

from random import randint

class FallBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    acc = 1
    air_friction = 0.1

    def move(self, height, width):
        self.velocity_x -= self.acc
        self.x += self.velocity_x
        if (self.velocity_y < 0):
            self.velocity_y += self.air_friction
        elif (self.velocity_y > 0):
            self.velocity_y -= self.air_friction
        if abs(self.velocity_y) < 0.5:
            self.velocity_y = 0
        self.y += self.velocity_y

        if (self.x <= 10):
            if (self.velocity_x <= -3):
                self.velocity_x *= -1
                self.velocity_x -= 2
                self.x = 10
            else:
                self.velocity_x = 0
                self.x = 10
                self.acc = 0
        # bounce off top
        if (self.x >= width - 50):
            self.velocity_x *= 0
            self.x = 0
            self.acc = 0
        # bounce off left and right
        if (self.y < 0):
            self.velocity_y *= -1
            self.y = 0
        if (self.y > height - 20):
            self.velocity_y *= -1 
            self.y = height -20

class PongGame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center

    def update(self, dt):
        self.ball.move(self.height, self.width)

    def on_touch_down(self, touch):
        if (touch.x >= self.width - 150):
            if touch.y <= 100:
                self.ball.velocity_y = -20
            elif (touch.y >= self.height - 100):
                self.ball.velocity_y = 20
            elif (self.ball.velocity_x == 0)and(self.ball.x == 10):
                self.ball.velocity_x = 30
                self.ball.acc = 1

class FfallApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    FfallApp().run()



#vis_proj

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.core.window import Window

from random import randint


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    acc = 1
    air_friction = 0.05

    def move(self, height, width):
        self.velocity_y -= self.acc
        self.y += self.velocity_y
        if (self.velocity_x < 0):
            self.velocity_x += self.air_friction
        elif (self.velocity_x > 0):
            self.velocity_x -= self.air_friction
        if abs(self.velocity_x) < 0.5:
            self.velocity_x = 0
        self.x += self.velocity_x
        #self.pos = Vector(*self.velocity) + self.pos
        # bounce off bottom
        if (self.y <= 10):
            if (self.velocity_y <= -3):
                self.velocity_y *= -1
                self.velocity_y -= 2
                self.y = 10
            else:
                self.velocity_y = 0
                self.y = 10
                self.acc = 0
        # bounce off top
        if (self.top >= height - 50):
            self.velocity_y *= 0
            self.y = 0
            self.acc = 0

        # bounce off left and right
        if (self.x < 0):
            self.velocity_x *= -1
            self.x = 0
        if (self.x > width - 20):
            self.velocity_x *= -1
            self.x = width -20


class PongGame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.y = randint(-7,7)
        #self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move(self.height, self.width)

    def on_touch_down(self, touch):
        if touch.y >= self.height - 50:
            if self.ball.velocity_y == 0:
                self.ball.velocity_y = 30
                self.ball.acc = 1
        if ((touch.y < self.height - 50) and (touch.y >= self.height -150)):
            if (touch.x <= 100):
                self.ball.velocity_x = -20
            if (touch.x >= self.width - 100):
                self.ball.velocity_x = 20

class FallApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    #Window.fullscreen = True  or 'auto'
    FallApp().run()

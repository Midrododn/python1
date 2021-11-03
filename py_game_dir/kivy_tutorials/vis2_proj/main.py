#vis2_proj

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.graphics import *

from kivy.core.window import Window

from random import randint
import numpy as np

fall_clr = (0.5, 0., 0.5)


class BigRect(Widget):

    def __init__(self):
        self.pos_x = 50
        self.pos_y = 50
        self.posxy = {0,10}
        self.size_x = 100
        self.size_y = 100

    def draw_inst(self, status = "new"):
        if (status == "new"):
            pass
        Color(1.,1.,1.)
        Rectangle(pos=(self.pos_x, self.pos_y), size=(self.size_x, self.size_y))



class BulletTtry1(Widget):

    def __init__(self, dem_x, dem_y, iname):
        self.ax = 0
        self.ay = 0
        self.pos_x = 10 + dem_x
        self.pos_y = 100 + dem_y
        self.rgb_color = (0.5,0,0.5)
        self.inst_name = iname

    def change_acc(self, accx , accy ):
        self.ax += accx
        self.ay += accy
        self.pos_x += self.ax
        self.pos_y += self.ay

    def draw_inst(self):
        Color(0.5,0,0.5)
        Rectangle(pos=(self.pos_x, self.pos_y), size=(5, 5))

    def rubber(self):
        Color(0.,0.,0.)
        Rectangle(pos=(self.pos_x, self.pos_y), size=(5, 5))

    def move_down(self, bord):
        low_y = bord[1]
        low_y = 10
        if(self.pos_y>low_y):
            self.pos_y -= 1
        else:
            self.pos_y = low_y


class Pong1Ball(Widget):
    pass


class PongGame(Widget):

    edges = BigRect()
    loc_fall_clr =  fall_clr

    ball = BulletTtry1(randint(-8,16),randint(-7,7),"ball")
    ball1 = BulletTtry1(randint(8,24),randint(-7,7),"1ball")
    ball2 = BulletTtry1(randint(16,32),randint(-7,7),"2ball")

    inst_list = []
    inst_list.append(ball)
    inst_list.append(ball1)
    inst_list.append(ball2)

    def serve_ball(self):
        for obj in self.inst_list:
            with self.canvas:
                obj.draw_inst()
    def  update(self, dt):
        self.edges.draw_inst()
        l_bord = np.array([self.width,self.height])
        for obj in self.inst_list:
            with self.canvas:
                obj.rubber()
                obj.move_down(l_bord)
                obj.draw_inst()
    def dummy_loop(self):
        for obj in self.inst_list:
            pass

class FallApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        game.cear_screen()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    print("begin")
    FallApp().run()

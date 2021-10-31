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

class DrawBlckRec(Widget):
    def __init__(self, x = 0, y = 0):
        self.lon_hig = Rectangle(pos=(self.x, self.y), size=(5, 5))


class borders(Widget):
    def __init__(self, ybottom = 0, xright = 0, ytop = 0):
        self.bottomy = ybottom
        self.rightx = xright
        self.topy = ytop
    def grub_args(self, ybottom = 0, xright = 0, ytop = 0):
        self.bottomy = ybottom
        self.rightx = xright
        self.topy = ytop
    def ifexist(self):
        print("exists")

class BulletTtry1(Widget):

    def __init__(self, dem_x, dem_y, iname):
        self.ax = 0
        self.ay = 0
        self.pos_x = 10 + dem_x
        self.pos_y = 100 + dem_y
        self.rgb_color = (0,0,1.)
        self.inst_name = iname

    def change_acc(self, accx , accy ):
        self.ax += accx
        self.ay += accy
        self.pos_x += self.ax
        self.pos_y += self.ay

    def draw_inst(self):
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

    edges = borders()
    #loc_fall_clr = (0.5, 0., 0.5)
    loc_fall_clr =  fall_clr

    ball = BulletTtry1(randint(-7,7),randint(-20,20),"ball")
    ball1 = BulletTtry1(randint(-7,7),randint(-7,7),"2ball")

    inst_list = []
    inst_list.append(ball)
    inst_list.append(ball1)

    def serve_ball(self):
        for obj in self.inst_list:
            with self.canvas:
                obj.draw_inst()
    def  update(self, dt):
        l_bord = np.array([self.width,self.height])
        for obj in self.inst_list:
            with self.canvas:
                obj.move_down(l_bord)
                obj.draw_inst()
    def dummy_loop(self):
        for obj in self.inst_list:
            pass

class FallApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    print("begin")
    FallApp().run()

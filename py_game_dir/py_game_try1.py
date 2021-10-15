# filename : py_game_try1.py

import pygame
import numpy as np
import time
from pygame import font
from pygame import color
from pygame import rect
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

color_dict = {
    "white":(255, 255, 255),
    "red":(255, 0, 0),
    "green":(0, 255, 0),
    "blue":(0, 0, 128),
    "black":(0, 0, 0),
}

class Bottom_surf(pygame.sprite.Sprite):
    def __init__(self, S_WIDTH = SCREEN_WIDTH, S_HEIGHT = SCREEN_HEIGHT):
        super(Bottom_surf, self).__init__()
        self.width = S_WIDTH
        self.heigh = S_HEIGHT - 40
        self.surf = pygame.Surface((self.width , 40))
        self.surf.fill(color_dict["white"])
        self.rect = self.surf.get_rect()

    def draw_instance(self):
        screen.blit(self.surf, (0 , self.heigh))
        

class Drop_rect(pygame.sprite.Sprite):
    def __init__(self):
        super(Drop_rect, self).__init__()
        self.width = 10
        self.height = 10
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(color_dict["red"])
        self.rect = self.surf.get_rect()
        self.count = 0

    def draw_instance(self):
        screen.blit(self.surf, self.rect)

    def update(self, pressed_keyes,S_BOTTOM = 600 - 40) -> None:
        #if pressed_keyes[K_DOWN]:
        #    self.rect.move_ip(0, 5)
        self.rect.move_ip(0, 5)
        
        if self.rect.bottom >= S_BOTTOM:
            self.rect.bottom = S_BOTTOM

class TXT_msg():
    static_lines = 0
    def __init__(self, c_dict = color_dict, S_WIDTH = SCREEN_WIDTH,
     msg = "> it would be length of the line ->"):
        self.txt_font = pygame.font.Font('freesansbold.ttf', 8)
        TXT_msg.static_lines += 1 
        self.c_dict = c_dict
        self.txt_string = msg
        self.txt_render = self.txt_font.render(self.txt_string, True, self.c_dict["green"],
         self.c_dict["blue"])
        self.push_right = S_WIDTH - self.txt_render.get_width()
        self.lits_position = TXT_msg.static_lines * self.txt_render.get_height()
    
    def prnt_msg(self, msg = "<TEXT TEXT"):
        if self.txt_string[0]==">":
            self.txt_string = str(msg)
        if msg[0]!= "<":
            self.txt_string = str(msg)
        self.txt_render = self.txt_font.render(self.txt_string, True, self.c_dict["green"],
         self.c_dict["blue"])
        txt_Rect = self.txt_render.get_rect()
        txt_Rect = (self.push_right , self.lits_position)
        screen.blit(self.txt_render, txt_Rect)

class Loop_Watch():
    static_prog_start = time.time()
    static_framerate_np = np.array([],dtype= np.float32)
    def __init__(self):
        self.start = time.time()
        self.finish = time.time()
        self.dt = 0.0
        self.max_dt = 0.0
        self.avr_dt = 0.0
        self.counter = 0

    def start_watch(self):
        self.start = time.time()

    def finish_watch(self):
        self.dt = time.time() - self.start
        if (self.counter == 5000 * 5):
            self.counter = 0
            self.max_dt = 0.0
        if (self.dt > self.max_dt):
            self.max_dt = self.dt
        self.finish = str(self.dt)

    def prnt_watch(self):
        self.finish_watch()
        self.avr_dt_np()
        time_stamp = "Last loop : " + str(self.dt)[:6] + "|avr dt = " + str(self.avr_dt)[:7]
        self.counter += 1
        return time_stamp
    
    def time_from_start(self):
        from_start =  time.time() - Loop_Watch.static_prog_start
        return from_start
    
    def prnt_from_start(self):
        txt = "Time from start : " + str(self.time_from_start())[:10]
        return txt

    def avr_dt_np(self):
        Loop_Watch.static_framerate_np = np.append(Loop_Watch.static_framerate_np, self.dt)
        tmp = np.shape(Loop_Watch.static_framerate_np)[0]
        tmp = np.sum(Loop_Watch.static_framerate_np) / tmp
        if (np.shape(Loop_Watch.static_framerate_np)[0] > 1000):
            Loop_Watch.static_framerate_np = np.array([],dtype= np.float32)
        self.avr_dt = tmp


def main():

    # FPS limitation    
    FPS = 60
    FramePerSec = pygame.time.Clock()

    block = Bottom_surf()
    drop = Drop_rect()
    time_obj = Loop_Watch()
    label1 = TXT_msg(msg = "Last loop : 0.0000|avr dt = 0.00000")
    label2 = TXT_msg(msg= "Time from start : 000.000")
    label3 = TXT_msg(msg= "FPS limitation = " +  str(FPS))

    all_sprites = pygame.sprite.Group()
    all_sprites.add(drop)
    all_sprites.add(block)

    running = True

    while running:
        time_obj.start_watch()
        #for event in pygame.event.get():
        #    if event.type == KEYDOWN:
        #        if event.key == K_ESCAPE:
        #            running = False
        #    elif event.type == QUIT:
        #        running = False

        pressed_keys = pygame.key.get_pressed()

        screen.fill((0,0,0))

        drop.update(pressed_keys)

        FramePerSec.tick(FPS)

        for entity in all_sprites:
            entity.draw_instance()

        # timer -------------------------------------
        time_str = time_obj.prnt_watch()
        time_obj.avr_dt_np()
        label1.prnt_msg(msg = time_str)
        label2.prnt_msg(time_obj.prnt_from_start())
        label3.prnt_msg() 
        # timer ------------------------------------
        

        pygame.display.flip()


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('Obj surf & txt')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    main()

    #pygame.quit()
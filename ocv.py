import numpy as np
from PIL import ImageGrab
import cv2
import time

print("start")

def ret_img(or_img, type = 'gray'):
    if (type == 'gray'):
        ret_scr = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        return ret_scr
    if (type == 'RGB'):
        ret_scr = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        return ret_scr
    


flag = True
last_time = time.time()
while(flag):
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    print("Loop {} sec".format(time.time()-last_time))
    last_time = time.time()
    #cv2.imshow('win', ret_img(screen, 'RGB'))
    #cv2.imshow('gray', ret_img(screen))
    #ret_img(screen, 'RGB')
    res = ret_img(screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        flag = False

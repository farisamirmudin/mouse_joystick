import pygame
import time
import mouse
from pynput.keyboard import Controller, Key
import os

def main():
    x = y = scroll = 0.0
    keyboard = Controller()
    done = False
    pygame.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joystick = joysticks[0]
    multp_move = 65
    multp_scroll = 5
    clip = lambda x ,k: x*k if abs(x)>0.1 else 0.0
    scaling = lambda x, min, max: (x-min)/(max-min)
    try:
        while not done:
            for event in pygame.event.get(): # User did something.
                if event.type == pygame.QUIT: # If user clicked close.
                    done = True # Flag that we are done so we exit this loop.
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        print('x is pressed')
                        mouse.press('left')
                    if event.button == 1:
                        mouse.click('right')
                    if event.button == 2:
                        keyboard.press(Key.alt)
                    if event.button == 11:
                        keyboard.press(Key.tab)
                    if event.button == 5:
                        done = True
                    if event.button == 9:
                        multp_move-=5
                        print("mouse pointer speed=", multp_move)
                    if event.button == 10:
                        multp_move+=5
                        print("mouse pointer speed=", multp_move)
                    if event.button == 15:
                        pass
                elif event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        print('x is released')
                        mouse.release('left')
                    if event.button == 2:
                        keyboard.release(Key.alt)
                    if event.button == 11:
                        keyboard.release(Key.tab)
                        
                elif event.type == pygame.JOYAXISMOTION:
                    x = clip(joystick.get_axis(0), multp_move)
                    y = clip(joystick.get_axis(1), multp_move)
                    scroll = clip(joystick.get_axis(3), multp_scroll)
                    
                    if event.axis == 4:
                        if event.value == 1.0:
                            print('lt full pressed')
                    if event.axis == 5:
                        if event.value == 1.0:
                            print('rt full pressed')
                    # lt = scaling(joystick.get_axis(4), -1, 1)
                    # rt = scaling(joystick.get_axis(5), -1, 1)
                    # if lt > 0.0:
                    #     print(joystick.get_axis(4))
                    # if rt > 0.0:
                    #     print(joystick.get_axis(5))
            mouse.move(x, y, absolute=False, duration=0.1)
            mouse.wheel(scroll)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
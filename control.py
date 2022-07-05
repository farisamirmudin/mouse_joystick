import pygame
import mouse
import handler
from misc import *
import time
import pyautogui as ag

# Initializing joystick
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick = joysticks[0]

ga = joystick.get_axis # Get axis value

while not done:
    for event in pygame.event.get(): # Button pressed or axis moved
        if event.type == pygame.JOYBUTTONDOWN: # Button is pressed
            cmd = default[event.button]
            print(cmd)
            if 'click' in cmd: # If command is to click
                button, n = handler.click(cmd)
                ag.click(button=button, clicks=n)
            else: # If command is to press key
                if cmd in keylist: # If it is a single command and available in the keylist
                    ag.press(cmd)
                if '+' in cmd: # If it is a combination of commands
                    if cmd == 'alt+tab': # alt+tab
                        if not falt:
                            ag.keyDown('alt')
                            time.sleep(0.1)
                            ag.keyDown('tab')
                            ag.keyUp('tab')
                            falt = not falt
                        else:
                            ag.keyUp('alt')
                            falt = not falt
                    else:
                        keys = handler.hotkey(cmd) 
                        ag.hotkey(*keys)
                if cmd == 'exit': # To exit the program
                    done = True
                if cmd == 'sens up': # Increase mouse sens
                    multp_move += 10
                if cmd == 'sens down': # Decrease mouse sens
                    multp_move -= 10

        elif event.type == pygame.JOYBUTTONUP: # Button is released
            pass
                    
        elif event.type == pygame.JOYAXISMOTION: # Axis is moved
            x = multp(ga(0), multp_move)
            y = multp(ga(1), multp_move)
            scroll = multp(ga(3), multp_scroll)
            # a4 = True if ga(4) > 0.9 else False
            # a5 = True if ga(5) > 0.9 else False

    mouse.move(x, y, absolute=False, duration=0.1) # Move mouse pointer
    mouse.wheel(scroll) # Scroll


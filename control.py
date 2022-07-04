import pygame
import mouse
import handler
from misc import *
import time

# Initializing joystick
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick = joysticks[0]

ga = joystick.get_axis

while not done:
    for event in pygame.event.get(): # Button pressed or axis moved
        if event.type == pygame.JOYBUTTONDOWN: # Button is pressed
            cmd = default[event.button]
            print(cmd)
            if 'click' in cmd:
                button, n = handler.click(cmd)
                agclick(button=button, clicks=n)
            else:
                if cmd in keylist:
                    agpress(cmd)
                else:
                    if '+' in cmd:
                        if cmd == 'alt+tab':
                            if not falt:
                                agkeydown('alt')
                                time.sleep(0.1)
                                agkeydown('tab')
                                agkeyup('tab')
                                falt = not falt
                            else:
                                agkeyup('alt')
                                falt = not falt
                        else:
                            keys = handler.hotkey(cmd)
                            aghotkey(*keys)
                    elif cmd == 'exit':
                        done = True
                    elif cmd == 'sens up':
                        multp_move += 10
                    elif cmd == 'sens down':
                        multp_move -= 10

        elif event.type == pygame.JOYBUTTONUP: # Button is released
            pass
                    
        elif event.type == pygame.JOYAXISMOTION:
            x = multp(ga(0), multp_move)
            y = multp(ga(1), multp_move)
            scroll = multp(ga(3), multp_scroll)
            # a4 = True if ga(4) > 0.9 else False
            # a5 = True if ga(5) > 0.9 else False

    mouse.move(x, y, absolute=False, duration=0.1)
    mouse.wheel(scroll)


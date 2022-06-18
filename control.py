import pygame
import pyautogui as pg
import mouse
from pynput.keyboard import Key, Controller
import readInput

# Initializing keyboard and joystick
keyboard = Controller()
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick = joysticks[0]

done = False
x = 0
y = 0
scroll = False
a4 = False
a5 = False

multp_move = 70
multp_scroll = 3
multp = lambda x, k: x*k if abs(x)>0.1 else 0

button_cmd = readInput.create_dict()
kp = keyboard.press
kr = keyboard.release
volDown = Key.media_volume_down
volUp = Key.media_volume_up
ga = joystick.get_axis

while not done:
    for event in pygame.event.get(): # Button pressed or axis moved
        if event.type == pygame.JOYBUTTONDOWN: # Button is pressed
            cmd = button_cmd[event.button]
            if cmd[0] == 'mouse':
                cmd[1](button=cmd[2])
            else:
                cmd[1](*cmd[2])

        elif event.type == pygame.JOYBUTTONUP: # Button is released
            pass
                    
        elif event.type == pygame.JOYAXISMOTION:
            x = multp(ga(0), multp_move)
            y = multp(ga(1), multp_move)
            scroll = multp(ga(3), multp_scroll)
            a4 = True if ga(4) > 0.9 else False
            a5 = True if ga(5) > 0.9 else False

    mouse.move(x, y, absolute=False, duration=0.1)
    mouse.wheel(scroll)

    kp(volDown) if a4 else kr(volDown)
    kp(volUp) if a5 else kr(volUp)

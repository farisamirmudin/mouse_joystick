import pygame
from pyautogui import *
import mouse
from pynput.keyboard import Key,Controller

def main():
    # Initializing keyboard and joystick
    keyboard = Controller()
    pygame.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joystick = joysticks[0]

    '''
    Initializing variables 
    A0, A1, A3 : axis value
    done : used for while loop
    scrollFlag : to scroll or not 
    multp_move : multiply axis value to a reasonable value
    multp : function that takes two parameters, axis value and multiplier
    '''
    
    A0=A1=A3=0.0
    done = False
    volumedown = volumeup = False
    
    multp_move = 70
    multp_scroll = 3
    multp = lambda x, k: x*k if abs(x)>0.1 else 0.0

    while not done:
        for event in pygame.event.get(): # Button pressed or axis moved
            if event.type == pygame.JOYBUTTONDOWN: # Button is pressed
                button = event.button
                if button == 0:
                    leftClick()
                if button == 1:
                    rightClick()
                if button == 2: # Dragging purpose
                    mouseDown()
                if button == 3:
                    pass
                if button == 5: # Stop program
                    done = True
                if button == 9:
                    multp_move -= 5
                if button == 10:
                    multp_move += 5
                if button == 11:
                    hotkey('ctrl', 'tab') # Changing tab in chrome
                if button == 12:
                    pass
                if button == 13:
                    press('left')
                if button == 14:
                    press('right')

            elif event.type == pygame.JOYBUTTONUP: # Button is released
                event.button = button
                if button == 2:
                    mouseUp()
                        
            elif event.type == pygame.JOYAXISMOTION:
                A0 = multp(joystick.get_axis(0), multp_move)
                A1 = multp(joystick.get_axis(1), multp_move)
                A3 = multp(joystick.get_axis(3), multp_scroll)
                A4 = joystick.get_axis(4)
                A5 = joystick.get_axis(5)

                if A4 > 0.9:
                    volumedown = True
                if A5 > 0.9:
                    volumeup = True
        mouse.move(A0, A1, absolute=False, duration=0.1)
        mouse.wheel(A3)
        if volumedown:
            keyboard.press(Key.media_volume_down) # Control system volume
            keyboard.release(Key.media_volume_down)
            volumedown = False
        if volumeup:
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            volumeup = False

if __name__ == "__main__":
    main()
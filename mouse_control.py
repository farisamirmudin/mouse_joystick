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
    A0, A1, A4 : axis value
    done : used for while loop
    scrollFlag : to scroll or not 
    multp_move : multiply axis value to a reasonable value
    multp : function that takes two parameters, axis value and multiplier
    '''
    
    A0=A1=A4=0.0
    done = False
    scrollFlag = False
    
    multp_move = 70
    multp = lambda x, k: x*k if abs(x)>0.1 else 0.0

    while not done:
        for event in pygame.event.get(): # Button pressed or axis moved
            if event.type == pygame.JOYBUTTONDOWN: # Button is pressed
                button = event.button
                if button == 0:
                    leftClick()
                if button == 1:
                    rightClick()
                if button == 2:
                    keyDown('alt')
                if button == 3:
                    mouseDown()
                if button == 4:
                    multp_move -= 5
                if button == 5:
                    multp_move += 5
                if button == 6:
                    keyboard.press(Key.media_volume_down) # Control system volume
                if button == 7:
                    keyboard.press(Key.media_volume_up)
                if button == 10: # Stop program
                    done = True
                
            elif event.type == pygame.JOYBUTTONUP: # Button is released
                if button == 2:
                    keyUp('alt')
                if button == 3:
                    mouseUp()
                if button == 6:
                    keyboard.release(Key.media_volume_down)
                if button == 7:
                    keyboard.release(Key.media_volume_up)
                    
            elif event.type == pygame.JOYAXISMOTION: # Axis is moved
                A0 = multp(joystick.get_axis(0), multp_move) # Horizontal movement of mouse
                A1 = multp(joystick.get_axis(1), multp_move) # Vertical movement of mouse
                A4 = joystick.get_axis(4) # value to set scrollFlag
                if abs(A4) > 0.6:
                    scrollFlag = True
                else:
                    scrollFlag = False
            elif event.type == pygame.JOYHATMOTION: # D-Pad
                HAT = joystick.get_hat(0)
                if HAT == (0,1): # Combine with button 2 (from above) results in Alt+tab
                    press('tab')
                if HAT == (-1, 0):
                    hotkey('ctrl', 'tab') # Changing tab in chrome
                if HAT == (1, 0):
                    press('right')
                if HAT == (1, 0):
                    press('down')
                
        mouse.move(A0, A1, absolute=False, duration=0.1) # move the mouse
        if scrollFlag:
            click = 3 if A4 > 0 else -3
            scroll(click) # scroll (direction inverted)

if __name__ == "__main__":
    main()
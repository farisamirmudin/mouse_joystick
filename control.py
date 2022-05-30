import pygame, pyautogui as ag, mouse
import win32api, win32con

def main():
    x = y = scroll = 0
    done = False
    pygame.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joystick = joysticks[0]
    multp_move = 65
    multp_scroll = 5
    clip = lambda x ,k: x*k if abs(x)>0.1 else 0.0
    scaling = lambda x, min, max: (x-min)/(max-min)
    left_right = False
    up_down = False
    try:
        while not done:
            for event in pygame.event.get(): # User did something.
                if event.type == pygame.QUIT: # If user clicked close.
                    done = True # Flag that we are done so we exit this loop.
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        mouse.press('left')
                    if event.button == 1:
                        mouse.press('right')
                    if event.button == 2:
                        curr = win32api.GetCursorPos()
                        x = 50
                        y = 50
                        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)
                        print('moved')
                    if event.button == 5:
                        done = True
                    if event.button == 9:
                        multp_move-=5
                        print("mouse pointer speed=", multp_move)
                    if event.button == 10:
                        multp_move+=5
                        print("mouse pointer speed=", multp_move)
                    if event.button == 11:
                        ag.keyDown('w')
                    if event.button == 12:
                        ag.keyDown('s')
                    if event.button == 13:
                        ag.keyDown('a')
                    if event.button == 14:
                        ag.keyDown('d')
                elif event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        mouse.release('left')
                    if event.button == 1:
                        mouse.release('right')
                    if event.button == 2:
                        pass
                    if event.button == 11:
                        ag.keyUp('w')
                    if event.button == 12:
                        ag.keyUp('s')
                    if event.button == 13:
                        ag.keyUp('a')
                    if event.button == 14:
                        ag.keyUp('d')
                        
                elif event.type == pygame.JOYAXISMOTION:
                    pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
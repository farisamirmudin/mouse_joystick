import pygame
import macmouse as mouse
import pyautogui as ag

# pygame setup
pygame.init()

# joystick setup
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick = joysticks[0]

def main():
    done = False
    multiplier_move = 4
    multiplier_scroll = 2
    xOffset = 0
    yOffset = 0
    scroll_delta = 0
    scaleMove = lambda x, k: x*k if abs(x)>0.1 else 0
    get_axis = joystick.get_axis
    volumeup = False
    volumedown = False

    while not done:
        if volumedown:
            ag.press(u'KEYTYPE_SOUND_DOWN')
            volumedown = False
        if volumeup:
            ag.press(u'KEYTYPE_SOUND_UP')
            volumeup = False
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    mouse.click(mouse.LEFT)
                if event.button == 1:
                    mouse.click(mouse.RIGHT)
                if event.button == 2:
                    ag.press('tab')
                if event.button == 3:
                    done = True
                if event.button == 9:
                    multiplier_move /= 1.5
                if event.button == 10:
                    multiplier_move *= 1.5
                if event.button == 12:
                    ag.keyDown('command')
                if event.button == 13:
                    ag.hotkey('ctrl', 'tab')
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 12:
                    ag.keyUp('command')
            if event.type == pygame.JOYAXISMOTION:
                xOffset = scaleMove(get_axis(0), multiplier_move)
                yOffset = scaleMove(get_axis(1), multiplier_move)
                scroll_delta = scaleMove(get_axis(3), multiplier_scroll)

                # https://stackoverflow.com/questions/64641029/trying-to-mute-the-system-using-pyautogui-pressvolumemute-but-its-not-doing

                if get_axis(4) > 0.999:
                    volumedown = True
                if get_axis(5) > 0.999:
                    volumeup = True

                mouse.move(xOffset, yOffset, False)
                mouse.wheel(scroll_delta)

if __name__ == "__main__":
    main()
    pygame.quit()

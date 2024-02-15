import pygame
import macmouse as mouse
import pyautogui as ag

# pygame setup
pygame.init()
pygame.joystick.init()

def main():
    joysticks = {}
    done = False
    multiplier_move = 10
    multiplier_scroll = 2
    scale = lambda x, k: x*k if abs(x)>0.1 else 0
    clock = pygame.time.Clock()

    while not done:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
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

        for joystick in joysticks.values():
            xOffset = scale(joystick.get_axis(0), multiplier_move)
            yOffset = scale(joystick.get_axis(1), multiplier_move)
            scroll_delta = scale(joystick.get_axis(3), multiplier_scroll)
            mouse.move(xOffset, yOffset, False)
            mouse.wheel(scroll_delta)

            if joystick.get_axis(2) > 0.99:
                ag.press('right')
            if joystick.get_axis(2) < -0.99:
                ag.press('left')
            # https://stackoverflow.com/questions/64641029/trying-to-mute-the-system-using-pyautogui-pressvolumemute-but-its-not-doing
            if joystick.get_axis(4) > 0.99:
                ag.press(u'KEYTYPE_SOUND_DOWN')
            if joystick.get_axis(5) > 0.99:
                ag.press(u'KEYTYPE_SOUND_UP')

if __name__ == "__main__":
    main()
    pygame.quit()

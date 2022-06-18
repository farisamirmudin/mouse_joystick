import pyautogui as pg

def handle_mouse(cmd):
    click = pg.doubleClick if 'double' in cmd else pg.click
    return 'mouse', click, 'left' if 'left' in cmd else 'right'

def handle_key(cmd):
    if '+' in cmd:
        cmd_list = cmd.strip().split('+')
        return 'keyboard', pg.hotkey, cmd_list

def create_dict():
    button_cmd_str = {}
    button_cmd = {}
    for i in range(16):
        cmd_str = input('Button {0}: '.format(i))
        cmd = None
        if 'click' in cmd_str:
            cmd = handle_mouse(cmd_str)
        else:
            cmd = handle_key(cmd_str)

        button_cmd_str[i] = cmd_str
        button_cmd[i] = cmd
    return button_cmd


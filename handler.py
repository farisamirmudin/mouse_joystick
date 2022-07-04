def click(cmd):
    n=1
    if 'double' in cmd:
        n=2
    if 'left' in cmd:
        return 'left', n
    else:
        return 'right', n
    

def hotkey(cmd):
    return [x for x in cmd.split('+')]



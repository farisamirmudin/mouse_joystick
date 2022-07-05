keylist = [ "\t", "\n", "\r", " ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", 
            "?", "@", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", 
            "~", "accept", "add", "alt", "altleft", "altright", "apps", "backspace", "browserback", "browserfavorites", "browserforward", "browserhome", "browserrefresh", "browsersearch", "browserstop", 
            "capslock", "clear", "convert", "ctrl", "ctrlleft", "ctrlright", "decimal", "del", "delete", "divide", "down", "end", "enter", "esc", "escape", "execute", "f1", "f10", "f11", "f12", "f13", 
            "f14", "f15", "f16", "f17", "f18", "f19", "f2", "f20", "f21", "f22", "f23", "f24", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "final", "fn", "hanguel", "hangul", "hanja", "help", "home", 
            "insert", "junja", "kana", "kanji", "launchapp1", "launchapp2", "launchmail", "launchmediaselect", "left", "modechange", "multiply", "nexttrack", "nonconvert", "num0", "num1", "num2", 
            "num3", "num4", "num5", "num6", "num7", "num8", "num9", "numlock", "pedown", "peup", "pause", "pgdn", "pgup", "playpause", "prevtrack", "print", "printscreen", "prntscrn", "prtsc", 
            "prtscr", "return", "right", "scrolllock", "select", "separator", "shift", "shiftleft", "shiftright", "sleep", "space", "stop", "subtract", "tab", "up", "volumedown", "volumemute", "volumeup", 
            "win", "winleft", "winright", "yen", "command", "option", "optionleft", "optionright" ]

default = { 0: "left click", 1: "right click", 2: "ctrl+tab", 3: "alt+tab", 4: "", 5: "exit", 6: "", 7: "", 8: "", 9: "sens down", 10: "sens up", 11: "volumeup", 12: "volumedown", 13: "left", 
            14: "right", 15: "" }

done = False
x = 0
y = 0
scroll = False
a4 = False
a5 = False
falt = False

multp_move = 70
multp_scroll = 3
multp = lambda x, k: x*k if abs(x)>0.1 else 0


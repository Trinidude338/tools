import curses
import time
import math

def main():
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.raw()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    curses.mousemask(1)
    c = ' '
    chars = []
    mouse = (0,0,0,0,0)
    maxyx = stdscr.getmaxyx()
    curs = [0, 0]
    while(1):
        drawChars(stdscr, chars)
        try:
            c = stdscr.getch()
            if (c == curses.KEY_MOUSE):
                mouse = curses.getmouse()
                curs = [mouse[2], mouse[1]]
        except:
            mouse = (0,0,0,0,0)
            c = -1
        if (c == 27):
            curses.mousemask(0)
            while (stdscr.getch()!=curses.KEY_DC):
                time.sleep(0.016)
            curses.endwin()
            exit(0)
        num = ""
        if (c == curses.KEY_F0):
            num = stdscr.getstr()
            direc = stdscr.getch()
            if (num.isdigit()):
                for i in range(int(num)):
                    if (direc==curses.KEY_UP):
                        curs[0] -= 1
                    elif (direc==curses.KEY_DOWN):
                        curs[0] += 1
                    elif (direc==curses.KEY_LEFT):
                        curs[1] -= 1
                    elif (direc==curses.KEY_RIGHT):
                        curs[1] += 1
                    else:
                        pass
            else:
                pass
        if (c == curses.KEY_BACKSPACE):
            curs[1] -= 1
            for i in chars:
                if (i[1]==curs[0] and i[2]==curs[1]):
                    chars.pop(chars.index(i))
        if (c == curses.KEY_UP):
            curs[0] -= 1
        if (c == curses.KEY_DOWN):
            curs[0] += 1
        if (c == curses.KEY_LEFT):
            curs[1] -= 1
        if (c == curses.KEY_RIGHT):
            curs[1] += 1
        if (curs[0]<0):
            curs[0] = 0
        elif (curs[0]>=maxyx[0]):
            curs[0] = maxyx[0]-1
        elif (curs[1]<0):
            curs[1] = 0
        elif(curs[1]>=maxyx[1]):
            curs[1] = maxyx[1]-1
        elif (c>31 and c<127):
            chars.append([chr(c), curs[0], curs[1]])
            curs[1] += 1
        elif (c == 127):
            for i in chars:
                if (i[1]==curs[0] and i[2]==curs[1]):
                    chars.pop(chars.index(i))
        stdscr.move(curs[0], curs[1])
        stdscr.addch(curses.ACS_BLOCK)
        stdscr.move(curs[0], curs[1])
        stdscr.refresh()
        stdscr.erase()
        time.sleep(0.016)
    curses.endwin()

def drawChars(stdscr, chars):
    for i in chars:
        stdscr.addch(i[1], i[2], i[0])

if __name__ == '__main__':
    main()

import curses
import time
import math
import random
import sys

def main():
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.raw()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    stdscr.keypad(True)
    stdscr.nodelay(True)
    maxyx = stdscr.getmaxyx()
    frame = 0
    extinguish = 0
    playing = 1
    intensity = [[0 for x in range(maxyx[1])] for y in range(maxyx[0])]
    intensity = addBuff(stdscr, intensity)
    while(1):
        if(frame>59):
            frame = 0
        else:
            frame += 1
        #draw stuff
        drawBuff(stdscr, intensity)
        #
        try:
            c = stdscr.get_wch()
        except:
            c = 0
        if(c=='q'):
            break
        if(c==' '):
            if(playing==1):
                playing = 0
            else:
                playing = 1
        if(c=='e'):
            if(extinguish==1):
                extinguish = 0
            else:
                extinguish = 1
        #do stuff
        if(playing):
            if(not extinguish):
                intensity = addBuff(stdscr, intensity)
            intensity = dispurseBuff(stdscr, intensity)
        #
        stdscr.refresh()
        stdscr.erase()
        time.sleep(0.016)
    curses.endwin()

def dispurseBuff(stdscr, intensity):
    maxyx = stdscr.getmaxyx()
    for y in range(maxyx[0]):
        for x in range(maxyx[1]):
            if(intensity[y][x]>99):
                intensity[y][x] = 99
            elif(intensity[y][x]<4):
                intensity[y][x] = 0
                try:
                    intensity[y-1][x] -= 25
                except:
                    pass
                try:
                    intensity[y][x-1] -= 10
                except:
                    pass
                try:
                    intensity[y][x+1] -= 10
                except:
                    pass
                try:
                    intensity[y+1][x] -= 5
                except:
                    pass
            elif(intensity[y][x]<22 and intensity[y][x]>4):
                intensity[y][x] -= 4
            elif(intensity[y][x]<40 and intensity[y][x]>22):
                intensity[y][x] *= 0.22
                try:
                    intensity[y-1][x] += 20
                except:
                    pass
                try:
                    intensity[y][x-1] += 10
                except:
                    pass
                try:
                    intensity[y][x+1] += 10
                except:
                    pass
                try:
                    intensity[y+1][x] -= 7
                except:
                    pass
            else:
                intensity[y][x] *= 0.22
                try:
                    intensity[y-1][x] += 40
                except:
                    pass
                try:
                    intensity[y][x+1] += 25
                except:
                    pass
                try:
                    intensity[y][x-1] += 25
                except:
                    pass
                try:
                    intensity[y+1][x] -= 10
                except:
                    pass
    return intensity

def addBuff(stdscr, intensity):
    maxyx = stdscr.getmaxyx()
    for y in range(int(maxyx[0]*95/100), int(maxyx[0])):
        for x in range(int(maxyx[1]*1/100), int(maxyx[1]*99/100)):
            intensity[y][x] = random.randrange(75, 95)
    return intensity

def drawBuff(stdscr, intensity):
    maxyx = stdscr.getmaxyx()
    for y in range(maxyx[0]):
        for x in range(maxyx[1]):
            if(intensity[y][x]<10):
                shade = ' '
                color = 2
            elif(intensity[y][x]<20):
                shade = '.'
                color = 1
            elif(intensity[y][x]<30):
                shade = ','
                color = 1
            elif(intensity[y][x]<40):
                shade = ';'
                color = 1
            elif(intensity[y][x]<50):
                shade = '!'
                color = 1
            elif(intensity[y][x]<60):
                shade = '%'
                color = 1
            elif(intensity[y][x]<70):
                shade = '&'
                color = 1
            elif(intensity[y][x]<80):
                shade = '#'
                color = 1
            elif(intensity[y][x]<90):
                shade = '$'
                color = 1
            else:
                shade = '@'
                color = 1
            try:
                stdscr.addch(y, x, shade, curses.color_pair(color))
            except:
                pass

if __name__ == '__main__':
    main()

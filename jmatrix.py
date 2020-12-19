import curses
import time
import math
import random
import sys

def main(stdscr):
    usage = "jmatrix.py [-t timeout] [-c \"character list\"] [-s] [-h]"
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.raw()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.keypad(True)
    stdscr.nodelay(True)
    maxyx = stdscr.getmaxyx()
    strings = []
    frame = 0
    playing = 1
    elapsed0 = time.time()
    timeout = 0
    elapsed = 0
    screensaver = 0
    chars = range(33, 127)
    for num, i in enumerate(sys.argv):
        if(i=="-t"):
            timeout = int(sys.argv[num+1])
        elif(i=="-c"):
            chars0 = list(sys.argv[num+1])
            chars = []
            for i in chars0:
                chars.append(ord(i))
        elif(i=="-s"):
            screensaver = 1
        elif(i=="-h" or i=="--help"):
            curses.endwin()
            print(usage)
            exit()
    while(elapsed<timeout or timeout==0):
        elapsed1 = time.time() 
        if(frame>59):
            frame = 0
        else:
            frame += 1
        #draw stuff
        for i in strings:
            drawString(stdscr, i)
        #
        try:
            c = stdscr.get_wch()
        except:
            c = 0
        if(screensaver):
            if(c!=0):
                break
        if(c=='q'):
            break
        elif(c==' '):
            if(playing==1):
                playing = 0
            else:
                playing = 1
        #do stuff
        if(len(strings)<maxyx[1]-1):
            if(playing):
                strings.append(genString(stdscr, strings, chars))
        elif(len(strings)>=maxyx[1]):
            while(len(strings)>=maxyx[1]):
                strings.pop()
        if(playing):
            if(frame%2==0):
                for i in strings:
                    i[3].pop()
                    i[3].insert(0, chr(random.choice(chars)))
                    i[0] += 1
                    if(i[4]>0):
                        i[4] -= 1
                    else:
                        i[4] = 5
        for i in strings:
            if(i[0]>=maxyx[0]+i[2]):
                strings.remove(i)
        elapsed = elapsed1 - elapsed0
        #
        stdscr.refresh()
        stdscr.erase()
        time.sleep(0.016)
    curses.endwin()

def genString(stdscr, strings, charsinp):
    #[y, x, len, [chars], blink]
    maxyx = stdscr.getmaxyx()
    lst = [0]
    options0 = []
    for i in strings:
        options0.append(i[1])
    options1 = []
    for i in range(maxyx[1]):
        if(i not in options0):
            options1.append(i)
    lst.append(random.choice(options1))
    leng = random.randrange(5, 25)
    lst.append(leng)
    chars = []
    for i in range(leng):
        chars.append(chr(random.choice(charsinp)))
    lst.append(chars)
    lst.append(random.randrange(6))
    return lst

def drawString(stdscr, string):
    maxyx = stdscr.getmaxyx()
    curs = [string[0], string[1]]
    for num, i in enumerate(string[3]):
        if(num==0 and string[4]==1):
            try:
                stdscr.addch(curs[0]+1, curs[1], curses.ACS_BLOCK)
            except:
                pass
        try:
            stdscr.addch(curs[0], curs[1], i, curses.color_pair(1))
        except:
            pass
        curs[0] -= 1

stdscr = curses.initscr()
curses.wrapper(main)

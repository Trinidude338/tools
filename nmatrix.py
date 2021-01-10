import curses
import time
import math
import random
import sys

def main(stdscr):
    usage = "nmatrix.py [-t timeout] [-w \"Words\"] [-s] [-h]"
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.raw()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscr.keypad(True)
    stdscr.nodelay(True)
    maxyx = stdscr.getmaxyx()
    words = ["if(x>0):", 
            "if(x<0):", 
            "if(x==0):", 
            "else:", 
            "while(x>0):", 
            "while(x<0):", 
            "while(x==0):", 
            "for(x>0):", 
            "for(x<0):", 
            "for(x==0):", 
            "def main():", 
            "def sin(x):", 
            "def cos(x):", 
            "def tan(x):", 
            "def return():", 
            "def mod(list):", 
            "x=0",
            "x=1",
            "x=2",
            "x=3",
            "x=4",
            "x=5",
            "x=6",
            "x=7",
            "x=8",
            "x=9",
            "y=0",
            "y=1",
            "y=2",
            "y=3",
            "y=4",
            "y=5",
            "y=6",
            "y=7",
            "y=8",
            "y=9",
            "import curses",
            "import math",
            "import time",
            "import random",
            "import sys",
            ]
    lines = []
    frame = 0
    randColor = 0
    playing = 1
    elapsed0 = time.time()
    timeout = 0
    elapsed = 0
    screensaver = 0
    chars = range(33, 127)
    for num, i in enumerate(sys.argv):
        if(i=="-t"):
            timeout = int(sys.argv[num+1])
        elif(i=="-w"):
            words = [str(x) for x in sys.argv[num+1].split('\\'+'n')]
        elif(i=="-s"):
            screensaver = 1
        elif(i=="-h" or i=="--help"):
            curses.endwin()
            print(usage)
            exit()
    while(elapsed<timeout or timeout==0):
        elapsed = time.perf_counter() 
        if(frame>59):
            frame = 0
        else:
            frame += 1
        #draw stuff
        for i in lines:
            drawLine(stdscr, i)
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
        elif(c=='r'):
            if(randColor==1):
                randColor = 0
            else:
                randColor = 1
        #do stuff
        if(playing):
            if(len(lines)<maxyx[0]):
                lines.append(genLine(stdscr, lines, words))
            for i in lines:
                if(randColor):
                    i[4] = random.randrange(1, 5)
                else:
                    i[4] = 0
                if(i[2]==0):
                    i[1] += 1
                else:
                    i[1] -= 1
                if(i[2]==0):
                    if(i[1]==maxyx[1]):
                        x = 0
                        for j in i[3]:
                            x += len(j)
                            x += 1
                        lines.append(genLine(stdscr, lines, words, i[0], i[1]-x, i[2]))
                    elif(i[1]>maxyx[1]*2+30):
                        lines.pop(lines.index(i))
                else:
                    if(i[1]==0):
                        x = 0
                        for j in i[3]:
                            x += len(j)
                            x += 1
                        lines.append(genLine(stdscr, lines, words, i[0], i[1]+x, i[2]))
                    elif(i[1]<0-maxyx[1]-30):
                        lines.pop(lines.index(i))
        #
        stdscr.refresh()
        stdscr.erase()
        time.sleep(0.016)
    curses.endwin()

def genLine(stdscr, lines, charsinp, ovrideY=-1, ovrideX=-1, ovrideDir=-1):
    #[y, x, dir, words, color]
    maxyx = stdscr.getmaxyx()
    lst = []
    options0 = []
    options1 = []
    for i in lines:
        options0.append(i[0])
    for i in range(maxyx[0]):
        if(i not in options0):
            options1.append(i)
    if(ovrideY==-1):
        lst.append(random.choice(options1))
    else:
        lst.append(ovrideY)
    if(ovrideX==-1):
        if(ovrideDir==-1):
            if(random.choice(range(2))==0):
                lst.append(-10)
                lst.append(0)
            else:
                lst.append(maxyx[1]+10)
                lst.append(1)
        else:
            if(ovrideDir==0):
                lst.append(-10)
                lst.append(0)
            else:
                lst.append(maxyx[1]+10)
                lst.append(1)
    else:
        if(ovrideDir==-1):
            if(random.choice(range(2))==0):
                lst.append(ovrideX)
                lst.append(0)
            else:
                lst.append(ovrideX)
                lst.append(1)
        else:
            if(ovrideDir==0):
                lst.append(ovrideX)
                lst.append(0)
            else:
                lst.append(ovrideX)
                lst.append(1)
    lst.append([])
    x = 0
    for i in lst[3]:
        x += len(i)
    while(x<maxyx[1]*8.7/10):
        lst[3].append(random.choice(charsinp))
        x = 0
        for i in lst[3]:
            x += len(i)
    lst.append(0)
    return lst

def drawLine(stdscr, line):
    maxyx = stdscr.getmaxyx()
    curs = [line[0], line[1]]
    if(line[2]==0):
        for i in line[3]:
            curs[1] -= len(i)+1
            for num, j in enumerate(i):
                try:
                    stdscr.addch(curs[0], curs[1]+num, j, curses.color_pair(line[4]))
                except:
                    pass
    else:
        for i in line[3]:
            for num, j in enumerate(i):
                try:
                    stdscr.addch(curs[0], curs[1]+num, j, curses.color_pair(line[4]))
                except:
                    pass
            curs[1] += len(i)+1

stdscr = curses.initscr()
curses.wrapper(main)

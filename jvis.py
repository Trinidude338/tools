import sounddevice
import curses
import time

def main():
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_CYAN)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    curses.raw()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)
    maxyx = stdscr.getmaxyx()
    rec = sounddevice.rec(frames=int(44100/80), channels=2)
    sounddevice.wait()
    playing = 1
    while(1):
        #draw frame
        drawScopeStereo(stdscr, rec)
        #
        #input
        try:
            c = stdscr.get_wch()
        except:
            c = 0
        #
        if(c=='q'):
            break
        if(c==' '):
            if(playing):
                playing = 0
            else:
                playing = 1
        if(playing):
            rec = sounddevice.rec(frames=int(44100/80), channels=2)
            sounddevice.wait()
        stdscr.refresh()
        stdscr.erase()
        time.sleep(0.00125)
    curses.endwin()

def drawScopeStereo(stdscr, rec):
    maxyx = stdscr.getmaxyx()
    for num, i in enumerate(rec):
        if(i[0]>=0.0):
            for num2, j in enumerate(range(int(i[0]*maxyx[0])+1)):
                if(int(maxyx[0]/2-num2)%8==1):
                    color = 1
                elif(int(maxyx[0]/2-num2)%8==2):
                    color = 2
                elif(int(maxyx[0]/2-num2)%8==3):
                    color = 3
                elif(int(maxyx[0]/2-num2)%8==4 or int(maxyx[0]/2-num2)==int(maxyx[0]/2)):
                    color = 4
                elif(int(maxyx[0]/2-num2)%8==5):
                    color = 5
                elif(int(maxyx[0]/2-num2)%8==6):
                    color = 6
                elif(int(maxyx[0]/2-num2)%8==7):
                    color = 7
                else:
                    color = 0
                if(num%3!=0):
                    try:
                        stdscr.addch(int(maxyx[0]/2-num2), num, ' ', curses.color_pair(color))
                    except:
                        pass
        if(i[1]>=0.0):
            for num2, j in enumerate(range(int((i[1])*maxyx[0])+1)):
                if(int(maxyx[0]/2+num2)%8==1):
                    color = 1
                elif(int(maxyx[0]/2+num2)%8==2):
                    color = 2
                elif(int(maxyx[0]/2+num2)%8==3):
                    color = 3
                elif(int(maxyx[0]/2+num2)%8==4 or int(maxyx[0]/2+num2)==int(maxyx[0]/2)):
                    color = 4
                elif(int(maxyx[0]/2+num2)%8==5):
                    color = 5
                elif(int(maxyx[0]/2+num2)%8==6):
                    color = 6
                elif(int(maxyx[0]/2+num2)%8==7):
                    color = 7
                else:
                    color = 0
                if(num%3!=0):
                    try:
                        stdscr.addch(int(maxyx[0]/2+num2), num, ' ', curses.color_pair(color))
                    except:
                        pass


if __name__ == '__main__':
    main()

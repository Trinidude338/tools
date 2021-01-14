import sounddevice
import curses
import time
import numpy as np

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
    frames = 75.0
    if(sounddevice.default.samplerate is None):
        sounddevice.default.samplerate = 22050
    rec = np.array(sounddevice.rec(frames=int(sounddevice.default.samplerate/frames), channels=2, blocking=True))
    newRec = np.array([[0.0, 0.0] for x in range(maxyx[1])])
    for i in range(maxyx[1]):
        sliced = np.array(rec[int((i/maxyx[1])*len(rec)):int((i+1/maxyx[1])*len(rec))])
        left = 0
        right = 0
        for j in sliced:
            left += j[0]
            right += j[1]
        left /= len(sliced)
        right /= len(sliced)
        if(rec[i][0]<left):
            newRec[i][0] = left
        else:
            newRec[i][0] = rec[i][1]-0.2
        if(rec[i][1]<right):
            newRec[i][1] = right
        else:
            newRec[i][1] = rec[i][1]-0.2
    playing = 1
    while(1):
        #draw frame
        drawScopeStereo(stdscr, newRec)
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
            elap0 = time.time()
            rec = np.array(sounddevice.rec(frames=int(sounddevice.default.samplerate/frames), channels=2, blocking=True))
            elap1 = time.time()
            elap = elap1 - elap0
            for i in range(maxyx[1]):
                sliced = np.array(rec[int((i/maxyx[1])*len(rec)):int((i+1/maxyx[1])*len(rec))])
                left = 0
                right = 0
                for j in sliced:
                    left += j[0]
                    right += j[1]
                left /= len(sliced)
                right /= len(sliced)
                if(newRec[i][0]<left):
                    newRec[i][0] = left
                else:
                    newRec[i][0] -= 0.05
                if(newRec[i][1]<right):
                    newRec[i][1] = right
                else:
                    newRec[i][1] -= 0.05
        stdscr.refresh()
        stdscr.erase()
        if((frames*0.000028)-elap>0):
            time.sleep((frames*0.000028)-elap)
    curses.endwin()

def drawScopeStereo(stdscr, rec):
    maxyx = stdscr.getmaxyx()
    for i in range(maxyx[1]):
        if(i%3==0):
            continue
        stdscr.addch(int(maxyx[0]/2), i, ' ', curses.color_pair(4))
    for num, i in enumerate(rec):
        if(i[0]>=0.0):
            for num2, j in enumerate(range(int(i[0]*maxyx[0])+1)):
                if(num%3==0):
                    break
                if(num2<=0.0):
                    color = 4
                elif(int(maxyx[0]/2-num2)%8==1):
                    color = 1
                elif(int(maxyx[0]/2-num2)%8==2):
                    color = 2
                elif(int(maxyx[0]/2-num2)%8==3):
                    color = 3
                elif(int(maxyx[0]/2-num2)%8==4):
                    color = 4
                elif(int(maxyx[0]/2-num2)%8==5):
                    color = 5
                elif(int(maxyx[0]/2-num2)%8==6):
                    color = 6
                elif(int(maxyx[0]/2-num2)%8==7):
                    color = 7
                else:
                    color = 4
                try:
                    stdscr.addch(int(maxyx[0]/2-num2), num, ' ', curses.color_pair(color))
                except:
                    pass
        if(i[1]>=0.0):
            for num2, j in enumerate(range(int((i[1])*maxyx[0])+1)):
                if(num%3==0):
                    break
                if(num2<=0.0):
                    color = 4
                elif(int(maxyx[0]/2+num2)%8==1):
                    color = 1
                elif(int(maxyx[0]/2+num2)%8==2):
                    color = 2
                elif(int(maxyx[0]/2+num2)%8==3):
                    color = 3
                elif(int(maxyx[0]/2+num2)%8==4):
                    color = 4
                elif(int(maxyx[0]/2+num2)%8==5):
                    color = 5
                elif(int(maxyx[0]/2+num2)%8==6):
                    color = 6
                elif(int(maxyx[0]/2+num2)%8==7):
                    color = 7
                else:
                    color = 4
                try:
                    stdscr.addch(int(maxyx[0]/2+num2), num, ' ', curses.color_pair(color))
                except:
                    pass


if __name__ == '__main__':
    main()

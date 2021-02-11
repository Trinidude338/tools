import curses
import time
import math
import random
import sys
import os
import vlc

def main(stdscr):
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.raw()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscr.keypad(True)
    stdscr.nodelay(True)
    maxyx = stdscr.getmaxyx()
    formats = [".mp3", ".wav", ".wma", ".mp4", ".mp4"]
    frame = 0
    playing = 1
    state = 0
    prev = 0
    curs = 0
    stopped = False
    prevSongs = []
    songs0 = os.listdir()
    songs = []
    for num, i in enumerate(songs0):
        if(i[-4:] in formats):
            songs.append(i)
    if(len(songs)<1):
        exit(1)
    song = random.choice(songs)
    prevSongs.append(song)
    player = vlc.MediaPlayer(song)
    length = player.get_position()
    while(1):
        if(frame>59):
            frame = 0
        else:
            frame += 1
        #draw stuff
        if(state==0):
            drawPlayer(stdscr, song, length)
        else:
            drawMenu(stdscr, songs, curs)
        #
        try:
            c = stdscr.get_wch()
        except:
            c = 0
        if(c=='q'):
            break
        elif(c=='m'):
            if(state==1):
                state = 0
            else:
                state = 1
        elif(c=='z'):
            prev += 1
            stopped = False
            player.stop()
            if(len(prevSongs)==0):
                song = random.choice(songs)
                player = vlc.MediaPlayer(song)
            else:
                song = prevSongs[(prev+1)*-1]
                player = vlc.MediaPlayer(song)
        elif(c=='x'):
            stopped = False
            playing = 1
        elif(c==' ' or c=='c'):
            stopped = False
            if(playing==1):
                playing = 0
                player.pause()
            else:
                playing = 1
        elif(c=='v'):
            player.stop()
            stopped = True
        elif(c=='b'):
            prevSongs.append(song)
            stopped = False
            player.stop()
            if(prev==0):
                song = random.choice(songs)
            else:
                prev -= 1
                song = prevSongs[(prev+1)*-1]
            player = vlc.MediaPlayer(song)
        elif(c==curses.KEY_UP and curs>0):
            curs -= 1
        elif(c==curses.KEY_DOWN and curs<len(songs)-1):
            curs += 1
        elif(c==chr(10) or c==chr(13)):
            prevSongs.append(song)
            stopped = False
            player.stop()
            prev = 0
            song = songs[curs]
            player = vlc.MediaPlayer(song)
        #do stuff
        if(playing and not stopped):
            player.play()
        length = player.get_position()
        if(length>=.99):
            prevSongs.append(song)
            stopped = False
            player.stop()
            prev = 0
            song = random.choice(songs)
            player = vlc.MediaPlayer(song)
        #
        stdscr.refresh()
        stdscr.erase()
        time.sleep(0.016)
    curses.endwin()

def drawMenu(stdscr, songs, curs):
    maxyx = stdscr.getmaxyx()
    if(curs<(maxyx[0]/2)):
        visible = songs[:maxyx[0]]
        rCurs = curs
    elif(curs>(len(songs)-maxyx[0]/2)):
        visible = songs[maxyx[0]*-1:]
        rCurs = int(maxyx[0]/2+(curs-(len(songs)-maxyx[0]/2)))
    else:
        visible = songs[int(curs-(maxyx[0]/2)):int(curs+(maxyx[0]/2))]
        rCurs = int(maxyx[0]/2)+1
    for num, i in enumerate(visible):
        if(num==rCurs):
            try:
                stdscr.addstr(num, 1, i, curses.color_pair(1))
            except:
                pass
            continue
        try:
            stdscr.addstr(num, 1, i, curses.color_pair(0))
        except:
            pass

def drawPlayer(stdscr, song, length):
    size = 50
    line0 = "[Z]Previous    [X]Play    [C]Toggle Pause    [V]Stop    [B]Next    [M]Song list"
    maxyx = stdscr.getmaxyx()
    stdscr.addstr(int(maxyx[0]/2)-1, int(maxyx[1]/2-(len(song)/2)), song, curses.color_pair(3))
    complete = ""
    complete += '['
    for i in range(size):
        if(int(size*length)==i):
            complete += '>'
        elif(size*length>i):
            complete += '='
        else:
            complete += '-'
    complete += ']'
    stdscr.addstr(int(maxyx[0]/2)+1, int(maxyx[1]/2-(len(complete)/2)), complete, curses.color_pair(2))
    stdscr.addstr(int(maxyx[0]/2)+3, int(maxyx[1]/2-(len(line0)/2)), line0, curses.color_pair(4))

stdscr = curses.initscr()
curses.wrapper(main)

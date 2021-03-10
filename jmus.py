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
    repeat = 0
    playing = 1
    state = 0
    prev = 0
    prevNum = 0
    curs = 0
    volume = 100
    stopped = False
    prevSongs = []
    prevSearch = ""
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
    dur = player.get_length()
    while(1):
        if(frame>59):
            frame = 0
        else:
            frame += 1
        #draw stuff
        if(state==0):
            drawPlayer(stdscr, song, length, dur, volume, repeat)
        else:
            drawMenu(stdscr, songs, curs, length, dur, volume)
        #
        try:
            c = stdscr.get_wch()
        except:
            c = 0
        if(c=='q'):
            break
        elif(c=='-'):
            if(volume>=10):
                volume -= 10
        elif(c=='_'):
            if(volume>=1):
                volume -= 1
        elif(c=='='):
            if(volume<=90):
                volume += 10
        elif(c=='+'):
            if(volume<=99):
                volume += 1
        elif(c=='/'):
            search = ""
            f = False
            while(1):
                state = 1
                stdscr.erase()
                drawMenu(stdscr, songs, curs, length, dur, volume)
                stdscr.addstr(int(maxyx[0]-1), 0, str(" "*(maxyx[1]-1)))
                stdscr.addstr(int(maxyx[0]-1), 0, '/'+search)
                stdscr.refresh()
                if(f):
                    break
                try:
                    c = stdscr.get_wch()
                except:
                    c = 0
                if(c==chr(10) or c==chr(13)):
                    for num, i in enumerate(songs):
                        if(search in i):
                            curs = num
                            prevNum = num
                            f = True
                            break 
                        elif(num==len(songs)-1):
                            f = True
                elif(c==chr(8)):
                    search = search[:-1]
                elif(c==chr(27)):
                    search = ""
                    break
                elif(c!=0):
                    search += c
            prevSearch = search
            c = 0
        elif(c=='n'):
            b = False
            for num, i in enumerate(songs):
                if(prevSearch in i and num>prevNum):
                    curs = num
                    prevNum = num
                    break
                elif(num==len(songs)-1):
                    b = True
            if(b):
                for num, i in enumerate(songs):
                    if(prevSearch in i):
                        curs = num
                        prevNum = num
                        break
        elif(c=='m'):
            if(state==1):
                state = 0
            else:
                state = 1
        elif(c=='r'):
            if(repeat==0):
                repeat = 1
                repSong = song
            else:
                repeat = 0
        elif(c=='z'):
            stopped = False
            player.stop()
            if(prev<len(prevSongs)-1):
                prev += 1
                song = prevSongs[(prev+1)*-1]
            else:
                song = random.choice(songs)
                prevSongs.insert(0, song)
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
            stopped = False
            player.stop()
            if(repeat==0):
                if(prev>0):
                    song = prevSongs[(prev+1)*-1]
                    prev -= 1
                else:
                    song = random.choice(songs)
                    if(prevSongs[-1]!=song):
                        prevSongs.append(song)
                player = vlc.MediaPlayer(song)
            else:
                song = repSong
                player = vlc.MediaPlayer(repSong)
        elif(c==curses.KEY_RIGHT):
            player.set_time(player.get_time()+5000)
        elif(c==curses.KEY_LEFT):
            player.set_time(player.get_time()-5000)
        elif(c==curses.KEY_UP and curs>0):
            curs -= 1
        elif(c==curses.KEY_DOWN and curs<len(songs)-1):
            curs += 1
        elif(c==chr(46)):
            curs += int(maxyx[0]/2)
            if(curs>=len(songs)):
                curs = len(songs)
        elif(c==chr(44)):
            curs -= int(maxyx[0]/2)
            if(curs<0):
                curs = 0
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
        if(length>=.999):
            prevSongs.append(song)
            stopped = False
            player.stop()
            prev = 0
            if(repeat==0):
                song = random.choice(songs)
            else:
                song = repSong
            player = vlc.MediaPlayer(song)
        dur = player.get_length()
        player.audio_set_volume(volume)
        #
        stdscr.refresh()
        stdscr.erase()
        time.sleep(0.016)
    curses.endwin()

def drawMenu(stdscr, songs, curs, length, duration, volume):
    maxyx = stdscr.getmaxyx()
    if(curs<(maxyx[0]/2)):
        visible = songs[:maxyx[0]]
        rCurs = curs
    elif(curs>(len(songs)-maxyx[0]/2)):
        visible = songs[maxyx[0]*-1:]
        rCurs = int(maxyx[0]/2+(curs-(len(songs)-maxyx[0]/2)))
    else:
        visible = songs[int(curs-(maxyx[0]/2)):int(curs+(maxyx[0]/2))]
        if((maxyx[0]/2)%1==0):
            rCurs = int(maxyx[0]/2)
        else:
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
    tminus = int((duration/1000)-(duration*length)/1000)
    if(tminus%60>=10):
        tminus = str('-'+str(int(tminus/60))+':'+str(tminus%60))
    else:
        tminus = str('-'+str(int(tminus/60))+':'+'0'+str(tminus%60))
    status = "[/]Start Search    [N]Next Search Item    Volume: "+str(volume)+'  '+"T: "+str(tminus)
    stdscr.addstr(0, int(maxyx[1]-len(status)), status, curses.color_pair(1))

def drawPlayer(stdscr, song, length, duration, volume, repeat):
    size = 50
    line0 = "[Z]Previous    [X]Play    [C]Toggle Pause    [V]Stop    [B]Next    [M]Song list"
    line2 = "[R]Repeat Song"
    line1 = ""
    line1 += "Volume: "+str(volume)
    if(repeat==1):
        line1 += " (ON REPEAT)"
    maxyx = stdscr.getmaxyx()
    stdscr.addstr(int(maxyx[0]/2)-1, int(maxyx[1]/2-(len(song)/2)), song, curses.color_pair(3))
    complete = ""
    tplus = int((duration*length)/1000)
    tminus = int((duration/1000)-(duration*length)/1000)
    if(tplus%60>=10):
        tplus = str(str(int(tplus/60))+':'+str(tplus%60))
    else:
        tplus = str(str(int(tplus/60))+':'+'0'+str(tplus%60))
    if(tminus%60>=10):
        tminus = str('-'+str(int(tminus/60))+':'+str(tminus%60))
    else:
        tminus = str('-'+str(int(tminus/60))+':'+'0'+str(tminus%60))
    complete += tplus
    complete += '\t'
    complete += '['
    for i in range(size):
        if(int(size*length)==i):
            complete += '>'
        elif(size*length>i):
            complete += '='
        else:
            complete += '-'
    complete += ']'
    complete += '\t'
    complete += tminus
    stdscr.addstr(int(maxyx[0]/2)+1, int(maxyx[1]/2-(len(complete)/2)), complete, curses.color_pair(2))
    stdscr.addstr(int(maxyx[0]/2)+3, int(maxyx[1]/2-(len(line0)/2)), line0, curses.color_pair(4))
    stdscr.addstr(int(maxyx[0]/2)+5, int(maxyx[1]/2-(len(line2)/2)), line2, curses.color_pair(4))
    stdscr.addstr(int(maxyx[0]/2)+7, int(maxyx[1]/2-(len(line1)/2)), line1, curses.color_pair(1))

stdscr = curses.initscr()
curses.wrapper(main)

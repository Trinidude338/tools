import curses
import math
import time

gridNumber = [0, 17, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 48, 49, 50, 51, 52, 53]
gridNumber.extend(range(54, 126))

symbols = [
        "H",                                                                                                "He", 
        "Li", "Be",                                                                "B", "C", "N", "O", "F", "Ne", 
        "Na", "Mg",                                                             "Al", "Si", "P", "S", "Cl", "Ar",
        "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
        "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
        "Cs", "Ba", "La-Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Ti", "Pb", "Bi", "Po", "At", "Rn",
        "Fr", "Ra", "Ac-Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Uut", "Fl", "Uup", "Lv", "Uus", "Uuo"
        ]

atomicNumber = [
        1,                                                                   2,
        3, 4,                                                5, 6, 7, 8, 9, 10,
        11, 12,                                         13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
        37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 
        55, 56, 0, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
        87, 88, 0, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118
        ]

massNumber = [
        1.008,                                                                                                                 4.003,
        6.94, 9.012,                                                                        10.81, 12.01, 14.01, 16.00, 19.00, 20.18,
        22.99, 24.31,                                                                       26.98, 28.09, 30.97, 32.06, 35.45, 39.95,
        39.10, 40.08, 44.96, 47.87, 50.94, 52.00, 54.94, 55.85, 58.93, 58.69, 63.55, 65.38, 69.72, 72.63, 74.92, 78.97, 79.90, 83.80,
        85.47, 87.62, 88.91, 91.22, 92.91, 95.95, 97.0, 101.1, 102.9, 106.4, 107.9, 112.4, 114.8, 118.7, 121.8, 127.6, 126.9, 131.3,
        132.9, 137.3,   0.0, 178.5, 180.9, 183.8, 186.2, 190.2, 192.2, 195.1, 197.0, 200.6, 204.4, 207.2, 209.0, 209.0, 210.0, 222.0,
        223.0, 226.0,   0.0, 267.0, 270.0, 271.0, 270.0, 277.0, 276.0, 281.0, 282.0, 285.0, 285.0, 289.0, 288.0, 293.0, 294.0, 294.0
        ]

def drawTable(stdscr, symbols, atomicNumber, massNumber, gridNumber):
    maxyx = stdscr.getmaxyx()
    #line0 = "+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+"
    line0 = [ curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_HLINE, curses.ACS_PLUS]
    #line1 = "|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |"
    line1 = [ curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE]
    topLeftCorner = [math.trunc(maxyx[0]/2-19), math.trunc(maxyx[1]/2-55)]
    curs = [topLeftCorner[0], topLeftCorner[1]]
    for x in range(7):
        for i in line0:
            stdscr.addch(curs[0], curs[1], i)
            curs[1] += 1
        curs[0] += 1
        curs[1] = topLeftCorner[1]
        for y in range(3):
            for j in line1:
                stdscr.addch(curs[0], curs[1], j)
                curs[1] += 1
            curs[0] += 1
            curs[1] = topLeftCorner[1]
    for i in line0:
        stdscr.addch(curs[0], curs[1], i)
        curs[1] += 1
    curs[0] = topLeftCorner[0]
    curs[1] = topLeftCorner[1]+7
    for x in range(95):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+1
    curs[1] = topLeftCorner[1]+7
    for x in range(95):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+2
    curs[1] = topLeftCorner[1]+7
    for x in range(95):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+3
    curs[1] = topLeftCorner[1]+7
    for x in range(95):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+4
    curs[1] = topLeftCorner[1]+13
    for x in range(59):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+5
    curs[1] = topLeftCorner[1]+13
    for x in range(59):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+6
    curs[1] = topLeftCorner[1]+13
    for x in range(59):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+7
    curs[1] = topLeftCorner[1]+13
    for x in range(59):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+8
    curs[1] = topLeftCorner[1]+13
    for x in range(59):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+9
    curs[1] = topLeftCorner[1]+13
    for x in range(59):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+10
    curs[1] = topLeftCorner[1]+13
    for x in range(59):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    curs[0] = topLeftCorner[0]+11
    curs[1] = topLeftCorner[1]+13
    for x in range(59):
        stdscr.addch(curs[0], curs[1], ' ')
        curs[1] += 1
    for num, x in enumerate(gridNumber):
        curs[0] = int(topLeftCorner[0]+int(x/18)*4)+1
        curs[1] = int(topLeftCorner[1]+int(x%18)*6)+1
        stdscr.addstr(curs[0], curs[1], str(massNumber[num]))
        curs[0] = int(topLeftCorner[0]+int(x/18)*4)+2
        curs[1] = int(topLeftCorner[1]+int(x%18)*6)+1
        stdscr.addstr(curs[0], curs[1], symbols[num])
        curs[0] = int(topLeftCorner[0]+int(x/18)*4)+3
        curs[1] = int(topLeftCorner[1]+int(x%18)*6)+1
        stdscr.addstr(curs[0], curs[1], str(atomicNumber[num]))

def main():
    stdscr = curses.initscr()
    curses.start_color()
    curses.raw()
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(True)
    stdscr.keypad(True)
    curses.curs_set(0)
    maxyx = stdscr.getmaxyx()
    if(maxyx[0]<40 or maxyx[1]<110):
        screenTooSmall(stdscr)
        curses.endwin()
        exit(1)
    drawTable(stdscr, symbols, atomicNumber, massNumber, gridNumber)
    stdscr.refresh()
    while(stdscr.getch()==curses.ERR):
        time.sleep(0.01)
    curses.endwin()

if __name__ == '__main__':
    main()

def main():
    stdscr = curses.initscr()
    curses.start_color()
    curses.raw()
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(True)
    stdscr.keypad(True)
    curses.curs_set(0)
    maxyx = stdscr.getmaxyx()
    if(maxyx[0]<40 or maxyx[1]<110):
        screenTooSmall(stdscr)
        curses.endwin()
        exit(1)
    drawTable(stdscr, symbols, atomicNumber, massNumber, gridNumber)
    stdscr.refresh()
    while(stdscr.getch()==curses.ERR):
        time.sleep(0.01)
    curses.endwin()

if __name__ == '__main__':
    main()

import curses

screen = curses.initscr()

curses.start_color()

screen.addstr("Pogrubiony\n", curses.A_BOLD)
screen.addstr("podświetlony\n", curses.A_STANDOUT)
screen.addstr("podkreślony\n", curses.A_UNDERLINE)

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

screen.addstr("CZERWONY ALARM!!!", curses.color_pair(1))

screen.addstr("CZERWONY ALARM!!!", curses.color_pair(1) | curses.A_BOLD | curses.A_DIM)


screen.refresh()

curses.napms(6000)
curses.endwin()

print("Zakończono...")

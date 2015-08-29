import random
from curses import wrapper
import curses

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# stdscr = curses.initscr()
# curses.cbreak()
# curses.noecho()
# stdscr.keypad(True)

def temp(stdscr):
	# Clear screen
	stdscr.clear()


	# for i in range(0, 9):
	#     v = i-10
	#     stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

	while True:

		key = stdscr.getkey()
		stdscr.refresh()
		if key == "\n":
			break
		print(key)

wrapper(temp)


# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()

curses.endwin()

# for i in range(1,10):
# 	text = "\033["
# 	text += str(i) + "m"
# 	text += chr(9608)
# 	text += "\033[0m"
# 	print(i, text)

# for i in range(30,47):
# 	text = "\033["
# 	text += str(i) + "m"
# 	text += chr(9608)
# 	text += "\033[0m"
# 	print(i, text)

# for i in range(90,98):
# 	text = "\033["
# 	text += str(i) + "m"
# 	text += chr(9608)
# 	text += "\033[0m"
# 	print(i, text)



# for i in range(1,10):
# 	text = chr(9608) + "(" + str(i) + ") "

# 	if random.randint(0,1):
# 		text += "Still needs work"
# 		print(bcolors.FAIL, text, bcolors.ENDC)
# 	else:
# 		text += "Everything is good"
# 		print(bcolors.OKGREEN, text, bcolors.ENDC)




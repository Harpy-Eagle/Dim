import sys
import time
import curses

def slow_print(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(1)


def fast_print(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.001)


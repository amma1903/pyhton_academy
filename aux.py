from gameplay import *
import os
from time import sleep
from sys import *
from names import *
from aux import *

def clear_screen(wait):
    print(f'\n(Screen will be cleared in {wait} seconds)')
    sleep(wait) # Waiting for 4 seconds to clear the screen
    os.system('clear') # Clearing the Screen

def read_args():
    args = list(argv)
    arg = {'name': False, 'score': False}

    for a in range(1, len(args)):
        if args[a].isnumeric() and arg['score'] == False:
            arg['score'] = int(args[a])
            if arg['score'] > 100:
                arg['score'] = 100
        elif arg['name'] == False:
            arg['name'] = args[a]

    return arg

def instructions():
    print("\nWinning Rules of the Rock paper scissor game as follows: \n"
                                    +"rock vs paper->paper wins \n"
                                    + "rock vs scissor->rock wins \n"
                                    +"paper vs scissor->scissor wins \n")
    clear_screen(10)
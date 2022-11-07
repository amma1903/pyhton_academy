from gameplay import *
import os
from time import sleep
from sys import *
from names import *
from aux import *

def get_older_name():

    try:
        with open('older_name.txt', 'r') as f:
            lines = f.readlines()
            return lines[0]
    except:
        with open('older_name.txt', 'w+') as f:
            return 'default'

def save_name(name):
    with open('older_name.txt', 'w+') as f:
        f.write(name)

def aplly_name(args):
    if args['name'] != False:
        save_name(args['name'])
        return args['name']

    print(f'Before start playing choose your name:')
    name =  input()

    if name == '':
        name = get_older_name()

    save_name(name)

    return name
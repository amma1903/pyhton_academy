from gameplay import *
import os
from time import sleep
from sys import *
from names import *
from aux import *
from score import *

pcScore = 0
myScore = 0
player = Gameplay()
computer = Gameplay()
args = read_args()
name = aplly_name(args)
print(f"""Your name is: {name} and the max score is: {args['score']}""")

while True:
    option = read_input()
    computer.set_play_random()

    if option == 0 or option == 1 or option == 2:
        player.set_play(option)
        winner = play(player, computer)
        pcScore, myScore = updateScore(pcScore,myScore,winner)
        check_max_score_reached(pcScore, myScore, args['score'])
    elif option == 3:
        instructions()
    else:
        break


'''
tratar show resultado a cada iteracao
testes
'''


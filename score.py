from random import randint
from gameplay import *
import os
from time import sleep
from sys import *
from names import *
from aux import *

def play(player, computer):
    win = player.show_winner(computer)
    my_hand = player.show_play()
    pc_hand = computer.show_play()
    if win == 'W':
        print(f'You won!!! Your hand ({mapping_hands(my_hand)}) is stronger then the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)
    elif win == 'L':
        print(f'You lost!!! Your hand ({mapping_hands(my_hand)}) is weaker then the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)
    else:
        print(f'You draw!!! Your hand ({mapping_hands(my_hand)}) is equal to the computers ({mapping_hands(pc_hand)})')
        clear_screen(5)
    return win

def mapping_hands(hand):
    if hand == 0:
        return 'Rock'
    elif hand == 1:
        return 'Paper'
    elif hand == 2:
        return 'Scizor'
    else:
        'undefined hand error, please correct code'

def check_max_score_reached(pcScore,myScore, maxScore):
    if maxScore != False:
        if pcScore == maxScore:
            print('Max score reached. You have lost. Sad face!')
            clear_screen(10)
            exit()
        elif myScore == maxScore:
            print('Max score reached. You have won. Congratulations!')
            clear_screen(10)
            exit()



def read_input():
    while True:
        print("Enter choice \n Rock \n Paper \n Scissor \n Instructions \n Exit ")

        players_choice =  input()

        if players_choice == '0' or 'rock'.find(players_choice.lower()) == 0:
            return 0
        elif players_choice == '1' or 'paper'.find(players_choice.lower()) == 0:
            return 1
        elif players_choice == '2' or 'scissor'.find(players_choice.lower()) == 0:
            return 1
        elif players_choice == '3' or 'instructions'.find(players_choice.lower()) == 0:
            return 1
        elif players_choice == '4' or 'exit'.find(players_choice.lower()) == 0:
            return 1
        else:
            print('please choose from one of the valid options')

def updateScore(pcScore,myScore,winner):

    if winner == 'W':
        myScore += 1
    elif winner == 'L':           
        pcScore += 1
    print(f'PC Score: {pcScore}\nMy Score: {myScore}\n')
    return pcScore, myScore
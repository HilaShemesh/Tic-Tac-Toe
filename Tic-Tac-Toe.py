#!/usr/bin/env python
# coding: utf-8

# In[13]:


from IPython.display import clear_output

def display_board(board):
    clear_output()  #this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[14]:


# define mark of each player

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']   


# In[15]:


#place inputs on boards
def place_marker(board, marker, position):
    board[position] = marker
        


# In[16]:


#check game status
def win(board, marker):
     return ((board[7] == board[8] == board[9] == marker) or
            (board[9] == board[5] == board[1] == marker) or
            (board[8] == board[5] == board[2] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[1] == board[2] == board[3] == marker) or
            (board[7] == board[4] == board[1] == marker) or 
            (board[9] == board[6] == board[3] == marker) or
            (board[7] == board[5] == board[3] == marker))
    


# In[17]:


import random
def random_player_start(player1, player2):
    lst_players = ['X', 'O']
    start = random.choice(lst_players)
    if start == player1:
        return lst_players[0]
    else:
        return lst_players[1]


# In[18]:


def full_board_check(board):
    flag = True
    loc = 0
    while flag:
        if board[loc] != 'X' and board[loc] != 'O':
            flag = False
        else:
            loc +=1
            
    return flag


# In[19]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[20]:


def space_check(board, position):
    
    return board[position] == ' '


# In[21]:


def pos_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[22]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = pos_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = pos_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





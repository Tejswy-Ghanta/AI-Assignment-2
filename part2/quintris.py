# Simple quintris program! v0.2
# D. Crandall, Sept 2021
# lghanta, shrgutta, pursurve

from AnimatedQuintris import *
from SimpleQuintris import *
from kbinput import *
import time, sys
import copy
import re

class HumanPlayer:
    def get_moves(self, quintris):
        print("Type a sequence of moves using: \n  b for move left \n  m for move right \n  n for rotation\n  h for horizontal flip\nThen press enter. E.g.: bbbnn\n")
        moves = input()
        return moves

    def control_game(self, quintris):
        while 1:
            c = get_char_keyboard()
            commands =  { "b": quintris.left, "h": quintris.hflip, "n": quintris.rotate, "m": quintris.right, " ": quintris.down }
            commands[c]()

#####
# This is the part you'll want to modify!
# Replace our super simple algorithm with something better
#
class ComputerPlayer:
    # This function should generate a series of commands to move the piece into the "optimal"
    # position. The commands are a string of letters, where b and m represent left and right, respectively,
    # and n rotates. quintris is an object that lets you inspect the board, e.g.:
    #   - quintris.col, quintris.row have the current column and row of the upper-left corner of the 
    #     falling piece
    #   - quintris.get_piece() is the current piece, quintris.get_next_piece() is the next piece after that
    #   - quintris.left(), quintris.right(), quintris.down(), and quintris.rotate() can be called to actually
    #     issue game commands
    #   - quintris.get_board() returns the current state of the board, as a list of strings.
    #
    def __init__(self):
        self.col_weights = [i*15 for i in range(1,16)]
        self.row_weights = [j*25 for j in range(1,26)]

    # get all the possible Left, Right move strings given maximum possible moves
    def getPossibleMoves(self,lefts,rights,extra_moves,initial=''):
        pos_l_pos = []
        i=1
        while i<=lefts:
            pos_l_pos.append(extra_moves+initial+('b'*i))
            i = i+1

        pos_r_pos = []
        j=1
        while j<=rights:
            pos_r_pos.append(extra_moves+initial+('m'*j))
            j = j+1
        pos_l_pos.reverse()
        total_possible_moves = pos_l_pos+[''] +pos_r_pos

        return total_possible_moves

    def getUtilityValueOfMoves(self,successor,quintris):
        cur_board = quintris.get_board()
        cur_score = quintris.state[1]
        quintris_to_play = copy.deepcopy(quintris)

        for move in successor:
            if move == 'b':
                quintris_to_play.left()
            elif move == 'n':
                quintris_to_play.rotate()
            elif move == 'h':
                quintris_to_play.hflip()
            elif move == 'm':
                quintris_to_play.right() 
        quintris_to_play.down()

        new_score = quintris_to_play.state[1]

        new_board = quintris_to_play.get_board()
        new_piece_loc = []

        #get the changed board rows
        for i in range(len(cur_board)):
            if cur_board[i]!=new_board[i]:
                for j in range(len(cur_board[0])):
                    if new_board[i][j] == 'x' and cur_board[i][j] == ' ':
                        new_piece_loc.append([i,j])

        # print(new_piece_loc)
        c = 0
        #add weights for the corresponding indices
        for i in new_piece_loc:
            c = c + self.col_weights[i[1]]+self.row_weights[i[0]]

        if new_score > cur_score:
            c = c*1000
        return c

    # def getGaps(move_str):
    #     if(re.findall('/[x]* +[x]*/',move_str)):
    #         return True
        
    def get_moves(self, quintris):
        # super simple current algorithm: just randomly move left, right, and rotate a few times

        dummy_quintris = quintris
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
    
        # Step1: Get all possible configurations 
        # possible_config = ['','n','nn','nnn','h']
        pos_config_pieces = [[] for _ in range(5)]
        possible_moves = [[] for _ in range(5)]
        
        # to handle the piece cnfigurations if piece is towards right or left and all rotations/flips are not possible
        extra_moves=''
        max_l_w = max(len(cur_p[0]),len(cur_p))
        if max_l_w > (14-y_c):
          extra_moves='b'*max_l_w

        elif max_l_w > (y_c-0):
          extra_moves='m'*max_l_w

        if(extra_moves!=''):
            if(extra_moves.find('b')!=-1):
                i = len(extra_moves)
                while i!=0:
                    dummy_quintris.left()
                    i = i-1
            elif(extra_moves.find('m')!=-1):
                i = len(extra_moves)
                while i!=0:
                    dummy_quintris.right()
                    i = i-1
        # print(dummy_quintris.get_piece())
        # '' given piece as is case
        pos_config_pieces[0] = cur_p
        piece_len = len(cur_p[0])
        lefts = y_c - 0
        rights = 14 - (y_c + piece_len - 1)
        possible_moves[0]= self.getPossibleMoves(lefts,rights,extra_moves) 

        # 'h' case
        dummy_quintris.hflip()
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
        if(cur_p!=pos_config_pieces[0]):
            pos_config_pieces[4] = cur_p
            piece_len = len(cur_p[0])
            
            lefts = y_c - 0
            rights = 14 - (y_c + piece_len - 1)
            possible_moves[4] = self.getPossibleMoves(lefts,rights,extra_moves,'h')
            dummy_quintris.hflip()

        # 'n' case
        dummy_quintris.rotate()
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
        if(cur_p!=pos_config_pieces[0]):
            pos_config_pieces[1] = cur_p
            piece_len = len(cur_p[0])
        
            lefts = y_c - 0
            rights = 14 - (y_c + piece_len - 1)
            possible_moves[1] = self.getPossibleMoves(lefts,rights,extra_moves,'n')

        # 'nn' case
        dummy_quintris.rotate()
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
        if(cur_p!=pos_config_pieces[0]):
            pos_config_pieces[2] = cur_p
            piece_len = len(cur_p[0])
            
            lefts = y_c - 0
            rights = 14 - (y_c + piece_len - 1)
            possible_moves[2] = self.getPossibleMoves(lefts,rights,extra_moves,'nn')

        # 'nnn' case
        dummy_quintris.rotate()
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
        if(cur_p!=pos_config_pieces[1] and cur_p!=pos_config_pieces[0]):
            pos_config_pieces[3] = cur_p
            piece_len = len(cur_p[0])
        
            lefts = y_c - 0
            rights = 14 - (y_c + piece_len - 1)
            possible_moves[3] = self.getPossibleMoves(lefts,rights,extra_moves,'nnn')
            
        dummy_quintris.rotate()
        # print(pos_config_pieces)
        # print(possible_moves)

        # Step 2: Build max_player tree for each configuration 
        max_cost_piece = [[] for _ in range(5)]
        max_cost = [0 for _ in range(5)]
        
        for i in range(len(possible_moves)):
            max_c = 0
            # print(i)
            for j in possible_moves[i]:
                # print(j)
                c = self.getUtilityValueOfMoves(j,quintris)
                # print('c - ',c,' max_c - ',max_c)
                if( c > max_c):
                    max_cost_piece[i] = j
                    max_cost[i] = c
                    max_c = c

        # Step 3: Get the max value from the set 

        return max_cost_piece[max_cost.index(max(max_cost))]
       
    # This is the version that's used by the animted version. This is really similar to get_moves,
    # except that it runs as a separate thread and you should access various methods and data in
    # the "quintris" object to control the movement. In particular:
    #   - quintris.col, quintris.row have the current column and row of the upper-left corner of the 
    #     falling piece
    #   - quintris.get_piece() is the current piece, quintris.get_next_piece() is the next piece after that
    #   - quintris.left(), quintris.right(), quintris.down(), and quintris.rotate() can be called to actually
    #     issue game commands
    #   - quintris.get_board() returns the current state of the board, as a list of strings.
    #
    def control_game(self, quintris):
        # another super simple algorithm: just move piece to the least-full column
        while 1:
            time.sleep(0.1)
            final_move = self.get_moves(quintris)
            for move in final_move:
                if move == 'b':
                    quintris.left()
                elif move == 'n':
                    quintris.rotate()
                elif move == 'h':
                    quintris.hflip()
                elif move == 'm':
                    quintris.right()
            quintris.down()

###################
#### main program

(player_opt, interface_opt) = sys.argv[1:3]

try:
    if player_opt == "human":
        player = HumanPlayer()
    elif player_opt == "computer":
        player = ComputerPlayer()
    else:
        print("unknown player!")

    if interface_opt == "simple":
        quintris = SimpleQuintris()
    elif interface_opt == "animated":
        quintris = AnimatedQuintris()
    else:
        print("unknown interface!")

    quintris.start_game(player)

except EndOfGame as s:
    print("\n\n\n", s)

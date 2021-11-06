# Simple quintris program! v0.2
# D. Crandall, Sept 2021

from AnimatedQuintris import *
from SimpleQuintris import *
from kbinput import *
import time, sys

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

    def getPossibleMoves(self,lefts,rights,initial=''):
        pos_l_pos = []
        i=1
        while i<=lefts:
            pos_l_pos.append(initial+('b'*i))
            i = i+1

        pos_r_pos = []
        j=1
        while j<=rights:
            pos_r_pos.append(initial+('m'*j))
            j = j+1
        pos_l_pos.reverse()
        total_possible_moves = pos_l_pos+[''] +pos_r_pos

        return total_possible_moves

    def get_moves(self, quintris):
        # super simple current algorithm: just randomly move left, right, and rotate a few times

        dummy_quintris = quintris
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
    
        # Step1: Get all possible configurations 
        pos_config = [{'c':[],'moves':[],'optimal_move':{'cost' : 0,'move' :''}},{'n':[],'moves':[],'optimal_move':{'cost' : 0,'move' :''}},{'nn':[],'moves':[],'optimal_move':{'cost' : 0,'move' :''}},{'nnn':[],'moves':[],'optimal_move':{'cost' : 0,'move' :''}},{'h':[],'moves':[],'optimal_move':{'cost' : 0,'move' :''}}]
        # initial_board = quintris.get_board()

        # 'c' case
        pos_config[0]['c'] = cur_p
        piece_len = len(cur_p[0])
        lefts = y_c - 0
        rights = 14 - (y_c + piece_len - 1)
        pos_config[0]['moves'] = self.getPossibleMoves(lefts,rights) 
        pos_config[0]['optimal_move']['cost'] = piece_len*10

        # 'h' case
        dummy_quintris.hflip()
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
        if(cur_p!=pos_config[0]['c']):
            pos_config[4]['h'] = cur_p
            piece_len = len(cur_p[0])
            
            lefts = y_c - 0
            rights = 14 - (y_c + piece_len - 1)
            pos_config[4]['moves'] = self.getPossibleMoves(lefts,rights,'h')
            pos_config[4]['optimal_move']['cost'] = piece_len*10
            dummy_quintris.hflip()

        # 'n' case
        dummy_quintris.rotate()
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
        if(cur_p!=pos_config[0]['c']):
            pos_config[1]['n'] = cur_p
            piece_len = len(cur_p[0])
        
            lefts = y_c - 0
            rights = 14 - (y_c + piece_len - 1)
            pos_config[1]['moves'] = self.getPossibleMoves(lefts,rights,'n')
            pos_config[1]['optimal_move']['cost'] = piece_len*10

        # 'nn' case
        dummy_quintris.rotate()
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
        if(cur_p!=pos_config[0]['c']):
            
            pos_config[2]['nn'] = cur_p
            piece_len = len(cur_p[0])
            
            lefts = y_c - 0
            rights = 14 - (y_c + piece_len - 1)
            pos_config[2]['moves'] = self.getPossibleMoves(lefts,rights,'nn')
            pos_config[2]['optimal_move']['cost'] = piece_len*10

        # 'nnn' case
        dummy_quintris.rotate()
        (cur_p,x_c,y_c) = dummy_quintris.get_piece()
        if(cur_p!=pos_config[1]['n'] and cur_p!=pos_config[0]['c']):
            
            pos_config[3]['nnn'] = cur_p
            piece_len = len(cur_p[0])
        
            lefts = y_c - 0
            rights = 14 - (y_c + piece_len - 1)
            pos_config[3]['moves'] = self.getPossibleMoves(lefts,rights,'nnn')
            pos_config[3]['optimal_move']['cost'] = piece_len*10
        dummy_quintris.rotate()
        
        # Step 2: Build max_player tree for each configuration 
        # Step 3: Get the max value from the set 

        return random.choice(pos_config[random.randint(0, 4)]['moves']) or 'll'
       
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

            board = quintris.get_board()
            column_heights = [ min([ r for r in range(len(board)-1, 0, -1) if board[r][c] == "x"  ] + [100,] ) for c in range(0, len(board[0]) ) ]
            index = column_heights.index(max(column_heights))

            if(index < quintris.col):
                quintris.left()
            elif(index > quintris.col):
                quintris.right()
            else:
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

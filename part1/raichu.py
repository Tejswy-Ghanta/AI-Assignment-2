#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import math
import copy

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def convertToMatrix(board,k):
    temp = [board[idx: idx + k] for idx in range(0, len(board), k)]
    res = [list(ele) for ele in temp]
    return res

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def convert_liststr_to_str(x):
    sentence = ""
    for i in x:
        sentence += str(i)
    return sentence

# def ip_to_singlelist(l):



def pichu_successors(board, N, player):
    # print(board,'$$$$$$$$$$$$')
    possible_successors=[]
    if player=='w':
        for row in range(N):
            for col in range(N):       

                if board[row][col]=='w':
                    if row<(N-1) and col<(N-1) : #forward left diagonal 
                        if board[row+1][col+1]=='.':                           
                            t = copy.deepcopy(board)
                            t[row+1][col+1]='w'
                            t[row][col]='.'  
                            possible_successors.append(t)                                                  

                    if row<(N-1) and  col>1: #Forward jump right               
                        if board[row+1][col-1]=='b': 
                            t = copy.deepcopy(board)
                            t[row+1][col-1]='.'
                            t[row][col]='.'
                            t[row+2][col-2]='w'     
                            possible_successors.append(t)  
                                               

                    if row<(N-1) and col>0: #Forward right diagonal           
                        if board[row+1][col-1]=='.':
                            t = copy.deepcopy(board)
                            t[row+1][col-1]='w'
                            t[row][col]='.'
                            possible_successors.append(t)                           
                       
                    if  row<(N-1)  and col<(N-1): #Forward left jump
                        if board[row+1][col+1]=='b':
                            t = copy.deepcopy(board)
                            t[row+1][col+1]='.'
                            t[row][col]='.'
                            t[row+2][col+2]='w'
                            possible_successors.append(t) 
                            

    else:
        for row in range(N):
            for col in range(N):               
                if board[row][col]=='b':
                    

                    if row<(N-1) and row>0 and col<(N-1) and col>0: #forward left diagonal 
                        if board[row-1][col-1]=='.':
                            t = copy.deepcopy(board)
                            t[row-1][col-1]='b'
                            t[row][col]='.'  
                            possible_successors.append(t)    
                                                 

                    if row>1 and  col>1: #Forward jump left                
                        if board[row-1][col-1]=='w':                             
                            t = copy.deepcopy(board)
                            t[row-1][col-1]='.'
                            t[row][col]='.'
                            t[row-2][col-2]='b'     
                            possible_successors.append(t)                      

                    if row>0 and col<(N)-1: #Forward right diagonal                     
                        if board[row-1][col+1]=='.':
                            t = copy.deepcopy(board)
                            t[row-1][col+1]='b'
                            t[row][col]='.'
                            possible_successors.append(t)
                       
                    if  row>1  and col<N-2: #Forward right jump
                        if board[row-1][col+1]=='w':
                            t = copy.deepcopy(board)
                            t[row-1][col+1]='.'
                            t[row][col]='.'
                            t[row-2][col+2]='b'
                            possible_successors.append(t)
    

    return possible_successors

def pikachu_successors(board, N, player):
    # print(board,'!!!!')
    possible_successors=[]
    if player=='b':
        for row in range(N):
            for col in range(N):
                if board[row][col]=='B':

                    if  row>0 : # one forward
                        if board[row-1][col]=='.': 
                            t = copy.deepcopy(board)
                            t[row-1][col]='B'
                            t[row][col]='.'
                            possible_successors.append(t)

                    if  row>1 : # two forward
                        if board[row-2][col]=='.' and board[row-1][col]=='.': 
                            t = copy.deepcopy(board)
                            t[row-2][col]='B'
                            t[row][col]='.'
                            possible_successors.append(t)                            

                    if  col>0 : # one left     
                        if board[row][col-1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col-1]='B'
                            t[row][col]='.'
                            possible_successors.append(t)

                    if  col>1 : # two left     
                        if board[row][col-2]=='.' and board[row][col-1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col-2]='B'
                            t[row][col]='.'
                            possible_successors.append(t)
                            # print(possible_successors,'!!!!')

                    if  col<(N-1) : # one right  
                        if board[row][col+1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col+1]='B'
                            t[row][col]='.'
                            possible_successors.append(t)

                    if  col<(N-2) : # two right    
                        if board[row][col+2]=='.' and board[row][col+1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col+2]='B'
                            t[row][col]='.'
                            possible_successors.append(t)

                    if  row>1 :
                        if board[row-1][col]=='W' and board[row-2][col]=='.': #Jump one forward pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-1][col]='.'
                            t[row-2][col]='B'
                            possible_successors.append(t)

                    if  row>2 :
                        if board[row-1][col]=='.' and board[row-2][col]=='W' and board[row-3][col]=='.': #Jump two forward pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-2][col]='.'
                            t[row-3][col]='B'
                            possible_successors.append(t)
                           
                    if  col>1 :
                        if board[row][col-1]=='W' and board[row][col-2]=='.': #Jump one left pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-1]='.'
                            t[row][col-2]='B'
                            possible_successors.append(t)                           

                    if  col>2 :
                        if board[row][col-1]=='.' and board[row][col-2]=='W' and board[row][col-3]=='.': #Jump two left pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-2]='.'
                            t[row][col-3]='B'
                            possible_successors.append(t)
                    
                    if  col<(N-2) :
                        if board[row][col+1]=='W' and board[row][col+2]=='.': #Jump one right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+1]='.'
                            t[row][col+2]='B'
                            possible_successors.append(t)  
                                                    
                    if  col<(N-3) :
                        if board[row][col+1]=='.' and board[row][col+2]=='W' and board[row][col+3]=='.': #Jump two right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+2]='.'
                            t[row][col+3]='B'
                            possible_successors.append(t)
     #---               
                    if  row>1 :
                        if board[row-1][col]=='w' and board[row-2][col]=='.': #Jump one forward pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-1][col]='.'
                            t[row-2][col]='B'
                            possible_successors.append(t)

                    if  row>2 :
                        if board[row-1][col]=='.' and board[row-2][col]=='w' and board[row-3][col]=='.': #Jump two forward pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-2][col]='.'
                            t[row-3][col]='B'
                            possible_successors.append(t)
                           
                    if  col>1 :
                        if board[row][col-1]=='w' and board[row][col-2]=='.': #Jump one left pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-1]='.'
                            t[row][col-2]='B'
                            possible_successors.append(t)                           

                    if  col>2 :
                        if board[row][col-1]=='.' and board[row][col-2]=='w' and board[row][col-3]=='.': #Jump two left pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-2]='.'
                            t[row][col-3]='B'
                            possible_successors.append(t)
                    
                    if  col<(N-2) :
                        if board[row][col+1]=='w' and board[row][col+2]=='.': #Jump one right pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+1]='.'
                            t[row][col+2]='B'
                            possible_successors.append(t)  
                                                    
                    if  col<(N-3) :
                        if board[row][col+1]=='.' and board[row][col+2]=='w' and board[row][col+3]=='.': #Jump two right pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+2]='.'
                            t[row][col+3]='B'
                            possible_successors.append(t)
                            
                            

# #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    else:
        for row in range(N):
            for col in range(N):
                if board[row][col]=='W':                  

                    if  row<(N-1) : # one forward                     
                        if board[row+1][col]=='.': 
                            t = copy.deepcopy(board)
                            t[row+1][col]='W'
                            t[row][col]='.'
                            possible_successors.append(t)
                            
                    if  row<(N-2) : # two forward
                        if board[row+2][col]=='.' and board[row+1][col]=='.': 
                            t = copy.deepcopy(board)
                            t[row+2][col]='W'
                            t[row][col]='.'
                            possible_successors.append(t)                                                    

                    if  col>0 : # one left     
                        if board[row][col-1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col-1]='W'
                            t[row][col]='.'
                            possible_successors.append(t)                  

                    if  col>1 : # two left     
                        if board[row][col-2]=='.' and board[row][col-1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col-2]='W'
                            t[row][col]='.'
                            possible_successors.append(t)                        

                    if  col<(N-1) : # one right  
                        if board[row][col+1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col+1]='W'
                            t[row][col]='.'
                            possible_successors.append(t)
                            
                    if  col<(N-2) : # two right    
                        if board[row][col+2]=='.' and board[row][col+1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col+2]='W'
                            t[row][col]='.'
                            possible_successors.append(t)                           

                    if  row>1 :
                        if board[row-1][col]=='B' and board[row-2][col]=='.': #Jump one forward pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-1][col]='.'
                            t[row-2][col]='W'
                            possible_successors.append(t)

                    if  row>2 :
                        if board[row-1][col]=='.' and board[row-2][col]=='B' and board[row-3][col]=='.': #Jump two forward pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-2][col]='.'
                            t[row-3][col]='W'
                            possible_successors.append(t)
                           
                    if  col>1 :
                        if board[row][col-1]=='B' and board[row][col-2]=='.': #Jump one left pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-1]='.'
                            t[row][col-2]='W'
                            possible_successors.append(t)                                                    

                    if  col>2 :
                        if board[row][col-1]=='.' and board[row][col-2]=='B' and board[row][col-3]=='.': #Jump two left pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-2]='.'
                            t[row][col-3]='W'
                            possible_successors.append(t)                    
                    
                    if  col<(N-2) :
                        if board[row][col+1]=='B' and board[row][col+2]=='.': #Jump one right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+1]='.'
                            t[row][col+2]='W'
                            possible_successors.append(t)                             
                                                    
                    if  col<(N-3) :
                        if board[row][col+1]=='.' and board[row][col+2]=='B' and board[row][col+3]=='.': #Jump two right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+2]='.'
                            t[row][col+3]='W'
                            possible_successors.append(t)

                            #----
                    if  row>1 :
                        if board[row-1][col]=='b' and board[row-2][col]=='.': #Jump one forward pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-1][col]='.'
                            t[row-2][col]='W'
                            possible_successors.append(t)

                    if  row>2 :
                        if board[row-1][col]=='.' and board[row-2][col]=='b' and board[row-3][col]=='.': #Jump two forward pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-2][col]='.'
                            t[row-3][col]='W'
                            possible_successors.append(t)
                           
                    if  col>1 :
                        if board[row][col-1]=='b' and board[row][col-2]=='.': #Jump one left pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-1]='.'
                            t[row][col-2]='W'
                            possible_successors.append(t)                                                    

                    if  col>2 :
                        if board[row][col-1]=='.' and board[row][col-2]=='b' and board[row][col-3]=='.': #Jump two left pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-2]='.'
                            t[row][col-3]='W'
                            possible_successors.append(t)                    
                    
                    if  col<(N-2) :
                        if board[row][col+1]=='b' and board[row][col+2]=='.': #Jump one right pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+1]='.'
                            t[row][col+2]='W'
                            possible_successors.append(t)                             
                                                    
                    if  col<(N-3) :
                        if board[row][col+1]=='.' and board[row][col+2]=='b' and board[row][col+3]=='.': #Jump two right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+2]='.'
                            t[row][col+3]='W'
                            possible_successors.append(t)
    
    return possible_successors
                   
def raichu_successors(board, N, player):
    x1=raichu_right(board, N, player)
    x2=raichu_left(board, N, player)
    x3=raichu_up(board, N, player)
    x4=raichu_down(board, N, player)
    x=x1+x2+x3+x4
    return x

                   
def raichu_right(board, N, player):
    possible_successors=[]
    x=True
    pos=0
    if player=='w':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                if board[row][col]=='@':
                    # print(row,col)
                    pos=col
                    for i in range(col+1,N,1):
                        if board[row][i]=='.' and i<N and (board[row][i-1] not in 'WBbw$') and x==True and i-1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[row][i]='.','@'
                            pos=i
                            possible_successors.append(t)                          
                        
                        if t[row][i] in 'bB$' and i<N-1 and t[row][i+1]=='.' and x==True and i-1==pos :
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i+1],t[row][i-1]='.','@','.'
                            pos=i+1
                            x=False
                            i=i+1
                            possible_successors.append(t)
                        
                        # if i<(N-2) and t[row][i+2]=='.' and t[row][i+1] not in 'B$b' and x==False and t[row][i]not in '@':
                        if i<(N-1) and t[row][i]=='@' and t[row][i+1]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i+1]='.','@'
                            pos=i+1
                            possible_successors.append(t)
            # # break
    elif player=='b':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                if board[row][col]=='$':
                    pos=col
                    for i in range(col+1,N,1):
                        if board[row][i]=='.' and i<N and (board[row][i-1] not in 'WwbB$') and x==True and i-1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[row][i]='.','$'
                            pos=i
                            possible_successors.append(t)                           
                        
                        if t[row][i] in 'wW@' and i<N-1 and t[row][i+1]=='.' and x==True and i-1==pos :
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i+1],t[row][i-1]='.','$','.'
                            pos=i+1
                            x=False
                            i=i+1
                            possible_successors.append(t)
                        
                        # if i<(N-2) and t[row][i+2]=='.' and t[row][i+1] not in 'B$b' and x==False and t[row][i]not in '@':
                        if i<(N-1) and t[row][i]=='$' and t[row][i+1]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i+1]='.','$'
                            pos=i+1
                            possible_successors.append(t)  

    return possible_successors


def raichu_left(board, N, player):
    # print(board,'!!!!!!!!!!!')
    possible_successors=[]
    x=True
    pos=0
    if player=='w':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                
                if board[row][col]=='@':
                    # print(row,col)
                    pos=col
                    for i in range(col-1,-1,-1):
                        # print('***')
                        if board[row][i]=='.' and i>-1 and (board[row][i+1] not in 'WBbw$') and x==True and i+1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[row][i]='.','@'
                            pos=i
                            possible_successors.append(t)                          
                        
                        if t[row][i] in 'bB$' and i>0 and t[row][i-1]=='.' and x==True and i+1==pos :
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i-1],t[row][i+1]='.','@','.'
                            pos=i-1
                            x=False
                            i=i-1
                            possible_successors.append(t)
                        
                        if i>0 and t[row][i]=='@' and t[row][i-1]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i-1]='.','@'
                            pos=i-1
                            possible_successors.append(t)
            # break

    elif player=='b':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                
                if board[row][col]=='$':
                    # print(row,col)
                    pos=col
                    for i in range(col-1,-1,-1):
                        # print('***')
                        if board[row][i]=='.' and i>-1 and (board[row][i+1] not in 'WBbw@') and x==True and i+1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[row][i]='.','$'
                            pos=i
                            possible_successors.append(t)                          
                        
                        if t[row][i] in 'wW@' and i>0 and t[row][i-1]=='.' and x==True and i+1==pos :
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i-1],t[row][i+1]='.','$','.'
                            pos=i-1
                            x=False
                            i=i-1
                            possible_successors.append(t)
                        
                        if i>0 and t[row][i]=='$' and t[row][i-1]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i-1]='.','$'
                            pos=i-1
                            possible_successors.append(t)
            # break
    return possible_successors

              
def raichu_down(board, N, player):
    possible_successors=[]
    x=True
    pos=0
    if player=='w':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                if board[row][col]=='@':
                    # print(row,col)
                    pos=row
                    for i in range(row+1,N,1):
                        if board[i][col]=='.' and i<N and (board[i-1][col] not in 'WBbw$') and x==True and i-1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[i][col]='.','@'
                            pos=i
                            possible_successors.append(t)                          
                        
                        if t[i][col] in 'bB$' and i<N-1 and t[i+1][col]=='.' and x==True and i-1==pos :
                            t=copy.deepcopy(t)
                            t[i][col],t[i+1][col],t[i-1][col]='.','@','.'
                            pos=i+1
                            x=False
                            i=i+1
                            possible_successors.append(t)
                        
                        # if i<(N-2) and t[row][i+2]=='.' and t[row][i+1] not in 'B$b' and x==False and t[row][i]not in '@':
                        if i<(N-1) and t[i][col]=='@' and t[i+1][col]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[i][col],t[i+1][col]='.','@'
                            pos=i+1
                            possible_successors.append(t)
            # # break
    elif player=='b':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                if board[row][col]=='$':
                    # print(row,col)
                    pos=row
                    for i in range(row+1,N,1):
                        if board[i][col]=='.' and i<N and (board[i-1][col] not in 'WBbw@') and x==True and i-1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[i][col]='.','$'
                            pos=i
                            possible_successors.append(t)                          
                        
                        if t[i][col] in 'wW@' and i<N-1 and t[i+1][col]=='.' and x==True and i-1==pos :
                            t=copy.deepcopy(t)
                            t[i][col],t[i+1][col],t[i-1][col]='.','$','.'
                            pos=i+1
                            x=False
                            i=i+1
                            possible_successors.append(t)
                        
                        # if i<(N-2) and t[row][i+2]=='.' and t[row][i+1] not in 'B$b' and x==False and t[row][i]not in '@':
                        if i<(N-1) and t[i][col]=='$' and t[i+1][col]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[i][col],t[i+1][col]='.','$'
                            pos=i+1
                            possible_successors.append(t)
            # # break
    return possible_successors


def raichu_up(board, N, player):
    possible_successors=[]
    x=True
    pos=0
    if player=='w':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                if board[row][col]=='@':
                    # print(row,col)
                    pos=row
                    for i in range(row-1,-1,-1):
                        if board[i][col]=='.' and i>-1 and (board[i+1][col] not in 'WBbw$') and x==True and i+1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[i][col]='.','@'
                            pos=i
                            possible_successors.append(t)                          
                        
                        if t[i][col] in 'bB$' and i>0 and t[i-1][col]=='.' and x==True and i+1==pos :
                            t=copy.deepcopy(t)
                            t[i][col],t[i-1][col],t[i+1][col]='.','@','.'
                            pos=i-1
                            x=False
                            i=i-1
                            possible_successors.append(t)
                        
                        # if i<(N-2) and t[row][i+2]=='.' and t[row][i+1] not in 'B$b' and x==False and t[row][i]not in '@':
                        if i>0 and t[i][col]=='@' and t[i-1][col]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[i][col],t[i-1][col]='.','@'
                            pos=i-1
                            possible_successors.append(t)
            # # break
    elif player=='b':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                if board[row][col]=='$':
                    # print(row,col)
                    pos=row
                    for i in range(row-1,-1,-1):
                        if board[i][col]=='.' and i>-1 and (board[i+1][col] not in 'WBbw@') and x==True and i+1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[i][col]='.','$'
                            pos=i
                            possible_successors.append(t)                          
                        
                        if t[i][col] in 'wW@' and i>0 and t[i-1][col]=='.' and x==True and i+1==pos :
                            t=copy.deepcopy(t)
                            t[i][col],t[i-1][col],t[i+1][col]='.','$','.'
                            pos=i-1
                            x=False
                            i=i-1
                            possible_successors.append(t)
                        
                        # if i<(N-2) and t[row][i+2]=='.' and t[row][i+1] not in 'B$b' and x==False and t[row][i]not in '@':
                        if i>0 and t[i][col]=='$' and t[i-1][col]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[i][col],t[i-1][col]='.','$'
                            pos=i-1
                            possible_successors.append(t)
            # # break
    return possible_successors

def all_successors(board,N, player):
    a=[]
    value=[]
    state=[]
    x=convertToMatrix(board, 8)
    y=[]
    a1=pichu_successors(x, N, player)   
    a2=pikachu_successors(x, N, player)
    a3=raichu_successors(x, N, player)
    # a3=raichu_successors(board, N, player)
    a=a1+a2+a3
    

    for i in a:
        i=flatten_list(i)
        # print(i,'!!!!')
        y.append(heuristic(i,player,N))
        
        value.append(heuristic(i,player,N)[0])
        
        
        state.append(heuristic(i,player,N)[1])
    # return [value,state]
    # print(y,'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    return y
    

def heuristic(successor,player,N):
    # print(successor,'######################')
    # print('BOARD',successor)
    c_w,c_W,c_b,c_B,c_wr,c_br,n_w,n_b=0,0,0,0,0,0,0,0
    for i in range(N*N):
        if successor[i] =='w':
            c_w=c_w+1
    for i in range(N*N):
        if successor[i] =='W':
            c_W=c_W+1
    for i in range(N*N):
        if successor[i] =='b':
            c_b=c_b+1
    for i in range(N*N):
        if successor[i] =='B':
            c_B=c_B+1
    for i in range(N*N):
        if successor[i] =='@':
            c_wr=c_wr+1
    for i in range(N*N):
        if successor[i] =='$':
            c_br=c_br+1
    # print(c_w,c_b,'!!!!!!!!!!!!!!!!!!!!')
    if player=='w':
        value=(((c_w-c_b)*250) + ((c_W-c_B)*500) + ((c_wr-c_br)*1000))
    else:
        value=(((c_b-c_w)*250) + ((c_B-c_W)*500) + ((c_br-c_wr)*1000))
    # print('!!',value,successor)
    return [value,successor]
    
# def alphabeta():
#     alpha=9999999
#     beta=-9999999
#     minmax(board,5,alpha,beta,'w',N)

def minimax(current_board,depth,alpha,beta,player):
    
    x=copy.deepcopy(current_board)
    board=convert_liststr_to_str(current_board)
    print(board)
    N=8
    if depth == 0: 
        return heuristic(list(board),'w',8)[0],board
    
    if player=='w': 
        value = -9999999
        for succ in all_successors(board,N,'w'):
            # print(succ[0],'%')
            (maxeval,boards)=minimax(succ[1], (depth-1),alpha,beta,'b')
            value=max(value,maxeval)
            # print('!!!')
            alpha=max(alpha,maxeval)
            if beta <=alpha:
                break
            # print(value,'!!!')
        yield (value,boards)

    elif player =='b':          
        value = 9999999
        # print(board,'^^^^^^^^^^^^^^^^^^^')
        for succ in all_successors(board,8,'b'):
            # print('Enter') 
            (mineval,boards)=minimax(succ[1], (depth-1),alpha,beta,'w')
            value=min(value, mineval)
            # print('$$')
            beta=min(beta,mineval)
            if beta<=alpha:
                break
            # print(value,'@@@')
        yield (value,boards)




 
 
# // initial call
# minimax(currentPosition, 3, -∞, +∞, true)
                                               




# def find_best_move(board, N, player, timelimit):
#     # This sample code just returns the same board over and over again (which
#     # isn't a valid move anyway.) Replace this with your code!
#     #
#     while True:
#         time.sleep(1)
#         yield board


if __name__ == "__main__":
    board='......................w.......$...............B.......@.........'
    # x=['.', 'w', '.', '.', '.', 'w', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'b', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'b', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    #board_new=[char for char in board]
    N=8
    alpha=9999999
    beta=-9999999
    #(value,board) = minimax(board,2,-9999999,99999999,'w')
    # xxy = minimax(board,2,-9999999,99999999,'w')
    for i in minimax(board,2,-9999999,99999999,'w'):
        print(i)
    x=convertToMatrix(board,8)
    print(x,'!!!!!!!')
    # print(len(x),len(x[0]))
    # # print(x,'@@@@')
    # print(raichu_successors(x, 8, 'b'))
    # for i in range(0,8):
    #     for j in range(0,8):
            
    #         if x[i][j]=='@':
    #             print (i,j)











    # print(heuristic(flatten_list(x),'w',8),'******************')
    # print(list(board))




    # print(all_successors(board,N, 'b'))
    # all_successors(board,N, 'w')
    # print(heuristic(board,'w'))


    # convert ['a','b','c','d'] to 'abcd'










    # print(all_successors(board,8,'w'))

    # x=convertToMatrix(board, 8)
    # print(pichu_successors(x, 8, 'b'))
    # print(x,'$$$$$')
    # print(x[6][4])
    # print(x,'^^^^^^^^^^^^^^^^^^^^^^')
    # x=pichu_successors(x, 8, 'w')
    # print(x,'!!!')
    # print(raichu_successors(x, 8, 'w'))
    # if len(sys.argv) != 5:
    #     raise Exception("Usage: Raichu.py N player board timelimit")
        
    # (_, N, player, board, timelimit) = sys.argv
    # N=int(N)
    # timelimit=int(timelimit)
    # if player not in "wb":
    #     raise Exception("Invalid player.")

    # if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
    #     raise Exception("Bad board string.")

    # print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    # print("Here's what I decided:")
    # for new_board in find_best_move(board, N, player, timelimit):
    #     print(new_board)

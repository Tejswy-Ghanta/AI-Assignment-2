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
import heapq

#The below four functionsa are extra functions I have used to to convert board arrangements
def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def convertToMatrix(board,k):
    temp = [board[idx: idx + k] for idx in range(0, len(board), k)]
    res = [list(ele) for ele in temp]
    return res

def flatten_list(_2d_list):
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
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

def convert_raichu(x,N):
    for row in range (N):
        for col in range(N):
            if x[N-1][col] in 'wW':
                x[N-1][col]='@'
            if x[0][col] in 'bB':
                x[0][col]='$'
    return x


# Calculate Successors of pichus
def pichu_successors(board, N, player):
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
                            convert_raichu(t,N)
                            possible_successors.append(t)                                                  

                    if row<(N-1) and  col>1: #Forward jump right               
                        if board[row+1][col-1]=='b': 
                            t = copy.deepcopy(board)
                            t[row+1][col-1]='.'
                            t[row][col]='.'
                            t[row+2][col-2]='w'  
                            convert_raichu(t,N)   
                            possible_successors.append(t)                                                 

                    if row<(N-1) and col>0: #Forward right diagonal           
                        if board[row+1][col-1]=='.':
                            t = copy.deepcopy(board)
                            t[row+1][col-1]='w'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)                           
                       
                    if  row<(N-1)  and col<(N-1): #Forward left jump
                        if board[row+1][col+1]=='b':
                            t = copy.deepcopy(board)
                            t[row+1][col+1]='.'
                            t[row][col]='.'
                            t[row+2][col+2]='w'     ##############
                            convert_raichu(t,N)
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
                            convert_raichu(t,N)
                            possible_successors.append(t)    
                                                 
                    if row>1 and  col>1: #Forward jump left                
                        if board[row-1][col-1]=='w':                             
                            t = copy.deepcopy(board)
                            t[row-1][col-1]='.'
                            t[row][col]='.'
                            t[row-2][col-2]='b'   
                            convert_raichu(t,N)  
                            possible_successors.append(t)                      

                    if row>0 and col<(N)-1: #Forward right diagonal                     
                        if board[row-1][col+1]=='.':
                            t = copy.deepcopy(board)
                            t[row-1][col+1]='b'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                       
                    if  row>1  and col<N-2: #Forward right jump
                        if board[row-1][col+1]=='w':
                            t = copy.deepcopy(board)
                            t[row-1][col+1]='.'
                            t[row][col]='.'
                            t[row-2][col+2]='b'
                            convert_raichu(t,N)
                            possible_successors.append(t)    

    return possible_successors

#Returns all the successors of Pikachus
def pikachu_successors(board, N, player):
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
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  row>1 : # two forward
                        if board[row-2][col]=='.' and board[row-1][col]=='.': 
                            t = copy.deepcopy(board)
                            t[row-2][col]='B'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)                            

                    if  col>0 : # one left     
                        if board[row][col-1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col-1]='B'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  col>1 : # two left     
                        if board[row][col-2]=='.' and board[row][col-1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col-2]='B'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  col<(N-1) : # one right  
                        if board[row][col+1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col+1]='B'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  col<(N-2) : # two right    
                        if board[row][col+2]=='.' and board[row][col+1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col+2]='B'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  row>1 :
                        if board[row-1][col]=='W' and board[row-2][col]=='.': #Jump one forward pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-1][col]='.'
                            t[row-2][col]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  row>2 :
                        if board[row-1][col]=='.' and board[row-2][col]=='W' and board[row-3][col]=='.': #Jump two forward pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-2][col]='.'
                            t[row-3][col]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                           
                    if  col>1 :
                        if board[row][col-1]=='W' and board[row][col-2]=='.': #Jump one left pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-1]='.'
                            t[row][col-2]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)                           

                    if  col>2 :
                        if board[row][col-1]=='.' and board[row][col-2]=='W' and board[row][col-3]=='.': #Jump two left pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-2]='.'
                            t[row][col-3]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                    
                    if  col<(N-2) :
                        if board[row][col+1]=='W' and board[row][col+2]=='.': #Jump one right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+1]='.'
                            t[row][col+2]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)  
                                                    
                    if  col<(N-3) :
                        if board[row][col+1]=='.' and board[row][col+2]=='W' and board[row][col+3]=='.': #Jump two right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+2]='.'
                            t[row][col+3]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)
            
                    if  row>1 :
                        if board[row-1][col]=='w' and board[row-2][col]=='.': #Jump one forward pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-1][col]='.'
                            t[row-2][col]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  row>2 :
                        if board[row-1][col]=='.' and board[row-2][col]=='w' and board[row-3][col]=='.': #Jump two forward pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-2][col]='.'
                            t[row-3][col]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                           
                    if  col>1 :
                        if board[row][col-1]=='w' and board[row][col-2]=='.': #Jump one left pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-1]='.'
                            t[row][col-2]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)                           

                    if  col>2 :
                        if board[row][col-1]=='.' and board[row][col-2]=='w' and board[row][col-3]=='.': #Jump two left pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-2]='.'
                            t[row][col-3]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                    
                    if  col<(N-2) :
                        if board[row][col+1]=='w' and board[row][col+2]=='.': #Jump one right pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+1]='.'
                            t[row][col+2]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)  
                                                    
                    if  col<(N-3) :
                        if board[row][col+1]=='.' and board[row][col+2]=='w' and board[row][col+3]=='.': #Jump two right pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+2]='.'
                            t[row][col+3]='B'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                            
                            
    else:
        for row in range(N):
            for col in range(N):
                if board[row][col]=='W':                  

                    if  row<(N-1) : # one forward                     
                        if board[row+1][col]=='.': 
                            t = copy.deepcopy(board)
                            t[row+1][col]='W'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                            
                    if  row<(N-2) : # two forward
                        if board[row+2][col]=='.' and board[row+1][col]=='.': 
                            t = copy.deepcopy(board)
                            t[row+2][col]='W'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)                                                    

                    if  col>0 : # one left     
                        if board[row][col-1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col-1]='W'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)                  

                    if  col>1 : # two left     
                        if board[row][col-2]=='.' and board[row][col-1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col-2]='W'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)                        

                    if  col<(N-1) : # one right  
                        if board[row][col+1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col+1]='W'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                            
                    if  col<(N-2) : # two right    
                        if board[row][col+2]=='.' and board[row][col+1]=='.': 
                            t = copy.deepcopy(board)
                            t[row][col+2]='W'
                            t[row][col]='.'
                            convert_raichu(t,N)
                            possible_successors.append(t)                           

                    if  row>1 :
                        if board[row-1][col]=='B' and board[row-2][col]=='.': #Jump one forward pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-1][col]='.'
                            t[row-2][col]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  row>2 :
                        if board[row-1][col]=='.' and board[row-2][col]=='B' and board[row-3][col]=='.': #Jump two forward pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-2][col]='.'
                            t[row-3][col]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                           
                    if  col>1 :
                        if board[row][col-1]=='B' and board[row][col-2]=='.': #Jump one left pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-1]='.'
                            t[row][col-2]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)                                                    

                    if  col>2 :
                        if board[row][col-1]=='.' and board[row][col-2]=='B' and board[row][col-3]=='.': #Jump two left pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-2]='.'
                            t[row][col-3]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)                    
                    
                    if  col<(N-2) :
                        if board[row][col+1]=='B' and board[row][col+2]=='.': #Jump one right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+1]='.'
                            t[row][col+2]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)                             
                                                    
                    if  col<(N-3) :
                        if board[row][col+1]=='.' and board[row][col+2]=='B' and board[row][col+3]=='.': #Jump two right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+2]='.'
                            t[row][col+3]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  row>1 :
                        if board[row-1][col]=='b' and board[row-2][col]=='.': #Jump one forward pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-1][col]='.'
                            t[row-2][col]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)

                    if  row>2 :
                        if board[row-1][col]=='.' and board[row-2][col]=='b' and board[row-3][col]=='.': #Jump two forward pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row-2][col]='.'
                            t[row-3][col]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)
                           
                    if  col>1 :
                        if board[row][col-1]=='b' and board[row][col-2]=='.': #Jump one left pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-1]='.'
                            t[row][col-2]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)                                                    

                    if  col>2 :
                        if board[row][col-1]=='.' and board[row][col-2]=='b' and board[row][col-3]=='.': #Jump two left pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col-2]='.'
                            t[row][col-3]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)                    
                    
                    if  col<(N-2) :
                        if board[row][col+1]=='b' and board[row][col+2]=='.': #Jump one right pichu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+1]='.'
                            t[row][col+2]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)                             
                                                    
                    if  col<(N-3) :
                        if board[row][col+1]=='.' and board[row][col+2]=='b' and board[row][col+3]=='.': #Jump two right pikachu
                            t = copy.deepcopy(board)
                            t[row][col]='.'
                            t[row][col+2]='.'
                            t[row][col+3]='W'
                            convert_raichu(t,N)
                            possible_successors.append(t)
    
    return possible_successors

#Returns all the successors of Raichus   
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
                    pos=col
                    for i in range(col+1,N,1):
                        if board[row][i]=='.' and i<N and (board[row][i-1] not in 'WBbw$') and x==True and i-1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[row][i]='.','@'
                            pos=i
                            convert_raichu(t,N)
                            possible_successors.append(t)                          
                        
                        if t[row][i] in 'bB$' and i<N-1 and t[row][i+1]=='.' and x==True and i-1==pos :
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i+1],t[row][i-1]='.','@','.'
                            pos=i+1
                            x=False
                            i=i+1
                            convert_raichu(t,N)
                            possible_successors.append(t)
                        
                        if i<(N-1) and t[row][i]=='@' and t[row][i+1]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i+1]='.','@'
                            pos=i+1
                            convert_raichu(t,N)
                            possible_successors.append(t)

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
                            convert_raichu(t,N)
                            possible_successors.append(t)                           
                        
                        if t[row][i] in 'wW@' and i<N-1 and t[row][i+1]=='.' and x==True and i-1==pos :
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i+1],t[row][i-1]='.','$','.'
                            pos=i+1
                            x=False
                            i=i+1
                            convert_raichu(t,N)
                            possible_successors.append(t)
                        
                        if i<(N-1) and t[row][i]=='$' and t[row][i+1]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i+1]='.','$'
                            pos=i+1
                            convert_raichu(t,N)
                            possible_successors.append(t)  

    return possible_successors


def raichu_left(board, N, player):
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
                    pos=col
                    for i in range(col-1,-1,-1):
                        if board[row][i]=='.' and i>-1 and (board[row][i+1] not in 'WBbw$') and x==True and i+1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[row][i]='.','@'
                            pos=i
                            convert_raichu(t,N)
                            possible_successors.append(t)                          
                        
                        if t[row][i] in 'bB$' and i>0 and t[row][i-1]=='.' and x==True and i+1==pos :
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i-1],t[row][i+1]='.','@','.'
                            pos=i-1
                            x=False
                            i=i-1
                            convert_raichu(t,N)
                            possible_successors.append(t)
                        
                        if i>0 and t[row][i]=='@' and t[row][i-1]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i-1]='.','@'
                            pos=i-1
                            convert_raichu(t,N)
                            possible_successors.append(t)

    elif player=='b':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)               
                if board[row][col]=='$':
                    pos=col
                    for i in range(col-1,-1,-1):
                        if board[row][i]=='.' and i>-1 and (board[row][i+1] not in 'WBbw@') and x==True and i+1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[row][i]='.','$'
                            pos=i
                            convert_raichu(t,N)
                            possible_successors.append(t)                          
                        
                        if t[row][i] in 'wW@' and i>0 and t[row][i-1]=='.' and x==True and i+1==pos :
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i-1],t[row][i+1]='.','$','.'
                            pos=i-1
                            x=False
                            i=i-1
                            convert_raichu(t,N)
                            possible_successors.append(t)
                        
                        if i>0 and t[row][i]=='$' and t[row][i-1]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[row][i],t[row][i-1]='.','$'
                            pos=i-1
                            convert_raichu(t,N)
                            possible_successors.append(t)
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
                    pos=row
                    for i in range(row+1,N,1):
                        if board[i][col]=='.' and i<N and (board[i-1][col] not in 'WBbw$') and x==True and i-1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[i][col]='.','@'
                            pos=i
                            convert_raichu(t,N)
                            possible_successors.append(t)                          
                        
                        if t[i][col] in 'bB$' and i<N-1 and t[i+1][col]=='.' and x==True and i-1==pos :
                            t=copy.deepcopy(t)
                            t[i][col],t[i+1][col],t[i-1][col]='.','@','.'
                            pos=i+1
                            x=False
                            i=i+1
                            convert_raichu(t,N)
                            possible_successors.append(t)
                        
                        if i<(N-1) and t[i][col]=='@' and t[i+1][col]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[i][col],t[i+1][col]='.','@'
                            pos=i+1
                            convert_raichu(t,N)
                            possible_successors.append(t)

    elif player=='b':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                if board[row][col]=='$':
                    pos=row
                    for i in range(row+1,N,1):
                        if board[i][col]=='.' and i<N and (board[i-1][col] not in 'WBbw@') and x==True and i-1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[i][col]='.','$'
                            pos=i
                            convert_raichu(t,N)
                            possible_successors.append(t)                          
                        
                        if t[i][col] in 'wW@' and i<N-1 and t[i+1][col]=='.' and x==True and i-1==pos :
                            t=copy.deepcopy(t)
                            t[i][col],t[i+1][col],t[i-1][col]='.','$','.'
                            pos=i+1
                            x=False
                            i=i+1
                            convert_raichu(t,N)
                            possible_successors.append(t)
        
                        if i<(N-1) and t[i][col]=='$' and t[i+1][col]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[i][col],t[i+1][col]='.','$'
                            pos=i+1
                            convert_raichu(t,N)
                            possible_successors.append(t)

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
                    pos=row
                    for i in range(row-1,-1,-1):
                        if board[i][col]=='.' and i>-1 and (board[i+1][col] not in 'WBbw$') and x==True and i+1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[i][col]='.','@'
                            pos=i
                            convert_raichu(t,N)
                            possible_successors.append(t)                          
                        
                        if t[i][col] in 'bB$' and i>0 and t[i-1][col]=='.' and x==True and i+1==pos :
                            t=copy.deepcopy(t)
                            t[i][col],t[i-1][col],t[i+1][col]='.','@','.'
                            pos=i-1
                            x=False
                            i=i-1
                            convert_raichu(t,N)
                            possible_successors.append(t)
                        
                        if i>0 and t[i][col]=='@' and t[i-1][col]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[i][col],t[i-1][col]='.','@'
                            pos=i-1
                            convert_raichu(t,N)
                            possible_successors.append(t)

    elif player=='b':
        t=copy.deepcopy(board)
        for row in range(N):
            for col in range(N):
                x=True
                t=copy.deepcopy(board)
                if board[row][col]=='$':
                    pos=row
                    for i in range(row-1,-1,-1):
                        if board[i][col]=='.' and i>-1 and (board[i+1][col] not in 'WBbw@') and x==True and i+1==pos:
                            t=copy.deepcopy(board)
                            t[row][col],t[i][col]='.','$'
                            pos=i
                            convert_raichu(t,N)
                            possible_successors.append(t)                          
                        
                        if t[i][col] in 'wW@' and i>0 and t[i-1][col]=='.' and x==True and i+1==pos :
                            t=copy.deepcopy(t)
                            t[i][col],t[i-1][col],t[i+1][col]='.','$','.'
                            pos=i-1
                            x=False
                            i=i-1
                            convert_raichu(t,N)
                            possible_successors.append(t)
        
                        if i>0 and t[i][col]=='$' and t[i-1][col]=='.' and x==False and pos==i:
                            t=copy.deepcopy(t)
                            t[i][col],t[i-1][col]='.','$'
                            pos=i-1
                            convert_raichu(t,N)
                            possible_successors.append(t)

    return possible_successors

#This function returns the list of all possible suiccessors of the given board
def all_successors(board,N, player):
    a=[]
    value=[]
    state=[]
    x=convertToMatrix(board, N)
    y=[]
    a1=pichu_successors(x, N, player)   
    a2=pikachu_successors(x, N, player)
    a3=raichu_successors(x, N, player)
    a=a1+a2+a3

    for i in a:
        i=flatten_list(i)
        y.append(heuristic(i,player,N))       
    return a

#This function checks for the end board
def end(board):
    c_w,c_W,c_b,c_B,c_wr,c_br,n_w,n_b=0,0,0,0,0,0,0,0
    for i in range(N*N):
        if board[i] =='w':
            c_w=c_w+1
    for i in range(N*N):
        if board[i] =='W':
            c_W=c_W+1
    for i in range(N*N):
        if board[i] =='b':
            c_b=c_b+1
    for i in range(N*N):
        if board[i] =='B':
            c_B=c_B+1
    for i in range(N*N):
        if board[i] =='@':
            c_wr=c_wr+1
    for i in range(N*N):
        if board[i] =='$':
            c_br=c_br+1
    if (c_w + c_W + c_wr)==0 or (c_b + c_B + c_br)==0:
        return True

#This function returns the heuristic value of the board given by considering weights for each element
#I have considered pichu as 300, pikachu as 800 and raichu as 1500
def heuristic(successor,player,N):
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
    if player=='w':
        value=(((c_w-c_b)*300) + ((c_W-c_B)*800) + ((c_wr-c_br)*1500))
    else:
        value=(((c_b-c_w)*300) + ((c_B-c_W)*800) + ((c_br-c_wr)*1500))

    return value
    

#This function returns the minimum and maximum value of the board depending on the player
def minimax(current_board,depth,alpha,beta,player,N):   
    x=copy.deepcopy(current_board)
    board=convert_liststr_to_str(current_board)
    if depth == 0: 
        return heuristic(list(board),'w',8)
    if player=='w': 
        value = -9999999
        for succ in all_successors(board,N,'w'):
            maxeval=minimax(succ, (depth-1),alpha,beta,'b',N)
            value=max(value,maxeval)
            alpha=max(alpha,maxeval)
            if beta <=alpha:
                break
        return value

    elif player =='b':          
        value = 9999999
        for succ in all_successors(board,8,'b'):
            mineval=minimax(succ, (depth-1),alpha,beta,'w',N)
            value=min(value, mineval)
            beta=min(beta,mineval)
            if beta<=alpha:
                break
        return value


 
# // initial call
# minimax(currentPosition, 3, -∞, +∞, true)
                                               
#This function finds the best possible move of the current board by calling the minimax function
def find_best_move(board, N, player,timelimit):
    alpha=9999999
    beta=-9999999
    bestVal=-999999
    while True:
        for succ in all_successors(board,N,player):
            if player=='w':
                moveVal = minimax(board,2,alpha,beta,'w',N)
                if (moveVal > bestVal) :               
                    bestVal = moveVal
                    yield convert_liststr_to_str(flatten_list(succ))
            
            elif player=='b':
                moveVal = minimax(board,2,alpha,beta,'b',N)
                if (moveVal < bestVal) :               
                    bestVal = moveVal
                    yield convert_liststr_to_str(flatten_list(succ))

      



if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")   
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)

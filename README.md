## Part 1 Raichu:

* Initial State: Given NxN board with white and black Pichus and Pikachus places in a fixed position.
	Source state: ........W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........

* Goal State: To kill all the opponent player pieces

* Successor Function: It is the function which returns all the possible moves of the current state of each and every piece(Pichu, Pikachu or Raichu) on the board of current player.
Pichus : Can move in forward diagonal directions, that is forward right and forward left and can also kill the jump over opponent player Pichu in forward diagonal ways.
Pikachu: Can move one or two positions either forward, left or right. Can also kill and jump over opponent player Pichu or Pikachu if it is in one or two position right or left or forward.
Raichu: In can move in any directions(left, right, up, down and in all four diagonals) in any possible places and can kill and jump over opponent player Pichu or Pikachu or Raichu and land at any position in the same direction.

* Heuristic Function: It calculates the heuristic value by assuming few weights to each and every piece. I have assumed 300 for Pichu, 800 for Pikachu and 1500 for Raichu.  

* Minimax Function: To check whether or not the current move is better than the best move we take the help of this function which will consider all the possible ways the game can go and returns the best value for that move.Alpha beta pruning is used which is an optimization technique for minimax algorithm. It reduces the computation time by a huge factor. This allows us to search much faster and even go into deeper levels in the game tree. It cuts off branches in the game tree which need not be searched because there already exists a better move available. It is called Alpha-Beta pruning because it passes 2 extra parameters in the minimax function, namely alpha and beta.

* How My Solution Works: 
First the input is taken by calling the find_best_move function, this function finds the best possible move of the current board by calling the minimax function which returns the minimum or maximum heuristic value depending on the minimum(‘b’) or maximum player(‘w’).
For each current board received, the successor function firstly calculates all the possible next states of that board and will send that to the minimax condition of alpha beta pruning. In this process of calling each other once the depth reaches the limit then we will call the Heuristic function by sending that particular successor board. Using Min-max algorithm alpha beta pruning we will compute the best move in available time and return it .




## Part 2: The Game of Quintris

(1)Description - 

A game board of size 25 x 15 is given. Randomm 5 size pieces start falling from top of the board towards the end. Goal is to arrange them in such a way so that a complete row can be filled with pieces without gaps. Number of completely filled pieces is equal to player's score.

(2)State space - 

There are maximum 5 possible configurations for every given piece - given piece (as is), rotated piece (90), rotated piece (180), rotated piece (270), horizontal flip (mirror image). Each piece can be moved 'left' and 'right' through the width(15) of the board. The total state space shall count upto - 15^5 = 759375

Initial state - 

Empty board with a falling piece

(3)Successor function -

A function that generates all the valid board moves for given piece configuration. It can be an exhaustive list of all 15^5 combinations.

Heuristic function - 

Stacking of pieces is weighed according to the combination that adds maximum length to the row. Rows are incrementally weighed from bottom to top of the board. Columns are incrementally weighed from right to left. Therefore, the stacking of pieces happens from right to left.

(4)Algorithm design - 
**ExpectiMax algorithm**

There are 3 broad steps to perform for Simple version of Quintris -
1. Get all possible moves for the current falling piece -  populate all the chance nodes
2. Use a utility function to evaluate the chance nodes to identify the best move
3. Compute the best moves of all the configurations and extract the best configuration+best move combination

The algorithm is suppose to compute all the successor moves for a given piece which in game playing called the 'chance nodes'. Then use the evaluation function/utility function to maximise the utility of the best chance node. Extract the best configuration+ best move configuration and return that value.

Sample tree - 

                             piece
                             //\\\
    given piece, rotated(90),rotated(180),rotated(270), hflipped
        ///\\\     ///\\\      ///\\\        ///\\\        ///\\\
      m,mm,b,bb,..  m,mm,b,bb,..  m,mm,b,bb,..  m,mm,b,bb,..  m,mm,b,bb,..
        

## Part 3 Truth be Told
In this problem we have classified user-generated reviews of hotels as deceptive or truthful reviews using the Naive bayes classifier.In order to implement the Naive Bayes classifier,we have first cleaned the training dataset and testing dataset by removing various special charaters like $,!,etc as well as numbers.We created a dictionary of words which were present in the deceptive and truthful reviews of the training dataset.We then found the likelihood probabilities,and the prior probabilities of the classes.Laplace smoothing has been used while finding the probabilities to prevent probability value to be zero. We have found probability of a review in the testing dataset to be deceptive or truthful based on the words in the testing dataset for that review using the Bayes Theorem.The review was then classified as deceptive or truthful by comparing their deceptive and truthful posterior probabilities. We were able to increase the accuracy by filtering the datasets such as reducing special characters and numbers. We also filtered the testing dataset by keeping only those words that were present in either the deceptive or truthful review in the training dataset.The accuracy achieved with this classifier is 80.25%. 

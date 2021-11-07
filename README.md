

## Part 2: The Game of Quintris

(1)Description - 

A game board of size 25 x 15 is given. Randomm 5 size pieces start falling from top of the board towards the end. Goal is to arrange them in such a way so that a complete row can be filled with pieces without gaps. Number of completely filled pieces is equal to player's score.

(2)State space - 

There are maximum 5 possible configurations for every given piece - given piece (as is), rotated piece (90), rotated piece (180), rotated piece (270), horizontal flip (mirror image). Each piece can be moved 'left' and 'right' through the width(15) of the board. The total state space shall count upto - 15^5 = 759375

Initial state - 

Empty board with a falling piece

(3)Successor function -

A function that generates all the valid board moves for given piece configuration. It can be an exhaustive list of all 15^5 combinations.

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

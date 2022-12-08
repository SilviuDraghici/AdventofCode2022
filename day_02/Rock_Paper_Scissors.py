# python 3
# author: Silviu Draghici

'''
A giant Rock Paper Scissors tournament is in progress.

One Elf gives you an encrypted strategy guide (your puzzle input) that they say
will be sure to help you win. "The first column is what your opponent is going
to play:

A for Rock, B for Paper, and C for Scissors.

The second column--"
Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response:

X for Rock, Y for Paper, and Z for Scissors.

Winning every time would be suspicious, so the responses must have been
carefully chosen.

The winner of the whole tournament is the player with the highest score.
Your total score is the sum of your scores for each round. The score for a
single round is the score for the shape you selected
(1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of
the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you,
you should calculate the score you would get if you were to follow the
strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose
Paper (Y). This ends in a win for you with a score of 8
(2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should
choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a
score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get
a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your
strategy guide?
'''

# in case I want to specify file with command line
#import sys
#fileName = sys.argv[1]

if __name__ == "__main__":
  print("evaluating the strategy...")
 
  fileName = 'strategy_guide.txt'
  inputFile = open(fileName, 'r')
  
  l_map = {"A" : "Rock", "B" : "Paper", "C" : "Scissors"}
  r_map = {"X" : "Rock", "Y" : "Paper", "Z" : "Scissors"}
  hand_points= {"Rock": 1, "Paper": 2, "Scissors": 3}
  
  score = 0
  
  while True:
    line = inputFile.readline()
    if not line: break
    line = line.strip()
    
    line = line.split(" ")
    my_hand = r_map[line[1]]
    op_hand = l_map[line[0]]
    
    score += hand_points[my_hand]
    if((op_hand == "Rock" and my_hand == "Scissors") or
       (op_hand == "Paper" and my_hand == "Rock") or
       (op_hand == "Scissors" and my_hand == "Paper")):
      pass
    elif(op_hand == my_hand):
      score += 3
    else:
      score += 6
    
  inputFile.close()

  print("This strategies score is {}".format(score))
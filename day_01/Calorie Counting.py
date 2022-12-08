# python 3
# author: Silviu Draghici

'''
The Elves take turns writing down the number of Calories contained by the
various meals, snacks, rations, etc. that they've brought with them,
one item per line. Each Elf separates their own inventory from the previous
Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up
with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories,
a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.

The third Elf is carrying food with 5000 and 6000 Calories,
a total of 11000 Calories.

The fourth Elf is carrying food with 7000, 8000, and 9000 Calories,
a total of 24000 Calories.

The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf
to ask: they'd like to know how many Calories are being carried by the Elf
carrying the most Calories. In the example above,
this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories.
How many total Calories is that Elf carrying?
'''

# in case I want to specify file with command line
#import sys
#fileName = sys.argv[1]

if __name__ == "__main__":
  print("Finding most calories held by single elf...")
 
  fileName = 'calorie_counts.txt' 
  inputFile = open(fileName, 'r')

  current_elf = 1
  current_calories = 0
 
  max_elf = current_elf
  max_calories = current_calories
 
  while True:
  
    line = inputFile.readline()
    if not line: break
    
    if line == "\n":
      if(current_calories > max_calories):
        max_calories = current_calories
        max_elf = current_elf
      current_elf += 1
      current_calories = 0
  
    else:
      current_calories += int(line.strip())
    
  inputFile.close() 
  
  if(current_calories > max_calories):
    max_calories = current_calories
    max_elf = current_elf
  
  print("Elf {} is carrying the most calories with {} ".format(max_elf, max_calories))

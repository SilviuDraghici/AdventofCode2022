# python 3
# author: Silviu Draghici

'''
The expedition comes across a peculiar patch of tall trees all planted carefully
in a grid. The Elves explain that a previous expedition planted these trees as a
reforestation effort. Now, they're curious if this would be a good location for
a tree house.

First, determine whether there is enough tree cover here to keep a tree house
hidden. To do this, you need to count the number of trees that are visible from
outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height
of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is
the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid
are shorter than it. Only consider trees in the same row or column; that is,
only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are
already on the edge, there are no trees to block the view. In this example,
that only leaves the interior nine trees to consider:

The top-left 5 is visible from the left and top. (It isn't visible from the
right or bottom since other trees of height 5 are in the way.)
The top-middle 5 is visible from the top and right.
The top-right 1 is not visible from any direction; for it to be visible, there
would need to only be trees of height 0 between it and an edge.
The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, there
would need to be only trees of at most height 2 between it and an edge.
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a
total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
'''

# in case I want to specify file with command line
#import sys
#fileName = sys.argv[1]

if __name__ == "__main__":
  print("")
  
  fileName = 'input_test.txt'
  inputFile = open(fileName, 'r')
  
  tree_grid = []
  
  line = inputFile.readline()
  line = line.strip()
  
  width = len(line)
  
  while line:
    line = line.strip()
    line = list(map(int, list(line)))
    
    tree_grid.append(line)
    
    line = inputFile.readline()
  inputFile.close()
  
  height = len(tree_grid)
  
  max_s = 0
  max_e = 0
  
  visible_grid = [ [False] * (width) for i in range(height)]
  
  for h in range(1, height - 1):
    row = tree_grid[h]
    
    max_e = [0] * width
    max_e[width - 1] = row[width - 1]
    for w in range(width - 2, 0, -1):
      max_e[w] = max(row[w], max_e[w + 1])
    
    max_s = row[0]
    for w in range(1, width - 1):
      if row[w] > max_s or row[w] > max_e[w + 1]:
        visible_grid[h][w] = True
      max_s = max(max_s, row[w])

  for w in range(1, width - 1):
    row = [tree_grid[h][w] for h in range(height)]
    
    max_e = [0] * height
    max_e[height - 1] = row[height - 1]
    for h in range(height - 2, 0, -1):
      max_e[h] = max(row[h], max_e[h + 1])
    
    max_s = row[0]
    for h in range(1, height - 1):
      if row[h] > max_s or row[h] > max_e[h + 1]:
        visible_grid[h][w] = True
      max_s = max(max_s, row[h])
    
  num_visible = 0
  for h in range(1, height - 1):
    for w in range(1, width - 1):
      if visible_grid[h][w]:
        num_visible += 1
  
  num_visible += 2 * height + 2 * width - 4 
  print("There are {} visible trees".format(num_visible))
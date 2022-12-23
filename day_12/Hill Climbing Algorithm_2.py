# python 3
# author: Silviu Draghici

'''
You try contacting the Elves using your handheld device, but the river you're
following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input).
The heightmap shows the local area from above broken into a grid; the elevation
of each square of the grid is given by a single lowercase letter, where a is the
lowest elevation, b is the next-lowest, and so on up to the highest elevation,
z.

Also included on the heightmap are marks for your current position (S) and the
location that should get the best signal (E). Your current position (S) has
elevation a, and the location that should get the best signal (E) has elevation
z.

You'd like to reach E, but to save energy, you should do it in as few steps as
possible. During each step, you can move exactly one square up, down, left, or
right. To avoid needing to get out your climbing gear, the elevation of the
destination square can be at most one higher than the elevation of your current
square; that is, if your current elevation is m, you could step to elevation n,
but not to elevation o. (This also means that the elevation of the destination
square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could
start by moving down or right, but eventually you'll need to head toward the e
at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square
moving up (^), down (v), left (<), or right (>). The location that should get
the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the
location that should get the best signal?

--- Part Two ---

As you walk up the hill, you suspect that the Elves will want to turn this into
a hiking trail. The beginning isn't very scenic, though; perhaps you can find a
better starting point.

To maximize exercise while hiking, the trail should start as low as possible:
elevation a. The goal is still the square marked E. However, the trail should
still be direct, taking the fewest steps to reach its goal. So, you'll need to
find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the square
marked S that counts as being at elevation a). If you start at the bottom-left
square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with
elevation a to the location that should get the best signal?
'''

mods = [1,0,-1,0,1]

def dfs(searchList):
  global steps
  
  newSearchList = set()

  for (r, c) in searchList:
    h = field[r][c]
    
    if h == -14 or h == 0:
      return
    
    if h == -28:
      h = 25
    field[r][c] = -10
    for i in range(4):
      rm = r + mods[i]
      cm = c + mods[i + 1]
      if(0 <= rm < R) and (0 <= cm < C):
        hm = field[rm][cm]
        if hm == -14:
          hm = 0
        d = hm - h
        if d >= -1:
          newSearchList.add((rm,cm))
  steps += 1
  dfs(newSearchList)


if __name__ == "__main__":
  print(f"")
  
  fileName = 'input.txt'
  inputFile = open(fileName, 'r')
  
  field = []
  
  line = inputFile.readline()
  while line:
    line = line.strip()
    field.append([ord(c) - ord('a') for c in line])
    
    line = inputFile.readline()
  inputFile.close()
  
  
  steps = 0
  
  R = len(field)
  C = len(field[0])
  
  for r in range(R):
    for c in range(C):
      if field[r][c] == -28:
        searchList = set([(r,c)])
        dfs(searchList)
        break
  
  print(f"{steps}")

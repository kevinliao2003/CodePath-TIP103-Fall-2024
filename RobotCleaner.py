# OA problem: Robot Cleaner

"""
Given array of grid matrix, a robot need to clean the entire plan of floors
A clean floor is marked by "." and dirty floor is marked by "*" where is "#" is a wall. A robot can move 4 directions in a grid up, down, bot, left. 
Determine the minimum run robots needs to do to clean the entire grid. 
The robot can only move on block containing "." (clean grid) or "*" (dirty grid).

Edge case if connected clean floor doesn't have dirty sport, the robot won't run those spots (test case no 4 for reference)

couple of input test cases

['.#..', 
 '.#.#', 
 '######', 
 '...#.', 
 '...###'], output = 3

['#.*', 
 '#..#', 
 '.##.', 
 '*..'] , output = 2

['###', '###', '#####', '##', '.#####.', '..#..'], out = 5

['.....', 
 '#####', 
 '....*'], out = 1

 [ ".*#..*", 
   ".*#*.#", 
   "######", 
   ".*..#.", 
   "...###" ], result = 3

where ROWS = len(grid) and Cols = len(grid[0]).
"""

"""
Understand - 
Match - graphs (dfs), recursion

dfs:
- easier to implement with recursion rather than a queue for bfs
Plan/Implement:
define a recursive helper function
    base case: the robot hits a wall or if the robot is out of bounds, terminate

    if the position is dirty, mark it as clean
    # call the helper function in all 4 directions (up, down, left, right)

set the counter to 0
iterate over the grid
    iterate over the columns
        if the grid is dirty, call the helper function
        increment the counter
"""

def minSteps(grid):
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(row, col):
        # base case
        if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "#" or grid[row][col] == "x":
            return
        
        # if the position is dirty, mark it as clean
        grid[row] = grid[row][0:col] + "x" + grid[row][col+1:]
        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)

    counter = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "*":
                dfs(row, col)
                counter += 1

    return counter

print(minSteps(['.....', '#####', '....*']))
print(minSteps([ ".*#..*", ".*#*.#", "######", ".*..#.", "...###" ]))
print(minSteps(['#.*', '#..#', '.##.', '*..']))

"""
TC: O(2n), O(n * m) where n is the number of rows and m is the number of columns
SC: O(n * m) where
"""
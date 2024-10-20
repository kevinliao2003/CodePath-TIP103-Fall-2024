from collections import deque

# PROBLEM 1
def updateMatrix(mat):
  """
  1. Is 0 guaranteed to be in the matrtix? Can the matrix values be either 0 or 1?
  2. Matrix - likely, bfs - likely
  3. If the value is already 0, do nothing. Otherwise, use a bfs to find the nearest 0 for the cell.
  4.
  initialize an empty queue
  initialize an empty visited set

  loop through all the rows
      loop through all the cols
          if the value is 0
              add that position to the queue
              add that position to the visited set

  whule the queue isn't empty
      pop the leftmost element in the queue

      check all directions (up, down, left, right)
          get the new position
          check if the new position hasn't been visited and is in bounds
              add the position to the visited set
              add the position to the queue
              update the number of steps in the matrix

  return the matrix
  5. See code below.
  6. I think that overall, this is a very efficient approach with a time complexity of O(m * n) which is the number of nodes and with a space complexity of O(m * n) which is the visited and queue combined.
  """

  ROWS, COLS = len(mat), len(mat[0])
  q = deque()
  visited = set()
  for row in range(ROWS):
      for col in range(COLS):
          if mat[row][col] == 0:
              q.append((row, col, 0))
              visited.add((row, col))

  while q:
      row, col, steps = q.popleft()

      for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          new_row, new_col = row + x, col + y
          if (0 <= new_row < ROWS and 0 <= new_col < COLS 
              and (new_row, new_col) not in visited):
              q.append((new_row, new_col, steps + 1))
              visited.add((new_row, new_col))
              mat[new_row][new_col] = steps + 1

  return mat

# PROBLEM 2
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
  """
  1. Is (sr, sc) guaranteed to be a valid position in the image? Can the image be empty?
  2. Graphs - likely, bfs - likely
  3. Do a bfs from (src, sc).
  4.
  initialize a queue with the position (sr, sc)
  initialize a visited set
  while the queue isn't empty
      for every element in the queue
          pop the leftmost element
          change the color at that position
          check all 4 directions (up, down, left, right)
              if the position isn't out of bounds, hasn't been visited, and the value is qual to the color at position (sr, sc)
                  add the position to the queue
                  add the position to the visited set

  return the image
  5. See code below.
  6. The time complexity is O(N) where N is the number of pixels in the image and the space is O(N) where N is the number of pixels, since we may have to process every pixel at the end.
  """

  ROWS, COLS = len(image), len(image[0])
  change = image[sr][sc] # color to change
  q = deque([(sr, sc)])
  visited = set()
  visited.add((sr, sc))

  while q:
      for _ in range(len(q)):
          row, col = q.popleft()
          image[row][col] = color
          for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
              new_row, new_col = row + x, col + y
              if (0 <= new_row < ROWS and 0 <= new_col < COLS 
                  and (new_row, new_col) not in visited 
                  and image[new_row][new_col] == change):
                      q.append((new_row, new_col))
                      visited.add((new_row, new_col))

  return image
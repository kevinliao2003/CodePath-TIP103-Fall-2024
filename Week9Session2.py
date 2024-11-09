def exist(self, board: List[List[str]], word: str) -> bool:
    """
    1. Can the board be empty? Can the word be empty?
    2. Graphs - likely, bfs - likely, dfs - likely
    3. First, loop through the board and find a cell that contains the first char of word. Call dfs on that cell to check if the word exists in the board.
    4.
    define a dfs function with the row, col, visited set, and current index as parameters
        if the index is equal to the length of word
            return True
            
        if row is in bounds, cols in bounds and if the cell at (row, col) is equal to the val of the index in word
            add that position to the visited set
            call dfs on all 4 directions (left, right, up, down) and take the union of all of them
            
        remove the (row, col) position from the visited set
        return False
    
    for each row in board
        for each col in board
            if the cell's char is equal to the first char in word
                call dfs on that cell
    5. See code below.
    6. 
    """
    
    ROWS, COLS = len(board), len(board[0])
    
    def dfs(row, col, visited, idx):
        if idx == len(word):
            return True
        
        if (0 <= row < ROWS and 0 <= col < COLS 
            and (row, col) not in visited 
            and board[row][col] == word[idx]):
                visited.add((row, col))
                res = (dfs(row - 1, col, visited, idx + 1)
                or dfs(row + 1, col, visited, idx + 1)
                or dfs(row, col - 1, visited, idx + 1)
                or dfs(row, col + 1, visited, idx + 1))
                visited.remove((row, col))
                return res
        
        return False
    
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == word[0] and dfs(row, col, set(), 0):
                return True
            
    return False

 def generateParenthesis(self, n: int) -> List[str]:
    """
    U - Can n only be a positive inteer?
    M - Backtracking, recursion
    P -
    For it to be a well-formed parenthesis, at any given point in the parenthesis, the number of closed parenthesis must be less than or equal to the number of open parenthesis.
    I - 
    initialize a res variable to store all well-formed parenthesis
    initialize a curr variable for the current parenthesis
    
    define a recursive helper method (parameters: num_opened, num_closed)
        if num_opened equals n and num_closed equals n
            add curr to res
            return
        if num_closed is greater than num_opened
            return
            
        if num_opened is less than n
            add an opened parenthesis to curr
            recursively call the function, updating the num_opened parameter
            backtrack
        if num_closed is less than num_opened
            add a closed parenthesis to curr
            recursively call the function, updating the num_closed parameter
            backtrack
        
    call the helper method
    return res
    
    Example: n = 3
    backtrack(0, 0)
    backtrack(1, 0)
        backtrack(1, 1)
            backtrack(2, 1)
            backtrack(3, 1)
            backtrack(3, 2)
            backtrack(3, 3) -> return and backtrack
            
            backtrack(2, 2)
            backtrack(3, 2)
            backtrack(3, 3) -> return and backtrack
    backtrack(2, 0)
        backtrack(2, 1)
            backtrack(3, 1) -> return and backtrack
            backtrack(3, 2) -> return and backtrack
            backtrack(3, 3) -> return and backtrack
            
            backtrack(2, 2) -> return and backtrack
            backtrack(3, 2) -> return and backtrack
            backtrack(3, 3) -> return and backtrack
    backtrack(3, 0) -> return and backtrack
        backtrack(3, 1) -> return and backtrack
        backtrack(3, 2) -> return and backtrack
        backtrack(3, 3) -> return and backtrack
                                    
    curr = "()()()"
    res = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    R - 
    E - The time complexity would be O(4^n/n^(1/2)) which is the total number of valid parenthesis. The space complexity would be O(2n) since that's the maximum number of recursive calls on the recursive call stack in addition to the res and curr arrays.
    """
    
    res = []
    curr = []
    
    def backtrack(num_opened, num_closed):
        # print(num_opened, num_closed)
        if num_opened == n and num_closed == n:
            res.append("".join(curr.copy()))
            return
        if num_closed > num_opened:
            return
        
        if num_opened < n:
            curr.append('(')
            backtrack(num_opened + 1, num_closed)
            curr.pop()
        if num_closed < num_opened:
            curr.append(')')
            backtrack(num_opened, num_closed + 1)
            curr.pop()
            
    backtrack(0, 0)
    return res

def subsets(self, nums: List[int]) -> List[List[int]]:
    """
    U - 
    No duplicate subsets should be in the solution
    All numbers in nums are unique
    nums is guaranteed to have at least 1 element
    M - Recursive backtracking
    P/I - 
    initialize an empty list called res
    initialize an empty list called curr_combo
    
    define a helper method (parameters: idx)
        if idx is the length of nums
            add a deep copy of curr_combo to res
            return
            
        add the value at idx to curr_combo
        call the helper method, incrementing idx
        pop from idx
        call the helper method, incrementing idx
    R - 
    E - The space complexity in the worst case scenario would be O(2^n) since there are 2^n subsets where n is the length of nums. The time complexity is O(2^n) since there are 2 recursive calls for each function calls.
    """
    
    res = []
    curr_combo = []
    
    def helper(idx):
        if idx == len(nums):
            res.append(curr_combo.copy())
            return
        
        curr_combo.append(nums[idx])
        helper(idx + 1)
        curr_combo.pop()
        helper(idx + 1)
        
    helper(0)
    return res
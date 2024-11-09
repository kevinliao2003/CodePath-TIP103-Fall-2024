def longestPalindrome(self, s: str) -> str:
    """
    U - Will the string only contain lowercase English letters? Can it contain symbols, numbers? Moreover, can it be empty?
    M - Dynamic programming, 2 pointers, string
    P -
    We need to account for 2 cases: palindromes of odd and even length
    
    Iterate through s once and at each index, check for palindromes of even and odd length, updating the longest palindromic substring accordingly.
    I -
    initialize the longest palindrome substring (longest_str) to an empty string
    loop through s
        initialize a left pointer (l) to be (curr_idx - 1)
        initialize a right pointer (r) to be (curr_idx + 1)
        while the chars at l and r are the same and l and r are in bounds
            decrement l
            increment r
        increment l
        decrement r
        
        update longest_str if necessary
        
        initialize a left pointer (l) to be curr_idx
        initialize a right pointer (r) to be (curr_idx + 1)
        while the chars at l and r are the same and l and r are in bounds
            decrement l
            increment r
        increment l
        decrement r
        
        update longest_str if necessary
        
    return longest_str
    R - Since we iterate through the string once and expand from the center at each iteration, the time complexity would be O(n) with n being the number of elements in the string. We aren't allocating additional memory for any data structures, so the space complexity would be O(1)
    E - 
    """
    
    longest_str = ""
    for curr_idx in range(len(s)):
        # palindrome of odd length
        l, r = curr_idx - 1, curr_idx + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        
        if (r - l + 1) > len(longest_str):
            longest_str = s[l:r + 1]
        
        # palindrome of even length
        l, r = curr_idx, curr_idx + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        
        if (r - l + 1) > len(longest_str):
            longest_str = s[l:r + 1]
            
    return longest_str

def maxSubArray(self, nums: List[int]) -> int:
    """
    1. Does the array consist just of integers? Can they be positive and negative?
    2. Dynamic programming - likely
    3. Brute force method would just be to do 2 nested loops and check every possible subarray, but that likely won't be very efficient.
    
    Optimize using dynamic programming which will likely be a single iteration through the array.
    4.
    if nums is of length one return the first number by default
    
    start from index 1 of the nums
        update the value at the index with the maximum of the current value and the sum of the current value and the previous value
    return the maximum value in nums
    5. See code below.
    6. 
    """
    if len(nums) == 1:
        return nums[0]
    
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
    return max(nums)

def maximalRectangle(self, matrix: List[List[str]]) -> int:
    """
    1. Will the matrix only consist of 0s and 1s? Can it be empty? Will there always be a 1 in the array?
    2. DP - likely, graph dfs - neutral
    3. 
    If there is a 1 in the matrix, the minimum area is 1.
    IF there is a 1, traverse the column to calculate the length of the rectangle. From there, calculate the height
    4.
    initialize a res variable for the maximum area
    initialize an empty 2-d matrix called dp
    
    for each row in the matrix
        for each col in the matrix
            if the value at the position is 0
                continue
                
            set width to be 0
            if col is greater than 0
                set the dp result at the position to be one more than the dp result at the right
            otherwise
                set the dp result at that position to be 1
            set the width to be the dp value at the current position
            
            initiliaze height to be 0
            while the row is greater than 0
                set width to be the min of width and the row at (row - height)
                increase the height
                update res accordingly
                
    return res
    5. See code below.
    6. 
    """
    ROWS, COLS = len(matrix), len(matrix[0])
    
    res = 0
    dp = [[0] * COLS for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            if matrix[row][col] == '0':
                continue
                
            if col > 0:
                dp[row][col] = dp[row][col - 1] + 1
            else:
                dp[row][col] = 1
            width = dp[row][col]
            
            height = 0
            while row - height >= 0 and width > 0:
                width = min(width, dp[row - height][col])
                height += 1
                res = max(res, width * height)
                
    return res
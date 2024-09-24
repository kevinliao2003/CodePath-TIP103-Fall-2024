from collections import defaultdict 

"""
Problem 1: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
Problem 2: https://leetcode.com/problems/shifting-letters/
Problem 3: https://leetcode.com/problems/set-matrix-zeroes/
Problem 4: https://leetcode.com/problems/longest-repeating-character-replacement/
Problem 5: https://leetcode.com/problems/group-anagrams/description/
"""

# PROBLEM 1
"""
1. With the array only consist of integers? Only positive or negative integers? Could the input array be empty?
2. Two pointers - likely, sliding window - likely, stack - neutral
3. We want to keep track of the maximum element in a specific window. A monotonic stack would be good for this. On each iteration, check if the current element is less than the largest element in the stack. If so, continue to pop until the condition becomes false. Before continuing onto the next iteration, append the maximum element to the stack
4.
create an empty stack
iterate through the array
    keep track of the curr_max, or current maximum and initialize it to with the current value in the array
    when the stack is not empty and the current number is less than the largest element in the stack
        pop from the stack and update the current maximum accordingly
    append the current maximum to the stack
return the length of the stack
5. See the code below.
6. I think the overall, the implementation is rather efficient and uses more of a monotonic stack + greedy approach. Moreover, the time and space complexities are O(n).
"""

def maxChunksToSorted(arr):
   stack = []
   for num in arr:
       curr_max = num
       while stack and num < stack[-1]:
           curr_max = max(curr_max, stack.pop())
       stack.append(curr_max)
   return len(stack)

print(maxChunksToSorted([5,4,3,2,1]))
print(maxChunksToSorted([2,1,3,4,4]))

# PROBLEM 2
"""
1. Will the string only consist of lowercase English characters? Can the input string be empty? Will the length of s and shifts ALWAYS be the same?
2. String - likely, Array - likely
3. Use the ord function to get the ASCII value of a character and the chr function to get the corresponding char of the ASCII value. Loop through the shifts array and have a nested for loop to account for the first i + 1 letters. Beaware that the char z is an edge case.
4. 
initialize an empty string to append to.
iterate through the shifts
    iterate through all the chars up to the current index in shifts
        EDGE CASE: the new ascii value is grater than 122, which is the ascii value of z
            start the shift from 97, which is the ascii of 'a'
            get the corresponding ASCII value
            increment the ASCII value by the shift
            get the corresponding char of the new ASCII value
            append that char to the empty string
        Otherwise
            get the corresponding ASCII value
            increment the ASCII value by the shift
            get the corresponding char of the new ASCII value
            append that char to the empty string
5. See the code below.
6. Overall, I think this implementation is very efficient, with a single iteration through the array (linear time) and allocating memory for a new string (linear time). 

NOTES:
- To optimize the solution, calculate the total number of shifts for each character first
- Update shifs so that the number in each index contains the total numbers of shifts for a char at that index. Moreover, the fact that I precompute the number of times each character is shifted before doing the shift safes time, since I don't need to account for another nested loop.
"""

def shiftingLetters(s, shifts):
  for i in range(len(shifts) - 2, -1, -1):
    shifts[i] += shifts[i + 1]

  res = ""
  for i, shift in enumerate(shifts):
    new_ascii = ord(s[i]) + shift
    new_char = chr(97 + (new_ascii - 97) % 26)
    res += new_char
  return res

print(shiftingLetters("abc", [3,5,9]))
print(shiftingLetters("aaa", [1,2,3]))

# PROBLEM 3
"""
1. Could the matrix be empty? Does each row have the same nubmer of columns? Can I expect the matrix to contain just integers?
2. Array - likely
3. Try to implement this using constant space, as suggested by the problem. On the first iteration of the matrix, if a position is 0, set the first index of the row and column to 0. From there, using the first row and first column, update the element.

EDGE CASE: checl if the first row or the first col need to be set to 0
4. 
get the number of rols and cols in the matrix

loop through the rows
    loop through the cols
        if the current position is 0
            set the first index of the row to 0
            set the first index of the col to 0

loop through the rows starting at index 1
    loop through the cols starting at index 1
        if the first index of the current row or first index of the current col is 0
            set the position to 0

check if the first row needs to be set to 0 or if the second row needs to be set to 0

5. See code below.
6. This approach is optimized and uses O(n^2) time complexity since it uses a nested loop to traverse the matrix and O(1) time since no additional memory is created.

NOTES:
My initial approach was to use a set for rows and cols and if a position was marked 0, I would add that row to the rows set and col to the cols set. I would then traverse the matrix another time and if the row was already in the rows set or col was already in the cols set, I would set that position to 0.

The approach using constant space takes advantage of the first index of the row and column if there exists a 0 in that row or column.
"""

def setZeroes(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])

    first_col = False # if the first column should be set to 0
    for row in range(ROWS):
        if matrix[row][0] == 0:
            first_col = True
        for col in range(1, COLS):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

    for row in range(1, ROWS):
        for col in range(1, COLS):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0

    if matrix[0][0] == 0:
        for col in range(COLS):
            matrix[0][col] = 0
    if first_col:
        for row in range(ROWS):
            matrix[row][0] = 0

    print(matrix)

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

# PROBLEM 4
"""
1. Will the string only contain uppercase English letters? Can the input string be empty?
2. Sliding window - likely, two pointers - likely
3. Have 2 pointers, one that starts at index 0 and the other at index 1. Use a dictionary to map each character to its frequency in the window. When the length of the window - the maximum frequency is greater than k, update the size of the largest window and increment the left pointer accordingly.
4. 
initialize two pointers, a left and a right
initialize a res variable that tracks the lenght of the largest substring
initialize a dictionary that maps each char to its frequency

when the right pointer doesn't exceed bounds
    for the char at the right pointer, increment the count in the dict by 1
    if the length of the window - the maximum frequency is larger than k
    decrement the count of the char at the left pointer
    move the left pointer

update the largest size of the window
increment the right pointer
    
5. See code below.
6. I would say that overall, this is a very efficient implementation. The time complexity is O(n), since I'm iterating over the string once, and I'm not using additional memory, so the space complexity would be O(1).
"""

def characterReplacement(s, k):
    l, r = 0, 0
    res = 0
    dic = defaultdict(int)
    while r < len(s):
        dic[s[r]] += 1
        if (r - l + 1) - max(dic.values()) > k:
            dic[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
        r += 1

    return res

print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))

# PROBLEM 5
"""
1. Will all the strings contain just lowercase English characters? Can a string be empty?
2. String - likely, Dictionary - likely
3. If 2 words were angrams, they would be the same if sorted in alphabetical order. USe a dictionary to map each sorted string to the corresponding strings. At the end, return the values of the dictionary.
4.
initialize a dictionary
loop through all the strings
    get the sorted string in alphabetical order
    add that pair (sorted string, original string) to the dictionary
return the values of the dictionary
5. See code below.
6. The time complexity would be O(n), since I'm iterating through the list of sttings, and the space complexity would be O(n), since I'm allocating additional memory for a dictionary. Overall, I think this approach is very efficient, and using a dictionary simplifies the work by a lot.
"""
def groupAnagrams(strs):
    dic = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        dic[sorted_word].append(word)
    return dic.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
# Substring
"""
1. Could the first string be empty? Could the second string be empty? Is it possible that length of the second string is less than that of the first string?
2. Built-in method in Python to check if one string is a substring of another - likely, Two Pointers - likely
3. 
First approach: return if second is present in first
Second approach: use a nested for loop, keeping track of the indices for second and first. For each index of second, check the next len(first) digits to see if the window contains the substring.
4. 
first_len = length of first string
second_len = length of second string
check if second_len > first_len:
  return False

for i in range(first_len - second_len):
  is_substring = if the current window contains the substring
  for j in range(second_len):
    if first[i + j] = second[j]:
      continue 
    else:
      is_substring = False
      break

return True
5. See below.
6. Both methods use constant space and O(n*m) time, which I think is the optimal solution.
"""

def substring1(first, second):
    first_len, second_len = len(first), len(second)
    if second_len > first_len:  # base case
        return False

    for i in range(first_len - second_len):
        is_substring = True
        for j in range(second_len):
            if first[i + j] == second[j]:
                continue
            else:
                is_substring = False
                break

        if is_substring:
            return True

    return False

def substring2(first, second):
    return second in first

"""
print(substring1("laboratory", "rat"))
print(substring1("cat", "meow"))
print(substring2("laboratory", "rat"))
print(substring2("cat", "meow"))
"""

# Longest Common Prefix
"""
1. Do the strings only contain lowercase English characters? Could they be empty?
2. Two Pointers - likely, Sliding Window - likely
3. Start at index 0, and check if each character has the same character at that index. If so, continue. Otherwise, termiante and return the string.
4.
The longest prefix cannot be longer than the length of the smallest string in strs.

Sort strs by length of string in increasing order.

If the smallest string is empty, return an empty string.

Otherwise, increment the index for which the chars of strings are equal and continue until the condition becomes false.
5. See code below.
6. Since I'm reassigning a sorted array, the space complexity would be O(n). Moreover, the time complexity would be O(n^2), since I have nested loops. I believe the code takes advantage of the fact that the longest prefix must be less than or equal to the shortest string in the input.
"""

def longestCommonPrefix(strs):
    strs = sorted(strs, key=len) # sorts strs by length of strings
    smallest = strs[0] # shortest string

    prefix, curr_idx = "", 0
    while curr_idx < len(smallest):
        for i in range(1, len(strs)):
            if strs[i][curr_idx] != smallest[curr_idx]:
                return prefix

        prefix += smallest[curr_idx]
        curr_idx += 1
    return prefix

"""
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
"""

# Add Binary
def addBinary(a, b):
        """
        UMPIRE method
        1. Are the only possible digits 1 and 0s?
        2. Bit manipulation - likely
        3. Start at the last character of each string and check the digits. If both are 0, keep track of the carry and add 0 to the string. Otherwise, add 1.
        4. 
        get the lengh of the smaller string
        start at the last index of the smaller string and traverse through the entire string
            at the index, if both numbers are 1, add 0 and keep track of the carry
            otherwise, add 1
        
        for the larger string, check if any digits have been visited and add the carry if necessary
        """
        
        # OPTIMAL SOLUTION
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digit1 = ord(a[i]) - ord("0") if i < len(a) else 0
            digit2 = ord(b[i]) - ord("0") if i < len(b) else 0
            
            total = digit1 + digit2 + carry
            toAdd = str(total % 2) # digit to append to the string
            carry = total // 2
            res = toAdd + res
        
        if carry:
            res = "1" + res
        
        return res
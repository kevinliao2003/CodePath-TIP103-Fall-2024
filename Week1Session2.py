# Integer Replacement
"""
1. Can the input number be very large?
2. Recursion - likely, Dynamic Programming - neutral
3. Implement the method recursively. If the number is even, recursively call the function on n//2. Otherwise, recursively call the function on (n + 1) and (n - 1) and take the max of each.
4.
def integerReplacement(n):
    if n is equal to 0, return 0

    if n is divisible by 2: 
        call integerReplacement(n // 2) + 1
    otherwise, max(integerReplacement(n + 1), integerReplcement(n - 1)) + 1
5. See code below.
6. The space complexity would be determined by the depth of the recursion tree, which is O(logn) when n is even and O(n) when n is odd. Therefore, in the worst case scenario, O(n) would be the worst time complexity. The time complexity in the worst case scnario would be O(2^n).

This may not be the most efficient method, since there may be a lot of repeated work. The most efficient solution would involve memoization.
"""

def integerReplacement(n):
    if n <= 1:
        return 0

    if n % 2 == 0:
        return integerReplacement(n // 2) + 1
    else:
        return min(integerReplacement(n + 1), integerReplacement(n - 1)) + 1

# The code below uses memoization. The time complexity would be O(n) and the space complexity would be O(n).
def integerReplacement(n):
    dp = defaultdict(int) # memoization involving dp
    def memoize(n):
        if n <= 1:
            return 0
        if n in dp:
            return dp[n]

        if n % 2 == 0:
            dp[n] += memoize(n // 2) + 1
        else:
            dp[n] += min(memoize(n + 1), memoize(n - 1)) + 1
        return dp[n]

    return memoize(n)

# Roman to Integer
"""
1. Could there be symbols that don't represent any numbers? Is the input restricted to only uppercase English letters?
2. Dictionary - likely
3. Create a dictionary containing the special cases, such as 4 and 9. From there, loop through s and check 2 digits at a time to see if they are in the dictionary as keys. If so, add to the number accordingly and increment the index by 2. Otherwise, just increment the index by 1.
4. 
Create a dictionary containing the special cases, such as 4 and 9.

num, curr_idx = 0, 0
while curr_idx < len(s) - 1:
    substr = s[curr_idx:curr_idx + 2]
    if substr in dic:
        num += dic[substr]
        curr_idx += 2
    else:
        num += dic[s[curr_idx]]
        curr_idx += 1
return num
5. See code below.
6. The space complexity would be O(n), since I'm allocating memory for a dictionary, and the time complexity would be O(n), since I'm iterating over the string once. I would say that this solutoion is overall quite efficient in that I use a dictionary to store the special cases of roman numerals.
"""

def romanToInt(s):
    dic = {
        'I':1,
        'IV':4,
        'V':5,
        'IX':9,
        'X':10,
        'XL':40,
        'L':50,
        'XC':90,
        'C':100,
        'CD':400,
        'D':500,
        'CM':900,
        'M':1000,
    }

    num, curr_idx = 0, 0
    while curr_idx < len(s) - 1:
        substr = s[curr_idx:curr_idx + 2]
        if substr in dic:
            num += dic[substr]
            curr_idx += 2
        else:
            num += dic[s[curr_idx]]
            curr_idx += 1

    if curr_idx == len(s) - 1:
        num += dic[s[curr_idx]]
    return num

print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))

# Integer to Roman
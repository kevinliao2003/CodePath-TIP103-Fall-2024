def trap(self, height: List[int]) -> int:
        """
        U - Can height be empty?
        M - Two pointers
        P/I -
        Have a left pointer (l) and a right pointer (r).
        Moreover, keep track of the maximum left height (maxLeft) and the maximum right height (maxRight).
        
        initialize the total amount of water (total)
        initialize l to index 0
        initialize r to the last index in the array
        initialize maxLeft and maxRight to negative infinity
        while l is less than r
            if the value at pointer l is less than or equal to the value at pointer r
                update maxLeft
                update total by adding to it the difference between maxLeft and the value at pointer l
                increment the pointer l
            otherwise
                update maxRight
                update totalby adding to it the difference between maxRight and the value at pointer r
                decrement the pointer r
                
        return total
        
        Example: [0,1,0,2,1,0,1,3^l^r,2,1,2,1]
        l = 7, r = 8
        maxLeft = 2, maxRight = 2
        total = 6
        R - 
        E - The time complexity is O(n) where n is the number of entries in height and the space complexity is O(1).
        """
        
        total = 0
        l, r = 0, len(height) - 1
        maxLeft = maxRight = float('-inf')
        while l < r:
            if height[l] <= height[r]:
                maxLeft = max(maxLeft, height[l])
                total += (maxLeft - height[l])
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                total += (maxRight - height[r])
                r -= 1
                
        return total

def isPalindrome(self, s: str) -> bool:
        """
        1. Can the string contain numbers? Can the input string be empty
        2. String - likely
        3. First, build a new string that converts all uppercase letters to lowercase letters and removes all non-alphanumeric numbers. From there, use two pointers to check if the string is a palindrome
        4. 
        initialize new_str: a new string that converts all uppercase letters to lowercase and removes any other kinds of characters
        loop through the string
            check if the char is a letter and is uppercase
                append the lowercase char to new_str
        
        use a left and right pointer
        while the left pointer is less than the right pointer
            check if the chars at the positions are equal
                increment the pointers
            otherwise, return false
            
        return true
        5. See code below.
        6. 
        """
        
        new_str = ""
        for char in s:
            if char.isupper():
                new_str += char.lower()
            elif char.islower() or char.isnumeric():
                new_str += char
        
        l, r = 0, len(new_str) - 1
        while l < r:
            if new_str[l] == new_str[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True

def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        U - 
        nums contains at least 3 elements
        the numbers can be positive or negative
        if there are no triplets that equal 0, return an empty list
        the solution CANNOT contain duplicate triplets
        M - Sorting, binary search
        P/I - 
        The brute force would be to check all triplet combos using 3 nested loops, but thise will result in a O(n^3) time complexity which probably isn't very efficient.
        
        However, if we sort the array and use binary search, that may be more optimal.
        
        Example: nums = [-1,0,1,2,-1,-4]
        sorted nums: [-4, -1, -1, 0, 1, 2]
        
        Pseudocode:
        sort nums in increasing order
        initialize an empty res list
        loop through nums
            # prevent duplicates
            if the index is greater than 0 and is equal to the previous num
                continue
        
            set a left pointer equal to the current index + 1
            set a right pointer equal to the last index
            while left is less than right
                get the mid pointer
                calculate the current sum of the 3 values
                if the sum is 0
                    add the 3 pairs as a list to res
                    
                    # prevent duplicates and continue looking for more triplets
                    while the left pointer is less than the right pointer and its value is the same as the previous value
                        increment the left pointer
                if the sum is greater than 0
                    decrement the right pointer
                else
                    increment the left pointer
                    
        return res
        R - 
        E - The space complexity would be O(n) for the res array. However, the time complexity would be O(n * logn) since we're first sorting nums in ascending order and doing a binary search on each iteration in the for loop.
        """
        
        """
        i = 1, l = 3, r = 4
        
        while loop in the total == 0 if statement doesn't execute, so the inner while loop is infinite with l = 3 and r = 4
        """
        
        nums.sort()
        # print(nums)
        
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # prevent duplicates
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                # print(i, l, r, res)
                m = (l + r) // 2
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1 # prevent infite loop
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
                    
        return res
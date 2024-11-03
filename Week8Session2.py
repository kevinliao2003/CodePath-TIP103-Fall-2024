from collections import defaultdict

def numRabbits(self, answers: List[int]) -> int:
        """
        answers is of at length at least 1
        all answers are >= 0
        
        we want to keep track of the answers
        if 2 rabbits have the same answer, they likely have the same color
        
        plan/implement:
        keep track of a visited set
        set res to 0, which is the count to return
            if answer isn't in visited
                add answer + 1 to res
                add it to visited
        return res
        
        TC: O(n) where n is the size of answers since we're iterating over answers once
        SC: O(n) since the visited set will have at most n elements
        """
        
        """
        also keep track of the frequency of each answer
        each answer could have a max frequency of (answer + 1)
        if answer is 0, add 1 to the counr
        otherwise
            increment the count of the answer
            if the answer is new, add (answer + 1) to res
            else if the answer is in freq and the count is less than (answer + 1), do nothing
            else if the answer is in freq, add (answer + 1) to res 
        """
        
        """
        SOLUTION: greedy approach using a dictionary to keep track of the frequency for each answer
        case 1: the answer is in the dictionary
            decrement the count of the current answer
            if the count is 0
                delete the pair from the dictionary
        case 2: the answer is unique
        if the answer isn't 0, set the count of answer to be answer
        add answer + 1 to res
        """
        
        freq = defaultdict(int)
        res = 0
        for answer in answers:
            if answer in freq:
                freq[answer] -= 1
                if freq[answer] == 0:
                    del freq[answer]
            else:
                if answer != 0:
                    freq[answer] = answer
                res += answer + 1
        return res

def largestNumber(self, nums: List[int]) -> str:
        """
        U - 
        nums has at least 1 element
        all numbers will be at least 0
        M - 
        P/I - 
        use the build in comparator method
        
        first, we want to convert all nums to strings
        afterwards, we run the entire list through the cmp_to_key method
        R - 
        E - 
        Time complexity: O(nlogn) since the most time-consuming operation is the sorting step
        Space complexity: O(n) to convert the int to a string
        """
        
        for i, num in enumerate(nums):
            nums[i] = str(num)
        # print(nums)
        
        def compare(s1, s2):
            if s1 + s2 > s2 + s1:
                return -1
            else:
                return 1
           
        res = "".join(sorted(nums, key=cmp_to_key(compare)))
        return str(int(res)) # remove leading 0s
import heapq

def longestConsecutive(self, nums: List[int]) -> int:
    """
    U  Can nums be empty? Is there guaranteed to be a longest consecutive sequence in increasing order?
    M - Sorting, heap
    P -
    The brute force method would be sorting the array and then checking the longest consecutive sequence.
    
    To optimize, use a heap.
    I -
    initialize the prev number
    initialize the length of the longest sequence and the current sequence
    while the nums is empty
        pop the smallest element using heap pop
        if it is the first element in the sequence
            assign it to the prev number
            continue
        otherwise, check if is greater than the prev number by 1
            update the length of the current sequence
        otherwise
            update the length of the longest sequence
            reset the length of the current sequence
            
        update the previous number
    R - 
    E - 
    TC: O(nlogn) since the heap will have at most n elements and the pop operation is logn
    SC: O(n) since the heap will have at most n elements
    """
    if not nums: # edge case
        return 0
    
    heapq.heapify(nums)
    
    prev = float('inf')
    longest_len, curr_len = 1, 1
    while nums:
        curr_num = heapq.heappop(nums)
        # print(prev, curr_num, curr_len)
        if curr_num == prev:
            continue
        elif curr_num == prev + 1:
            curr_len += 1
        else:
            longest_len = max(longest_len, curr_len)
            curr_len = 1
            
        prev = curr_num
        
    return max(curr_len, longest_len)

def maxProfit(self, prices: List[int]) -> int:
        """
        1. Can prices be empty? Are all the prices positive? Can you sell more than 1 stock on the same day?
        2. Two pointers - neutral, greedy - neutral
        3. To generate profit, we must buy at a lower price and sell at a higher price. However, we cannot buy a stock while still holding onto a stock.
        4.
        initialize res to 0
        loop through prices starting at index 1
            add to res the max of 0 and the difference between the current and previous prices
        return res
        5. See code below.
        6.
        TC: O(n) where n is the size of prices
        SC: O(1)
        """
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i - 1])
        return res

def maxProfit(self, prices: List[int]) -> int:
    """
    1. Are all the prices valid? Can they be negative?
    2. Dynamic programming - neutral
    3. To generate profit, I must buy at a lower price and sell at a higher price on a LATER DAY. I can do this AT MOST 2 times.
    
    For a dynamic programming approach, keep track of the maximum profit at each index.
    4.
    keep track of the cost of the 1st transaction (t1_cost) and the cost of the 2nd transaction (t2_cost)
    keep track of the profit of the 1st transaction (t1_profit) and the profit of the 2nd transaction (t2_cost)
    
    loop through prices
        update t1_cost
        update t1_profit
        update t2_codst
        update t2_profit
    return t2_profit
    
    5. See code below.
    6. O(1) for space complexity and O(n) for time complexity
    """
    
    t1_cost, t2_cost = float('inf'), float('inf')
    t1_profit, t2_profit = 0, 0
    
    for price in prices:
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)
        t2_cost = min(t2_cost, price - t1_profit)
        t2_profit = max(t2_profit, price - t2_cost)
    return t2_profit
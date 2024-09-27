from collections import Counter, deque
import heapq

def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        1. Will the tasks only consist of uppercase English letters?
        2. Heap - likely, two pointers - unlikely
        3. We want to process the most frequent tasks first, and when we process each task, we want to keep track of the next time it will be available. We will continue this until all tasks have been processed.
        4.
        use a counter to get the frequencies of all the tasks
        create a max heap using the values of the counter
        heapify the heap using the heapify method
        
        create a queue that represents the order in which the tasks will be processed
        use the res variable to keep track of the total time
        when either the heap or the queue isn't empty
            increment the res variable
            
            if the heap isn't empty
                pop from the heap
                increment that frequency, since this is a max heap
                if that frequency isn't 0
                    append to the queue the new frequency and the next time it would bew available in the form of a tuple
                    
            # now, check if the cooldown period has elapsed
            if queue is not empty and the leftmost time is equal to the total time elapsed
                append to the heap the leftmost frequency in the queue
        5. See code below.
        6. 
        """
        
        counter = Counter(tasks)
        freqs = [-1 * freq for val, freq in counter.items()]
        heapq.heapify(freqs)
        
        res = 0 # number of intervals to return
        q = deque()
        while q or freqs:
            res += 1
            if freqs:
                curr = heapq.heappop(freqs)
                curr += 1
                if curr != 0:
                    q.append((curr, res + n))
                    
            if q and q[0][1] == res:
                heapq.heappush(freqs, q.popleft()[0])
                
        return res

def leastBricks(self, wall: List[List[int]]) -> int:
        """
        1. Will the rows be of the same or uneven lengths?
        2. Array - likely, two pointers - neutral, dictionary - neutral
        3. Use a dictionary to keep track of the number of bricks at each column position. After iterating through each row, the answer would be the length of the wall minus the maximum number of bricks at a given index.
        4.
        initialize a dictionary
        for each row
            initialize a pos variable to 0
            iterate to the second to last index of the row
                increment the pos variable
                update the count at the current position
                
        return the length of the wall minus the maximum number of bricks at a given index.
        5. See code below.
        6.
        """
        
        dic = defaultdict(int)
        for row in wall:
            pos = 0
            for i in range(len(row) - 1):
                pos += row[i]
                dic[pos] += 1
                
        return len(wall) - max(dic.values()) if len(dic) > 0 else len(wall)

def findCelebrity(self, n: int) -> int:
        """
        1. Can the graph be empty?
        2. Graph - likely
        3. First, determine possible candidates for the celebrity by looping through each person and checking if all other persons know them. From there, pick the celebrity from the pool of candidates.
        4.
        initialize an array to store the candidates
        loop through all persons
            keep track of the candidate variable to see if the current person could be a celebrity
            loop through all other persons
                if the candidate knows the other person
                    set the candidate variable to false
                    exit the loop
                    
            if the candidate variable is true, add that candidate to the array
            
        loop through all candidates
            keep track of the celebrity variable to see if the current person could be a celebrity
            loop through all other persons
                if the other person does not know the celebrity
                    se the celebrity variable to false
                    exit the loop
                    
            if the celebrity variable is true
                return that candidate
                
        return -1
        5. See code below.
        6.
        """
        
        candidates = []
        for p1 in range(n):
            candidate = True
            for p2 in range(n):
                if p1 != p2 and knows(p1, p2):
                    candidate = False
                    break
                    
            if candidate:
                candidates.append(p1)
                
        for candidate in candidates:
            celebrity = True
            for p in range(n):
                if candidate != p and not knows(p, candidate):
                    celebrity = False
                    break
                    
            if celebrity:
                return candidate
            
        return -1
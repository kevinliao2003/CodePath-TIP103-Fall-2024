class RecentCounter:
    
    """
    Time complexity: O(n) for iterating over the queue
    Space complexity: O(n) for the queue
    """

    def __init__(self):
        """
        here, we want to initialize the data structure or class with 0 recent requests
        
        Pseudocode:
        initialize a queue (self.q) to deque()
        we want to initialize the current count to 0
        """
        
        self.q = deque()

    def ping(self, t: int) -> int:
        """
        add a new request at time t
        we want to return the number of requests in the past 3000 milliseconds, so the interval [t - 3000, t]
        GUARANTEED that every call to ping has a t value strictly larger than the previous t value
        
        we are adding to the end but popping from the start
        so a queue may come in handy here
        
        Pseudocode:
        add t to the end of the queue
        while q is not empty and the last element is NOT in the [t - 300, t] range
            pop it from the queue
            increment the current count
        return the length of the queue
        """

        self.q.append(t)
        while self.q and not (t - 3000 <= self.q[0] <= t):
            self.q.popleft()
        return len(self.q)
    
class MyQueue:
    
    """
    1. Will all the input be valid? Can I use 1 stack or are 2 stacks required?
    2. Stack - likely
    3. 
    For init, initialize 2 empty stacks (stack1, stack2)
    For push, append the element to stack1.
    For pop, while popping each element from stack1, append it to stack2. Pop from stack2 and set that as the element to return. From there, while popping each element from stack2, append it to stack1. Return that element.
    For peek, while popping each element from stack1, append it to stack2. Pop from stack2 and set that as the element to return. From there, while popping each element from stack2, appned it to stack1. Append the element to return to stack1 and return that element.
    For empty, return true if stack1 is of length 0 and false otherwise
    4.
    def __init__(self):
        initialize stack1 to be an empty stack
        initialzie stack2 to be an empty stack
    
    def push(x):
        append x to stack1
        
    def pop():
        while stack1 is not empty
            pop from stack1 and append that element to stack2
        set a variable res to the popped value from stack2
        while stack2 is not empty
            pop from stack2 and append that element to stack1
        return res
        
    def peek():
        while stack1 is not empty
            pop from stack1 and append that element to stack2
        set a variable res to the popped value from stack2
        while stack2 is not empty
            pop from stack2 and append that element to stack1
        append res to stack1
        return res
        
    def empty():
        return true if stack1 is of length 0 and false otherwise
    5. See code below.
    6. 
    """

    def __init__(self):
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        # print('pop before', self.stack1)
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        # print('pop after', self.stack1)
        return res

    def peek(self) -> int:
        # print('peek before', self.stack1)
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        # print('peek after', self.stack1)
        return res

    def empty(self) -> bool:
        return len(self.stack1) == 0
    
def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        U - 
        given an input of pushed and popped lists, return a boolean
        pushed and popped will have at least 1 integer
        pushed and popped are of equal length
        the values in pushed and popped are at least 0
        all elements of pushed are unique
        M - stack
        P/I - 
        Example 1: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        stack = [1, 2, 3]
        pop 4,
        push 5 -> stack = [1, 2, 3, 5]
        pop 5
        pop 3, 2, 1
        popped = [4, 5, 3, 2, 1]
        
        Example 2: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
        stack = [1, 2]
        pop 4, pop 3
        push 5 -> stack = [1, 2, 5]
        pop 5 -> stack = [1, 2]
        1 cannot be popped before 2, so return False
        
        we want to keep track of another list called stack
        as we iterate through pushed, we add that element to the stack
        when the last element of the stack is equal to the current element of popped, we pop from the stack. we continue doing this until the 2 elements are equal.
        afterwards, we increment the pointer in the popped list
        after the iterations, we return true if stack is empty and false otherwise
        
        Pseudocode:
        set stack to []
        set popped_idx to 0
        loop through pushed
            add the number to the stack
            while stack is not empty and the last element in the stack is equal to popped[popped_idx]
                pop from the stack
                increment popped_idx
                
        return true if stack is empty and false otherwise
        R - 
        E - 
        Time complexity: O(n) since we're iterating over pushed at most once
        Space complexity: O(n) for the stack since the stack will have at most n elements
        """
        
        stack = []
        popped_idx = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[popped_idx]:
                stack.pop()
                popped_idx += 1
                
        return not stack

def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        U - 
        The input will have a length of at least 2
        no asteroid has a value of 0
        the asteroids can be positive or negative
        
        positive - right, negative - left
        absolute value is the size
        M - 
        P/I - 
        we want to continue iterating through asteroids until there are no more collisions, so either when all the values are positive or negative
        
        Example 1: asteroids = [5,10,-5]
        we check indices 0 and 1
            both are positive -> do nothing
        we check indices 1 and 2
            -5 explodes, so we're left with 5 and 10
        the remaining asteroids are both positive, so do nothing
        
        Pseudocode:
        while True
            set collision to False # if there is a collision in the current iteration
            set new_asteroids to [] # after collisions
            for every 2 asteroids
                set asteroid1 to the current asteroid
                set asteroid2 to the next asteroid
                if asteroid1 and asteroid2 are both positive or both negative
                    add both asteroid1 and asteroid2 to new_asteroids
                else if the abs value of asteroid1 is the same as that of asteroid2
                    set collision to True
                else if the abs value of asteroid1 is greater than that of asteroid2
                    add asteroid1 to new_asteroids
                    set collision to True
                else if the abs value of asteroid2 is greater than that of asteroid1
                    add asteroid2 to new_asteroids
                    set collision to True
                
            set asteroids to new_asteroids
            if there was no collision or asteroids has a length less than 2
                return new_asteroids
                
        Example 1: asteroids = [5,10,-5]
        collision = True
        new_asteroids = [5, 10]
        asteroid1 = 10
        asteroid2 = -5
        R - 
        E - 
        """
        
        """
        SOLUTION: stack approach
        - this should be a single pass through the list
        
        Pseudocode:
        set stack to []
        loop through asteroids
            while the stack isn't empty and the asteroid is negative and the last value in the stack was positive
                get the difference between the last element in the stack and current asteroid
                if the difference is 0
                    pop the last element
                    set the current asteroid to 0
                if the difference is greater than 0
                    set the current asteroid to 0
                if the difference is less than 0
                    pop the last element
                    
            append the current asteroid to the stack if it is not 0
            
        Example 1: asteroids = [5,10,-5]
        stack = [5, 10]
        asteroid = 10, return [5, 10]
        
        Example 2: asteroids = [8,-8]
        stack = []
        asteroid = 0, return []
        
        Example 3: asteroids = [10,2,-5]
        stack = [10]
        asteroid = -5, return [10]
        
        Time complexity: O(n) for iterating through asteroids
        Space complexity: O(n) for the stack
        """
        
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = stack[-1] + asteroid
                if diff == 0:
                    stack.pop()
                    asteroid = 0 # no more collisions
                elif diff > 0:
                    asteroid = 0 # no more collisions
                elif diff < 0:
                    stack.pop()
                # print(asteroid, diff, stack)
                    
            if asteroid:
                stack.append(asteroid)
                
        return stack

def calculate(self, s: str) -> int:
        """
        1. Will the string always be a valid expression? Do I have to account for invalid input? Would I have to worry about multiplication or division?
        2. Stack - likely
        3.
        initialize an empty stack
        initialize a current number (curr_num)
        initialize a sign (1 for positive, -1 for negative)
        initialize a res variable
        iterate over the string
            if the char is a digit
                update curr_num (multiply the curr_num by 10 and add the value)
            if the char is a + or -
                add curr_num to the res (adjusting the sign if necessary)
                reset the curr_num
                update the sign
            if the char is a '('
                append the res to the stack
                append the sign to the stack
                reset the res
                reset the sign
            if the char is a ')'
                update the res variable
                multiply the res with the sign on top of the stack
                add the next popped element to the res
                reset the res variable
                
        return the sum of res and (curr_num * sign)
        4.
        5. See code below.
        6.
        """
        
        stack = []
        curr_num = 0
        sign = 1
        res = 0 # result to return
        for c in s:
            if c.isdigit():
                curr_num = (curr_num * 10) + int(c)
            elif c in '-+':
                res += (curr_num * sign)
                curr_num = 0
                
                if c == '-':
                    sign = -1
                else:
                    sign = 1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += (curr_num * sign)
                res *= stack.pop() # pop the sign
                res += stack.pop() # pop the number
                curr_num = 0
               
        return res + (curr_num * sign)
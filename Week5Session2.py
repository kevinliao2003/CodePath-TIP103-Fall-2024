def numTrees(self, n: int) -> int:
        """
        1. Is n always going to be a positive integer? Is n going to be very large, very small?
        2. Trees - likely, dynamic programming - neutral
        3. 
        Use dynamic programming. Initialize a dp array of size (n + 1) with the values at indices 0 and 1 set to 1. Each index in the array represents the number of trees that can be created with that number of unique nodes.
        
        To construct a unique BST, we need to construct a subtree of its left sequence and another out of its right subsequence and then combine them. Thus, use a nested loop - outer loop iterates from index 2 to n and the inner loop iterates from index 0 to (i + 1). In the inner loop, update the value at the outer loop index.
        4.
        initialize dp array
        initialize values at indices 0 and 1 to be 1
        iterate from indices 2 to n + 1 (index i)
            iterate from indices 0 to i + 1 (index j)
                update the value at index i to be the sum of the current value plus the product of the values at indices (i - j) and (j - 1).
                
        return the value of the last index
        5. See code below.
        6.
        """
        
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[-1]

def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        1. Is the root always valid? Can it be None?
        2. Trees - likely, recursion - likely, bfs - neutral
        3. Start at the root node and call the function recursively on the left and right subtrees. At the end, return the smaller between the depths of the left and right subtrees.
        4.
        
        define a helper method
            if root is valid and there exists no right and no left subtree
                return 0
                
            call the method recursively on the left subtree and assign its value to the variable left_depth + 1
            call the method recursively on the right subtree and assign its value to the the variable right_depth + 1
            return the minimum of left_depth and right_depth
        5. See code below.
        6. 
        """
        
        if not root: # base case
            return 0
        
        def helper(root):
            if not root or (root and not root.left and not root.right):
                return 0
            elif root and root.left and root.right:
                return min(helper(root.left) + 1, helper(root.right) + 1)
            elif root and root.left:
                return helper(root.left) + 1
            elif root and root.right:
                return helper(root.right) + 1
        
        return helper(root) + 1 # + 1 for the root

def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        U - 
        the tree has at least 1 node
        every node has at most 2 children
        the node values are either 0 or 1
        M - dfs
        P/I - 
        if the current node has a value of 1, do nothing and recurse on the left and right subtrees
        otherwise, if the current value is 0, check if the left or right subrrees contain a value of 1. if not, set the node to None
        we only want to call the contains1 helper method if the current node is 0
        
        # check if the current subtrees contains 1s
        define a helper method called contains1 (parameters: node)
            if not node
                return False
            if node.val is 1
                return True
            return contains1(node.left) or contains1(node.right)
        
        define a helper method called dfs (parameters: node)
            if not node
                return
            if the node has a value of 1
                recurse left
                recurse right
            if the node has a value of 0 and doesn't contain any 1s
                set node to None # prune it
                
        call the dfs helper method on the root node
        return root
        R - 
        E - 
        Time complexity: O(n) since the call stack will have at most n elements where n is the number nodes in the tree
        Space complexity: O(logn) if the tree is balanced and O(n) if the tree is unbalanced
        """
        
        def contains1(node):
            if not node:
                return False
            if node.val == 1:
                return True
            return contains1(node.left) or contains1(node.right)
        
        def dfs(node):
            if not node or not contains1(node):
                return None
            
            if not contains1(node.left):
                node.left = None
            if not contains1(node.right):
                node.right = None 
                
            dfs(node.left)
            dfs(node.right)
            return node

        return dfs(root)
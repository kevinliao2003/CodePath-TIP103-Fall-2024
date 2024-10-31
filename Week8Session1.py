from collections import defaultdict

def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        accounts has a size of at least 1
        each account has a name and at least 1 address
        
        we want to merge the accounts
        2 accounts belong to the same person if there is a common email in both accounts
        even if 2 accounts have the same name, they may belong to different people
        
        we could use a graph to represent this relation
        we use an undirected graph and have email1 point to email2 if they belong to the same person
        
        "johnsmith@mail.com" -> ["john_newyork@mail.com", "john00@mail.com"]
        "john_newyork@mail.com" -> ["johnsmith@mail.com"]
        "john00@mail.com" -> ["johnsmith@mail.com"]
        
        plan/implement:
        create the adjacency list
        
        define a visited set
        define a recursive dfs function (email)
            if the email has been visited
                return
                
            add email to the visited set
            add email to the list of emails for the current person
                
            for each neighbor of email 
                call dfs on the email
        
        set res to [] # merged accounts to return
        loop through the accounts
            loop through the emails
                set the list of emails for the current person to []
                call dfs on the email
            
            add the list of emails to res
        return res
        
        TC: O(m * n) since we're visiting each email at most once
        SC: O(m * n) where m is the number of accounts and n is the largest size of an account
        """
        
        adj = defaultdict(set)
        for account in accounts:
            emails = account[1:]
            for i in range(len(emails)):
                for j in range(i + 1, len(emails)):
                    adj[emails[i]].add(emails[j])
                    adj[emails[j]].add(emails[i])
        
        visited = set()
        def dfs(email):
            if email in visited:
                return
            
            visited.add(email)
            self.curr.append(email)
            
            for nei in adj[email]:
                dfs(nei)
                
        res = [] # merged accounts to return
        for account in accounts:
            emails = account[1:]
            self.curr = []
            for email in emails:
                dfs(email)
                
            if self.curr:
                self.curr.sort() # sort accounts in order
                res.append([account[0]] + self.curr)
            
        return res

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        the number of nodes in the tree is at least 0
        the node values are integers and can be positive or negative

        return all root-to-leaf paths where the sum of the node values in the path equals targetSum

        plan/implement:
        we want to define 2 lists: the paths to return and the currnet path
        write a recursive dfs function that takes in a node and the current sum
        when we reach a laf node and the current sum is equal to targetSum
        -> add the current path to the paths to return
        -> backtrack by popping the last element from the current path

        afterwards, call the dfs function on the left and right subtrees

        TC: O(n^2) where n is the number of nodes in the tree
        -> in the worst case we have n/2 leafs
        -> this will require a O(n) operation to copy over the nodes to a new list
        SC: O(n) 
        """

        res = [] # paths to return
        curr = [] # current level
        
        def dfs(node, curr):
            if not node:
                return
            
            currSum = sum(curr)
            if not node.left and not node.right and currSum + node.val == targetSum:
                curr.append(node.val)
                res.append(curr.copy())
                curr.pop() # backtrack
                
            dfs(node.left, curr + [node.val])
            dfs(node.right, curr + [node.val])
            
        dfs(root, [])
        return res
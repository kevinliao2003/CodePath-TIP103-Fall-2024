class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

# PROBLEM 1
def findCircleNum(isConnected):
    """
    1. Is the input always going to be valid
    2. Graphs - likely, union-find - likely
    3. For each pair of node, use the union-find algorithm to see if those 2 nodes can be joined. If so, increment the count
    4.
    define an array called ranks
    define an array called parents

    define a function called find that takes in a node parameter
        set the current node to the parameter
        while the node is not equal to it's parent
            set the parent of the node to the grandparent of the node
            set the current node to the parent node from above
        return the current node

    define a function called union that takes in 2 node parameteters (node1, node2)
        call the find function above for the 2 nodes and name them curr1, curr2

        if curr1 equals curr2
            return false

        if the rank of curr1 is greater than that of curr2
            set the parent of curr2 to be curr1
            increase the rank of curr1 by the rank of curr2
        otherwise
            set the parent of curr1 to be curr2
            increase the rank of curr2 by the rank of curr1

        return true
    5. See code below.
    6. The space complexity is O(n) since we're using the parent and rank arrays. Moreover, the time complexity would be O(n^2), since we need to iterate over all values in isConnected twice.
    """

    n = len(isConnected)
    ranks = [1] * n
    parents = [node for node in range(0, n)]

    def find(node):
        curr = node
        while curr != parents[curr]:
            parents[curr] = parents[parents[curr]]
            curr = parents[curr]
        return curr

    def union(node1, node2):
        curr1, curr2 = find(node1), find(node2)

        if curr1 == curr2:
            return False

        if ranks[curr1] > ranks[curr2]:
            parents[curr2] = curr1
            ranks[curr1] += ranks[curr2]
        else:
            parents[curr1] = curr2
            ranks[curr2] += ranks[curr1]

        return True

    res = n # number of provinces to return
    for node1 in range(n):
        for node2 in range(n):
            if isConnected[node1][node2] and union(node1, node2):
                res -= 1

    return res

# PROBLEM 2
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    """
    1. Can any of the nodes be empty or invalid?
    2. Graphs - likely, dfs - likely
    3. Use a dictionary to map an original node to its cloned node and perform a dfs on the graph.
    4. 
    initialize an empty dictionary

    define a helper method that takes in node as a parameter
        if the node is in the dictionary
            return it

        map the original node to its cloned node
        iterate through the neighbors
            for the cloned node, add to its neighbors, recursively calling the function on each of the neighbors

        return the cloned node
    5. See code below.
    6. The time complexity is O(N + M) where N is the number of nodes and M is the number of edges. The space complexity is O(N) since we're using a hash map and a stack for the recursion.
    """
    if not node:
        return None

    dic = {}

    def dfs(node):
        if node in dic:
            return dic[node]

        copy = Node(node.val)
        dic[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    dfs(node)
    return dic[node]
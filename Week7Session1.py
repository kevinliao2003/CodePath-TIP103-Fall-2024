from collections import defaultdict

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        1. Can I assume that the prerequisites will be valid courses?
        2. Graphs - likely, dfs - likely
        3. The goal of this problem should be to detect a cycle. If there is a cycle in the graph, we cannot take all the courses. Otherwise, we should be able to take all the courses.
        4.
        initialize an empty adjacency list using a dictionary
        loop through the prerequisites (a, b)
            append b to the list at a
            
        initialize an empty cycle set
        initialize an empty visited set
        initialize an empty res array
        define a helper dfs function (parameter: course)
            if the course is in the cycle
                return false
            if the course has been visited
                return true
                
            add the course to the cycle
            add the course to visited
            for all the prereqs of the current course
                if the course can't be completed
                    return false
            remove the course from the cycle
            add the course to res
            
        loop through the courses
            if dfs returns false
                return an empty array
        return res
        5. See code below.
        6. 
        Time complexity - O(V + E) where V is the number of vertices and E is the number of edges
        Space complexity - O(V + E)
        """
        
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
            
        cycle = set()
        visited = set()
        res = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            visited.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            
            cycle.remove(course)
            res.append(course)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        1. Will all the prereqs be valid in relation to the number of courses?
        2. Graphs - likely, topological sort - likely
        3. We could use topological sort to solve this problem.
        4.
        initialize a visited set
        initialize an adjacency list
        initialize a boolean array called is_source and by default each value is true for each course
        
        initialize a dictionary called reachable for the prerequisites
        
        define a helper dfs function (course)
            add the course to the visited set
            for each neighbor of the course
                add that neighbor to the list of the course at reachable
                if the neighbor hasn't been visited yet
                    call dfs on that neighbor
                add all courses that are reachable by the neighbor to that of course
            return
        
        loop through the prereqs (pre, post)
            append post to the list at pre
            set the value of is_source at post to false
            
        loop through all the course numbers
            if is_source at the course number is true
                call dfs of that course
                
        initialize a res array
        loop through the queries (course, prereq)
            append to res if prereq is in the list of reachable courses for course
        return res
        5. See code below.
        6. 
        Time complexity - O(V + E) where V is the number of vertices and E is the number of edges
        Space complexity - O(V + E)
        """
        
        visited = set()
        adj = defaultdict(list)
        is_source = [True] * numCourses
        reachable = defaultdict(set)
        
        for pre, post in prerequisites:
            adj[pre].append(post)
            is_source[post] = False
            
        def dfs(course):
            visited.add(course)
            for nei in adj[course]:
                reachable[course].add(nei)
                if nei not in visited:
                    dfs(nei)
                reachable[course].update(reachable[nei])
            return
            
        for course in range(numCourses):
            if is_source[course]:
                dfs(course)
                
        return [j in reachable[i] for i, j in queries]

def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        1. Are all the edges valid? Are they all unique?
        2. Graphs - likely, topological sort - likely
        3. 
        In topological sort, we start from the nodes that have no incoming edges, and for each edge (a goes to b), a comes before b in the ordering.
        
        If the number of nodes is even, there will be 2 nodes with the minimum height.
        If the number of nodes is odd, there will only be 1 node with the minimum height.
        4. 
        if n is less than 2
            return a list of all nodes up to n
            
        initialize an empty adjacent list
        loop through edges (a, b)
            add b to the list of a
            add a to the list of b
            
        initialize an empty variable called leaves to store the leaf nodes
        for each node in range n
            if it only has 1 neighbor
                add it to the leaves
                
        initialize the number of remaining nodes to be n
        while the number of remaining nodes is greater than 2
            subtract the number of remaining nodes by the number of leaves
            initialize a list for the new leaves
            while there are remaining leaves
                pop from the leaves (curr)
                remove the rightmost neighbor for that leaf
                remove the leaf as a neighbor for that neighbor
                if that neighbor only has 1 leaf left
                    add that neighbor to the new leaves list
                    
            set the leaves to be the new leaves
            
        return the leaves
        5. See code below.
        6. 
        Time complexity: O(V)
            V - 1 iterations to construct the graph given the edges
            retrieving the leaf nodes takes V steps
        Space complexity: O(V)
            we construct the graph with the adjacency list with V nodes and V - 1 edges
        """
        
        if n <= 2:
            return [i for i in range(n)]
        
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
            
        leaves = []
        for node in range(n):
            if len(adj[node]) == 1:
                leaves.append(node)
                
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
            
        return leaves

def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        U - 
        all tickets will be in the format [from, to]
        each airport will only be 3 characters long
        the itinerary must begin with "JFK"
        the itinerary with the smallest lexical order will be returned
        there will be AT LEAST 1 valid itinerary
        M - dfs, topological sort
        P/I - 
        first, we weant to build an adjacency list for the tickets
        afterwards, we want to sort all the neighbors for the airports in the adjacency list

        for each node, we also want to keep track if we've visited the neighbor
        -> this can be done with a dictionary where the key is the airport and the value is a list of booleans

        define a recursive helper function (parameters: node, route)
            if the length of the route is equal to len(tickets) + 1
                set the result to the route
                return True

            loop through the neighbors
                if the neighbor hasn't been visited
                    mark the neighbor as visited
                    call the helper function on the neighbor
                    mark the neighbor as not visited

        call the helper function on "JFK" with the route starting with "JFK"
        return the result
        R - 
        E - 
        Time complexity: O(E^d) where E is total number of flights and d is the maximum number of flights from an airport
            at each position, we have d choices
            in the worst case scenario, the backtracking algorithm would have to enumerate all possible combinations
        Space complexity: O(V + E) where V is the number of airports and E is the number of flights
        """

        #build adjacency list
        adj = defaultdict(list)
        for a, b in tickets:
            adj[a].append(b)

        visited = {}
        for k, v in adj.items():
            v.sort()
            visited[k] = [False] * len(v)

        #dfs function
        self.res = []
        def dfs(node, route):
            if len(route) == len(tickets) + 1:
                self.res = route
                return True

            for i, nei in enumerate(adj[node]):
                if not visited[node][i]:
                    visited[node][i] = True
                    tmp = dfs(nei, route + [nei])
                    visited[node][i] = False
                    if tmp:
                        return True
            return False

        dfs('JFK', ['JFK'])
        return self.res
from collections import defaultdict
import heapq

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        1, Is the source node k guaranteed to exist inte graph? Will the time always be positive?
        2. Graphs - likely, neutral - neutral
        3. Perform a bfs starting at node k. At the end of each level, add the largest time to the result.
        4. 
        initialize an empty adjacency list
        loop through times (source, target, weight)
            add the (target, weight) to the list at source in the form of a tuple
            
        initialize an empty heap (source node k, current weight of 0)
        initialize an empty visited set
        initialize a res variable
        while the queue isn't empty
            pop from the heap and retrieve the node and weight
            update the res variable accordingly
            for each neighbor of the node
                if the neighbor hasn't been visited
                    add the neighbor and UPDATED weight to the heap in the form of a tuple
                    add the neighbor to the visited set
            
        return res
        5. See code below.
        6. 
        Time complexity: 
        - O(E) to loop through the edges to build the adjacency list
        - O(E) to loop through the tuples in the heap
        Space complexity: 
        - O(V + E) where V is the number of nodes and E is the number of edges for the adjacency list
        - O(E) for the heap
        """
        
        adj = defaultdict(list)
        for source, target, weight in times:
            adj[source].append((target, weight))
            
        heap = [(0, k)]
        visited = set()
        res = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            visited.add(node)
            res = max(res, weight)
            for nei_node, nei_weight in adj[node]:
                if nei_node not in visited:
                    heapq.heappush(heap, (weight + nei_weight, nei_node))
            
        return res if len(visited) == n else -1

def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        1. Could the graph contain unconnected components?
        2. Graphs - likely, union find - neutral
        3. Call the union find method on each of the edges and if the method returns false, update the edge that can be removed. Return the edge at the end after all edges have been processed.
        4.
        initialize a ranks array for all the nodes
        initialize a parents array for all the nodes
        
        define a find method (node)
            initialize node to curr
            while curr is not equal to its parent
                set the parent of curr to its grandparent
                set curr to its parent
            return curr
            
        define a union method (node1, node2)
            call find on node1 and node2 and set the result to res1 and res2
            
            if res1 equals res2
                return false
                
            if the rank of res1 is greater than that of res2
                add the rank of res2 to the rank of res1
                update the parent of res2 to res1
            else
                add the rank of res1 to the rank of res2
                update the parent of res1 to res2
                
            return true
            
        initialize the res (edge to return)
        loop through all the edges
            call the union method on the edge and if it returns false
                set res to that edge
        return res
        5. See code below.
        6. 
        Time complexity: 
        O(n) where n is the number of vertices
        Space complexity: O(n) where n is the number of nodes to account for the ranks and parents lists
        """
        n = len(edges)
        ranks = [1] * (n + 1)
        parents = [node for node in range(0, n + 1)]
        
        # outputs a unique id so that 2 nodes have the same id if and only if they are in the same connected component
        def find(node):
            curr = node
            while curr != parents[curr]:
                parents[curr] = parents[parents[curr]]
                curr = parents[curr]
            return curr
        
        def union(node1, node2):
            # draws an edge between the components with find(node1) and find(node2)
            res1, res2 = find(node1), find(node2)
            
            if res1 == res2:
                return False
            
            if ranks[res1] > ranks[res2]:
                ranks[res1] += ranks[res2]
                parents[res2] = res1
            else:
                ranks[res2] += ranks[res1]
                parents[res1] = res2
                
            return True
        
        res = []
        for a, b in edges:
            if not union(a, b):
                res = [a, b]
        return res
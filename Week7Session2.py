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
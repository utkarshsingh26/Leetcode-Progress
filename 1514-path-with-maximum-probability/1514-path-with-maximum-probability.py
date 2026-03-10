class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        max_heap = [(-1, start_node)] # prob, node
        best = {} # node = prob

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob

            if node == end_node:
                return prob
            
            if node in best and best[node] >= prob:
                continue
            
            best[node] = prob

            for neighbor, neighbor_prob in graph[node]:
                new_prob = prob * neighbor_prob
                heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0
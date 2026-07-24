import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        heap = [(0,k)] # time, node
        min_times = {}

        while heap:
            time, node = heapq.heappop(heap)
            
            if node in min_times:
                continue
            
            min_times[node] = time

            for neighbor in graph[node]:
                if neighbor[0] not in min_times:
                    new_time = time + neighbor[1]
                    heapq.heappush(heap, (new_time, neighbor[0]))
        
        if len(min_times) != n:
            return -1
        
        return max(min_times.values())
        

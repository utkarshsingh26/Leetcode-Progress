import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        min_times = {} # node = time
        min_heap = [(0,k)] # time, node

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in min_times:
                continue
            
            min_times[node] = time

            for neighbor, neighbor_time in graph[node]:
                new_time = time + neighbor_time
                heapq.heappush(min_heap, (new_time, neighbor))

        if len(min_times) != n:
            return -1
        else:
            return max(min_times.values())


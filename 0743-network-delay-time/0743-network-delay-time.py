import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u,v,time in times:
            graph[u].append((v,time))
        
        min_times = {} # node = time
        min_heap = [(0,k)] # time from source to node, node

        while min_heap:
            time_k_to_i, node = heapq.heappop(min_heap)
            if node in min_times:
                continue
            min_times[node] = time_k_to_i

            for neighbor, neighbor_time in graph[node]:
                heapq.heappush(min_heap, (neighbor_time + time_k_to_i, neighbor))
        
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1
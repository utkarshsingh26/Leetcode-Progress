import heapq
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        directions =[(0,1), (0,-1), (1,0), (-1,0)]
        min_heap = [(0,0,0,0)] # steps, row, column, obstacles_used
        visited = set()

        while min_heap:
            steps, row, column, obstacles_used = heapq.heappop(min_heap)

            if row == rows-1 and column == columns-1:
                return steps
            
            if obstacles_used > k:
                continue
            
            if (row, column, obstacles_used) in visited:
                continue
            
            visited.add((row, column, obstacles_used))

            for dr, dc in directions:
                nr, nc = row + dr, column + dc
                new_obstacles_used = obstacles_used + 1

                if 0 <= nr < rows and 0 <= nc < columns and (nr, nc, new_obstacles_used) not in visited:

                    # respect the obstacle
                    if grid[nr][nc] == 0:
                        new_steps = steps + 1
                        heapq.heappush(min_heap, (new_steps, nr, nc, obstacles_used))

                    # destroy the obstacle
                    if grid[nr][nc] == 1 and new_obstacles_used <= k:
                        new_steps = steps + 1
                        heapq.heappush(min_heap, (new_steps, nr, nc, new_obstacles_used))
        
        return -1
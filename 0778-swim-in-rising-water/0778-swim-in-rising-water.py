import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        min_heap = [(grid[0][0], 0, 0)] # time, row, column
        visited = set()

        while min_heap:
            time, row, column = heapq.heappop(min_heap)

            if row == rows-1 and column == columns-1:
                return time
            
            if (row, column) in visited:
                continue
            
            visited.add((row, column))

            for dr, dc in directions:
                nr, nc = row + dr, column + dc

                if 0 <= nr < rows and 0 <= nc < columns and (nr,nc) not in visited:
                    new_time = max(grid[nr][nc], time)
                    heapq.heappush(min_heap, (new_time, nr, nc))
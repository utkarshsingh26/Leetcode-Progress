from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        maxArea = 0
        visited = set()

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            area = 1

            while queue:
                row, column = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        area += 1
            
            return area

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxArea = max(area, maxArea)
        
        return maxArea

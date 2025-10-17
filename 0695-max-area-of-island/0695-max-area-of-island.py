from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        max_area = 0
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(r,c):
            area = 1
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                row, column = queue.popleft()

                for dr,dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            
            return area

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area
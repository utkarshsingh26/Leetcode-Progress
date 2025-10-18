from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = [0]
        queue = deque()

        rows = len(grid)
        columns = len(grid[0])

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    freshOranges[0] += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        if freshOranges[0] == 0 and not queue:
            return 0
        
        def bfs(queue):
            minutes = 0
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            while queue:
                for _ in range(len(queue)):
                    row, column = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = dr + row, dc + column

                        if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr,nc))
                            freshOranges[0] -= 1
                minutes += 1
            
            if freshOranges[0] == 0:
                return minutes - 1
            else:
                return -1
        
        return bfs(queue)

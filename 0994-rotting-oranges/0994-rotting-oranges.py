from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        fresh = [0]

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh[0] += 1
        
        if fresh[0] == 0:
            return 0
        
        def bfs(queue):
            minutes = 0
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            while queue:
                level_length = len(queue)
                for _ in range(level_length):
                    row, column = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, column + dc

                        if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh[0] -= 1
                            queue.append((nr, nc))
                minutes += 1
            
            return minutes-1 if fresh[0] == 0 else -1
        
        return bfs(queue)
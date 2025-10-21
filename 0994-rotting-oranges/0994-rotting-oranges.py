from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        fresh = [0]
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh[0] += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        if not queue and fresh[0] == 0:
            return 0
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(queue):
            minutes = 0
            while queue:
                level = []
                level_length = len(queue)

                for _ in range(level_length):
                    row, column = queue.popleft()
                    
                    for dr, dc in directions:
                        nr, nc = row + dr, column + dc

                        if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr,nc))
                            fresh[0] -= 1
                
                minutes += 1

            return minutes-1 if fresh[0] == 0 else -1
        
        return bfs(queue)

        
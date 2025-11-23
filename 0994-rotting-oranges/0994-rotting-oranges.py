from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        queue = deque()
        fresh = [0]
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh[0] += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        if fresh[0] == 0:
            return 0
        
        def bfs(queue, visted):
            minutes = 0

            while queue:
                for _ in range(len(queue)):
                    row, column = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = row + dr, column + dc

                        if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1 and (nr, nc) not in visited:
                            fresh[0] -= 1
                            grid[nr][nc] == 2
                            visited.add((nr,nc))
                            queue.append((nr,nc))
                minutes += 1

            return minutes-1 if fresh[0] == 0 else -1
        
        return bfs(queue, visited)
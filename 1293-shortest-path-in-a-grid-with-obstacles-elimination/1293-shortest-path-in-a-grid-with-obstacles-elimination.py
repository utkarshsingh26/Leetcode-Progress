from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        if k >= rows + cols - 2:
            return rows + cols - 2

        queue = deque([(0, 0, 0, 0)])  # row, col, steps, obstacles_used
        visited = set([(0, 0, 0)])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            row, col, steps, used = queue.popleft()

            if row == rows - 1 and col == cols - 1:
                return steps

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_used = used + grid[nr][nc]

                    if new_used <= k and (nr, nc, new_used) not in visited:
                        visited.add((nr, nc, new_used))
                        queue.append((nr, nc, steps + 1, new_used))

        return -1
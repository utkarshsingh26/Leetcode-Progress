from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        columns = len(heights[0])

        atlantic_queue = deque()
        atlantic_set = set()

        pacific_queue = deque()
        pacific_set = set()

        for r in range(rows):
            for c in range(columns):
                if (r == 0 or c == 0):
                    pacific_queue.append((r,c))
                    pacific_set.add((r,c))
                if (r == rows-1 or c == columns-1):
                    atlantic_queue.append((r,c))
                    atlantic_set.add((r,c))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(queue, visited):
            while queue:
                row, column = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and heights[nr][nc] >= heights[row][column] and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
        
        bfs(pacific_queue, pacific_set)
        bfs(atlantic_queue, atlantic_set)

        return list(pacific_set & atlantic_set)
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_seen = set()
        pacific_queue = deque()

        atlantic_seen = set()
        atlantic_queue = deque()

        rows = len(heights)
        columns = len(heights[0])

        for c in range(columns):
            pacific_seen.add((0,c))
            pacific_queue.append((0,c))
        
        for r in range(rows):
            pacific_seen.add((r,0))
            pacific_queue.append((r,0))
        
        for c in range(columns):
            atlantic_seen.add((rows-1,c))
            atlantic_queue.append((rows-1,c))
        
        for r in range(rows):
            atlantic_seen.add((r,columns-1))
            atlantic_queue.append((r,columns-1))
        
        def bfs(queue, visited):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while queue:
                row, column = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + column

                    if 0 <= nr < rows and 0 <= nc < columns and heights[nr][nc] >= heights[row][column] and (nr, nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))

        
        bfs(atlantic_queue, atlantic_seen)
        bfs(pacific_queue, pacific_seen)

        return list(atlantic_seen & pacific_seen)

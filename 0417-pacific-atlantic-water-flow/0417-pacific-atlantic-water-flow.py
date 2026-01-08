from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        columns = len(heights[0])

        pacific_set = set()
        atlantic_set = set()
        pacific_queue = deque()
        atlantic_queue = deque()

        for c in range(columns):
            pacific_queue.append((0,c))
            pacific_set.add((0,c))
            
        for r in range(rows):
            pacific_queue.append((r,0))
            pacific_set.add((r,0))
        
        for c in range(columns):
            atlantic_queue.append((rows-1,c))
            atlantic_set.add((rows-1,c))
        
        for r in range(rows):
            atlantic_queue.append((r, columns-1))
            atlantic_set.add((r, columns-1))
        
        def bfs(queue, visited):

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            while queue:
                row, column = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited and heights[nr][nc] >= heights[row][column]:
                        visited.add((nr,nc))
                        queue.append((nr,nc))

        bfs(pacific_queue, pacific_set)
        bfs(atlantic_queue, atlantic_set)

        return list(pacific_set & atlantic_set)
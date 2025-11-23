from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        columns = len(board[0])

        visited = set()
        
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            while queue:
                row, column = queue.popleft()

                for dr,dc in directions:
                    nr, nc = dr + row, dc + column

                    if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] == "O" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O" and (r == 0 or r == rows-1 or c == 0 or c == columns-1):
                    bfs(r,c)
        
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O" and (r,c) not in visited and not (r == 0 or r == rows-1 or c == 0 or c == columns-1):
                    board[r][c] = "X"
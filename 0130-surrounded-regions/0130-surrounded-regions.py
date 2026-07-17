from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 1 and board[0][0] == "O":
            return

        rows = len(board)
        columns = len(board[0])
        queue = deque()
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        for r in range(rows):
            if board[r][0] == "O":
                queue.append((r,0))
                visited.add((r,0))
            if board[r][columns-1] == "O":
                queue.append((r,columns-1))
                visited.add((r,columns-1))

        for c in range(columns):
            if board[0][c] == "O":
                visited.add((0,c))
                queue.append((0,c))
            if board[rows-1][c] == "O":
                visited.add((rows-1,c))
                queue.append((rows-1,c))
        
        def bfs(queue, visited):
            while queue:
                row, column = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] == "O" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        
        bfs(queue, visited)

        for r in range(rows):
            for c in range(columns):
                if not (r != 0 or r != rows-1) and not (c != 0 or c != columns-1) or (r,c) not in visited:
                    board[r][c] = "X"
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        columns = len(board[0])

        def dfs(r,c,index):
            if index >= len(word):
                return True
            
            if not (0 <= r < rows) or not (0 <= c < columns) or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r+1,c,index+1)
                or
                dfs(r-1,c,index+1)
                or
                dfs(r,c+1,index+1)
                or
                dfs(r,c-1,index+1)
            )

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False
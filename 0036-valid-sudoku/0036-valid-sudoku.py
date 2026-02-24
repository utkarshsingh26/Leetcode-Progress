class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows
        for r in range(9):
            seen = set()
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in seen:
                    return False
                else:
                    seen.add(value)
        
        # columns

        for c in range(9):
            seen = set()
            for r in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in seen:
                    return False
                else:
                    seen.add(value)
        
        # smaller sqaures
        start = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for i,j in start:
            seen = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    value = board[r][c]

                    if value == ".":
                        continue

                    if value in seen:
                        return False
                    else:
                        seen.add(value)
        
        # all else passed
        return True
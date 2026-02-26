class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = []

        for i in range(n+1):
            binary = bin(i).count('1')
            result.append(binary)
        
        return result
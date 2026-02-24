class Solution:
    def hammingWeight(self, n: int) -> int:
        
        answer = bin(n).count('1')
        return answer
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binary = bin(n).count('1')
        
        return binary
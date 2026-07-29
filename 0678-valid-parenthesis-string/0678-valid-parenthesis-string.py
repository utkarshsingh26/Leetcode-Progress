class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftMin = 0 #(
        leftMax = 0

        for char in s:
            if char == "(":
                leftMin += 1
                leftMax += 1
            elif char == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1 # consider that * = )
                leftMax += 1 # consider that * = (

            if leftMax < 0:
                return False # we opened way too many (
                
            if leftMin < 0:
                leftMin = 0
        
        return leftMin == 0
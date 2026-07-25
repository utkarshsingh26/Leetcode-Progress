class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        result = []
        temp = []

        dictionary = {
            "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
            "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"
        }

        def backtrack(index):
            if index == len(digits):
                result.append("".join(temp[:]))
                return
            
            for char in dictionary[digits[index]]:
                temp.append(char)
                backtrack(index+1)
                temp.pop()
        
        backtrack(0)
        return result
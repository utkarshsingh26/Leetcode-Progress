class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        smallest = strs[0]

        for s in strs[1:]:
            smallest = smallest if len(smallest) < len(s) else s
        
        prefix = ""

        for i in range(len(smallest)):
            for word in strs:
                if smallest[i] != word[i]:
                    return prefix
            prefix += smallest[i]
        
        return prefix
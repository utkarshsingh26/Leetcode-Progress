class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        smallest = strs[0]

        for s in strs[1:]:
            if len(s) < len(smallest):
                smallest = s
        
        prefix = ""

        for i in range(len(smallest)):
            for word in strs:
                if smallest[i] != word[i]:
                    return prefix
            prefix += smallest[i]
        
        return prefix
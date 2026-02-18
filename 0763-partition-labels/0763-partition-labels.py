class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        result = []
        lastIndex = {}

        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        start = 0
        end = 0

        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])

            if i == end:
                length = (end - start) + 1
                start = i + 1
                result.append(length)
        
        return result
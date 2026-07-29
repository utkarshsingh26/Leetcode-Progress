class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        result = []

        end_map = {}
        for i in range(len(s)):
            end_map[s[i]] = i

        start = 0
        end = 0

        for i in range(len(s)):
            end = max(end, end_map[s[i]])

            if i == end:
                length = (end - start) + 1
                result.append(length)
                start = i + 1
        
        return result
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        result = []

        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            
            if interval[0] <= result[-1][1]:
                result[-1][0] = min(result[-1][0], interval[0])
                result[-1][1] = max(result[-1][1], interval[1])
        
        return result
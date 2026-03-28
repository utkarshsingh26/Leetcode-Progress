class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x:x[0])

        for interval in intervals:
            if not result:
                result.append(interval)
            
            if result[-1][1] >= interval[0]:
                result[-1][0] = min(result[-1][0], interval[0])
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        
        return result
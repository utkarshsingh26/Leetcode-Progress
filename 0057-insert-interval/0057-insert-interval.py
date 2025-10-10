class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals = intervals + [newInterval]
        intervals.sort()
        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
            if interval[0] <= result[-1][1]:
                result[-1][0] = min(result[-1][0], interval[0])
                result[-1][1] = max(result[-1][1],interval[1])
            else:
                result.append(interval)
        
        return result

        
            
        
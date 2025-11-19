class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals = intervals + [newInterval]
        intervals.sort(key=lambda x:x[0])
        result = []

        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
            else:
                start = result[-1][0]
                end = result[-1][1]

                if interval[0] <= end:
                     result[-1][0] = min(result[-1][0], interval[0])
                     result[-1][1] = max(result[-1][1], interval[1])
                else:
                    result.append(interval)
        
        return result


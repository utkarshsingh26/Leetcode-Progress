class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])
        count = 0
        start = intervals[0][0]
        end = intervals[0][1]

        for interval in intervals[1:]:
            if not (end <= interval[0]):
                count += 1
            else:
                start = interval[0]
                end = interval[1]
        
        return count
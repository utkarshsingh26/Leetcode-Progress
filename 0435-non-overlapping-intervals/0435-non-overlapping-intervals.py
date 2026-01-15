class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count = 0
        intervals.sort(key=lambda x:x[1])

        start = intervals[0][0]
        end = intervals[0][1]

        print(intervals)

        for interval in intervals[1:]:
            if end <= interval[0]:
                start = interval[0]
                end = interval[1]
            else:
                count += 1

        return count
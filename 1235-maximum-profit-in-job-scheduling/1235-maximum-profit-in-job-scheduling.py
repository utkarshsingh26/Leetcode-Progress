class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def recursive(i):
            if i == len(intervals):
                return 0
            
            if i in cache:
                return cache[i]
            
            # exclude
            result1 = recursive(i+1)

            # include
            # j = i+1
            # while j < len(intervals) and intervals[i][1] > intervals[j][0]:
            #     j += 1
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            result2 = intervals[i][2] + recursive(j)

            cache[i] = result = max(result1, result2)

            return result
        
        return recursive(0)
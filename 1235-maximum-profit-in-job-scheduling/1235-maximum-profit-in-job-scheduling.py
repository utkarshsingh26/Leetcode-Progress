class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = sorted(zip(startTime, endTime, profit))
        cache = {}
        
        def recursive(i):
            if i == len(jobs):
                return 0
            
            if i in cache:
                return cache[i]
            
            # don't take the job
            result1 = recursive(i+1)

            # take the job
            # j = i+1
            # while j < len(jobs) and jobs[i][1] > jobs[j][0]:
            #     j += 1
            j = bisect.bisect_right(jobs, (jobs[i][1], -1, -1))
            result2 = jobs[i][2] + recursive(j)

            # return the result
            result = max(result1, result2)
            cache[i] = result
            return result
        
        return recursive(0)
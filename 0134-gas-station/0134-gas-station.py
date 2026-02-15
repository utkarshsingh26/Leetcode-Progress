class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        total_sum = 0

        for i in range(len(gas)):
            interim_sum = gas[i] - cost[i]
            total_sum += interim_sum

            if total_sum < 0:
                total_sum = 0
                start = i+1
        
        return start
            
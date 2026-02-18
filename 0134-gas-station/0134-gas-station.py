class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        summ = 0

        for i in range(len(gas)):
            summ += gas[i] - cost[i]

            if summ < 0:
                summ = 0
                start = i + 1
        
        return start
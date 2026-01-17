class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        station = 0
        difference = 0

        for i in range(len(gas)):

            difference += gas[i] - cost[i]

            if difference < 0:
                difference = 0
                station = i + 1
        
        return station
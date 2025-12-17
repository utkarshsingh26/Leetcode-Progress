class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            current_temp = temperatures[i]

            while stack and current_temp > temperatures[stack[-1]]:
                popped = stack.pop()
                prev_day = popped
                result[prev_day] = i - prev_day
            
            stack.append(i)
        
        return result
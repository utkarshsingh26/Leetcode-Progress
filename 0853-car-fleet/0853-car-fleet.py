class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort(key=lambda x:x[0], reverse=True)

        stack = []

        for position, speed in cars:
            time = (target - position) / speed

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
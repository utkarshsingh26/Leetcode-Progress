class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = [1] * len(height)
        right = [1] * len(height)
        result = [1] * len(height)
        water = 0
        
        left[0] = height[0]
        right[-1] = height[-1]

        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i])
        
        
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        print(left)
        print(right)

        for i in range(len(height)):
            result[i] = min(left[i], right[i]) - height[i]

            if result[i] > 0:
                water += result[i]
        
        return water
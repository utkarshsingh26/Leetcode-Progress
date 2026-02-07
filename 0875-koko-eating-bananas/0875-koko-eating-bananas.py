class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        answer = piles[-1]
        
        def totalEaten(x):
            answer = 0
            for pile in piles:
                answer += math.ceil(float(pile)/x)
            return answer
        
        left = 1
        right = piles[-1]

        while left <= right:
            mid = (left + right) // 2

            if totalEaten(mid) <= h:
                answer = mid
                right = mid  - 1
            else:
                left = mid + 1
        
        return answer
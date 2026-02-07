class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        answer = right

        def hoursEaten(n):
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/n)
            return hours
        
        while left <= right:
            mid = (left + right)//2

            if hoursEaten(mid) <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
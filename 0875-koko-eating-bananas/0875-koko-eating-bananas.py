class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        left = 1
        right = piles[-1]
        result = piles[-1]

        def hours_taken(num):
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/num)
            return hours

        while left <= right:
            mid = (left + right) // 2

            if hours_taken(mid) <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
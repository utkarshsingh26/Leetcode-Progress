class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        result = piles[-1]

        def hoursNeeded(num):
            result = 0

            for pile in piles:
                result += math.ceil(float(pile)/num)

            return result

        left = 1
        right = piles[-1]

        while left <= right:
            mid = (left + right) // 2

            if hoursNeeded(mid) <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result

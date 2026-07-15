class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        answer = right

        def hoursTaken(mid):
            count = 0
            for pile in piles:
                count += (math.ceil(int(pile)/mid))
            return count

        while left <= right:
            mid = (left + right) // 2

            if hoursTaken(mid) <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer


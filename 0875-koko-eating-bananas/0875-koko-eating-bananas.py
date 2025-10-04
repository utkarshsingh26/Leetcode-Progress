class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        answer = max(piles)

        left = 1
        right = max(piles)

        def checkForHours(number):
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/number)
            return hours

        while left < right:
            mid = (left + right) // 2

            check = checkForHours(mid)

            if check <= h:
                right = mid
                answer = mid
            else:
                left = mid + 1

        return answer
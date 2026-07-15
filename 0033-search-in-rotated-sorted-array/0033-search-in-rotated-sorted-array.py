class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] == target:
            return left
        
        if left == 0:
            return binarySearch(nums, target)
        else:
            left_half = nums[:left]
            right_half = nums[left:]
            
            if left_half[0] <= target <= left_half[-1]:
                return binarySearch(left_half, target)
            elif right_half[0] <= target <= right_half[-1]:
                temp_answer = binarySearch(right_half, target)
                return -1 if temp_answer == -1 else temp_answer + left
            else:
                return -1
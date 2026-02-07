class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(nums, target):
            left = 0
            right = len(nums)-1

            while left <= right:
                mid = (left + right)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        minIndex = left
        minElement = nums[minIndex]

        if target == minElement:
            return minIndex
        
        if minIndex == 0:
            return binarySearch(nums, target)
        else:
            if nums[0] <= target <= nums[minIndex-1]:
                arr = nums[:minIndex]
                return binarySearch(arr, target)
            else:
                arr = nums[minIndex:]
                answer = binarySearch(arr, target)
                return -1 if answer == -1 else answer + minIndex

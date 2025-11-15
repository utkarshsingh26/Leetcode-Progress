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
                elif nums[mid] > target:
                    right = mid - 1
            
            return -1
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        
        minNum = nums[left]
        minIndex = left

        if target == minNum:
            return minIndex
        
        if minIndex == 0:
            return binarySearch(nums, target)
        else:
            
            if nums[0] <= target <= nums[minIndex-1]:
                arr = nums[:minIndex]
                return binarySearch(arr, target)
            elif nums[minIndex] <= target <= nums[-1]:
                arr = nums[minIndex:]
                result = binarySearch(arr, target)
                return result + minIndex if result != -1 else -1
            else:
                return -1

                
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
                    print("here")
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
        
        smallest = nums[left]
        indexOfSmallest = left
        
        if smallest == target:
            return indexOfSmallest
        
        if indexOfSmallest == 0:
            return binarySearch(nums, target)
        
        if nums[indexOfSmallest] <= target <= nums[-1]:
            arr = nums[indexOfSmallest:]
            answer = binarySearch(arr, target)
            return -1 if answer == -1 else answer + indexOfSmallest
        elif nums[0] <= target <= nums[indexOfSmallest-1]:
            arr = nums[:indexOfSmallest]
            return binarySearch(arr, target)
        else:
            return -1
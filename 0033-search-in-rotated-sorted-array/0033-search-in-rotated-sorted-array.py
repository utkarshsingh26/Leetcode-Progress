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
        
        minIndex = left
        minElement = nums[left]

        if minElement == target:
            return minIndex
        
        if minElement < target <= nums[-1]:
            arr = nums[minIndex:]
            answer = binarySearch(arr, target)
            if answer != -1:
                answer += minIndex
                return answer
            else:
                return answer
        elif nums[0] <= target <= nums[minIndex-1]:
            arr = nums[:minIndex]
            return binarySearch(arr, target)
        else:
            return -1
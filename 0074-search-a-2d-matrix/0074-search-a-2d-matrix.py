class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            
            return False
        
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binarySearch(matrix[mid], target)
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
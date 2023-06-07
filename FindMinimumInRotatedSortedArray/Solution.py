class Solution:
    def findMin(self, nums: list[int]) -> int:
        #  left and right bounds of the array
        left: int = 0
        right: int = len(nums)-1

        while left != right:
            mid: int = left + (right - left)//2

            if nums[mid] <= nums[right] and nums[mid] >= nums[left]:
                # this array is sorted
                return nums[left]

            if nums[mid] <= nums[right]:
                # nums[mid] is in the right sorted
                right = mid

            if nums[mid] >= nums[left]:
                # nums[mid] is in the left sorted
                left = mid + 1
        
        return nums[left]
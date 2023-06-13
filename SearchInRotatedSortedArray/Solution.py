class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # initialize pointers to the end
        left = 0
        right = len(nums)-1
        result = -1

        if len(nums) == 1:
            return 0 if target == nums[0] else result

        # while our pointers haven't converged
        while left < right:
            mid = left + (right - left)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[left] and nums[mid] < nums[right]:
                # regular binary search on sorted array
                if target >= nums[mid]:
                    left = mid
                else:
                    right = mid

            if nums[mid] > nums[left]:
                # nums[mid] is part of left sorted array
                if nums[mid] <= target  and target >= nums[left]:
                    # target is in this left sorted array
                    right = mid
                else:
                    left = mid

            if nums[mid] < nums[right]:
                # nums[mid] is part of right sorted array
                if nums[mid] <= target and target <= nums[right]:
                    left = mid if left != mid else mid + 1
                elif target > nums[right]:
                    return -1
                else:
                    right = mid
        
        return left if nums[left] == target else result
        


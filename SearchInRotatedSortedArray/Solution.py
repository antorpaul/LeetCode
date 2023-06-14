class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # initialize pointers to the end
        left, right = 0, len(nums)-1
        result = -1

        if len(nums) == 1:
            return 0 if target == nums[0] else result

        # while our pointers haven't converged
        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid
            
            if left == right:
                return left if target == nums[left] else -1
            
            if nums[left] < nums[mid] and nums[mid] < nums[right]:
                # regular binary search on sorted array
                if target > nums[mid]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[left] <= nums[mid]:
                    # we are in the left sorted
                    # ..but nums[mid] may not be pivot
                    if nums[left] <= target and target < nums[mid]:
                        # look to the right of mid in left sorted
                        right = mid
                    else:
                        left = mid+1

                if nums[right] >= nums[mid]:
                    # we are in the right sorted
                    # ..but nums[mid] may not be pivot
                    if nums[mid] < target and target <= nums[right]:
                        left = mid+1
                    else:
                        right = mid-1
        
        return left if nums[left] == target else result
        


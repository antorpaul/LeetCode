class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # remove val and replace with -1 to serve as flag
        k = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums[i] = -1
                k += 1

        shift = 0
        for i in range(0, len(nums)):
            if nums[i] == -1:
                shift += 1
            else:
                nums[i-shift] = nums[i]
        
        return len(nums) - k
    
    def removeElementTwoPointers(self, nums: list[int], val: int) -> int:
        # establish 2 pointers
        i = 0
        j = 0

        # pointers will both traverse, but one will stall when we reach val
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

print("My First solution:")
sol = Solution()
array = [0, 1, 2, 2, 3, 0, 2, 4]
k = sol.removeElement(array, 2)
print("k = {}, nums = {}".format(k, array[0:k]))

print("LC Sponsored Solution:")
sol = Solution()
array2 = [0, 1, 2, 2, 3, 0, 2, 4]
k = sol.removeElementTwoPointers(array2, 2)
print("k = {}, nums = {}".format(k, array2[0:k]))
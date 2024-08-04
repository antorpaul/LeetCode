from typing import List
import math

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        # find the first decreasing element from the right
        fd_index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                fd_index = i
                break

        # if no such element is found, the array is in descending order
        if fd_index == -1:
            nums.reverse()
            return

        # find the smallest element to the right of fd_index that is larger than nums[fd_index]
        for i in range(n - 1, fd_index, -1):
            if nums[i] > nums[fd_index]:
                # swapping elements can be done via tuple unpacking
                # since python internally creates a tuple (nums[i], nums[fd_index])
                # and then unpacks it so there is no need for a temp
                nums[fd_index], nums[i] = nums[i], nums[fd_index]
                break

        # Reverse the subarray from fd_index + 1 to the end
        nums[fd_index + 1:] = reversed(nums[fd_index + 1:])



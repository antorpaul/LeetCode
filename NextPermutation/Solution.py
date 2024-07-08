from typing import List
import math

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        bestSwap = -1
        bestSwap_i = -1
        bestSwap_j = -1

        while j >= i:
            currentSwap = Solution.evaluateSwap(nums, i, j)
            if currentSwap > 0:
                if bestSwap < 0:
                    bestSwap = currentSwap
                bestSwap = min(currentSwap, bestSwap)
                if bestSwap == currentSwap:
                    bestSwap_i = i
                    bestSwap_j = j
            if i < j:
                i += 1
            else:
                if bestSwap > 0:
                    break
                j -= 1
            
        if bestSwap_i == -1 or bestSwap_j == -1:
            nums.sort()
        else:
            temp = nums[bestSwap_j]
            nums[bestSwap_j] = nums[bestSwap_i]
            nums[bestSwap_i] = temp
            nums[bestSwap_i+1:] = sorted(nums[bestSwap_i+1:]) 

    
    def evaluateSwap(nums: List[int], i, j):
        return math.pow(10, j - i) * (nums[j] - nums[i])

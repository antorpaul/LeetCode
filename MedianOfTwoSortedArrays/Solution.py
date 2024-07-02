import math
from typing import List
from math import ceil

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      # Initial Solution takeaways...
      # - While loop does not have a stop condition so it keeps going indefinitely
      # - Lack of clarity in the logic... cluttered and hard to understand
      # Partition the array into left and right portions
      total_len = len(nums2) + len(nums1)
      half = total_len // 2
      
      i = 0
      j = 0
      while j < len(nums2) and j < half//2:
         j += 1
      i = half - j

      while i < len(nums1) and j < len(nums2):
         if i+1 < len(nums1):
            if nums1[i] <= nums1[i+1]:
               continue
            else:
               j -= 1
         if j+1 < len(nums2):
            if nums2[j] <= nums2[j+1]:
               continue
            else:
               i -= 1
      
      if total_len % 2 != 0:
         return math.min(nums1[i], nums2[j])
      else:
         return (nums1[i] + nums2[i])/2.0

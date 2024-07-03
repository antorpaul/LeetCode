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
        total_size = len(nums1) + len(nums2)
        half = total_size//2

        l = 0
        r = len(nums2) - 1

        # feels like i should use binary search here
        while l <= r:
            m = (l + r)//2
            ind = (half - 1) - (m+1)
            if nums2[m] < nums1[ind+1]:
                if total_size % 2 != 0:
                    return min(nums1[ind], nums2[m+1])
                else:
                    return (nums1[ind] + nums2[m+1])/2
            else:
                r -= 1
        return 0
            


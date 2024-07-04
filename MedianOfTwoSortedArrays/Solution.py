import math
from typing import List
from math import ceil
from timeout_decorator import timeout, TimeoutError

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
    # @timeout(10)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_size = len(nums1) + len(nums2)
        half = total_size//2

        l = 0
        r = len(nums2) - 1
        m = (l + r)//2
        n = min(half - (m+1) - 1, len(nums1)-1)
        # if m > 0:
        #     # m+1 is the number of elements we have from nums2
        #     # we need half-(m+1) # of elements from nums1
        #     n = min(half - (m+1) - 1, len(nums1)-1)
        # else:
        #     n = min(half - 1, len(nums1)-1)
        # [1 2] 
        # [3 4] m = 0 + 1 // 2 = 0

        # [1 2]
        # [1] m = 0 + 0 //2 = 0

        # [1 2]
        # [] m = 0 + (-1) // 2 = -1

        # lmax => max value for the left partition
        # rmax => max value for the right partition
        # important for out of bounds checking
        n1_lmax = -1 * math.inf
        n2_lmax = -1 * math.inf
        n2_rmin = math.inf
        n1_rmin = math.inf

        while r >= l:
            if n+1 < len(nums2):
                n2_rmin = nums2[n+1]
            if m+1 < len(nums1):
                n1_rmin = nums1[m+1]
            if n > 0:
                n2_lmax = nums2[n]
            if m > 0:
                n1_lmax = nums1[m]
                
            if n2_lmax > n1_rmin:
                m -= 1
                n += 1
                continue
            elif n1_lmax > n2_rmin:
                m += 1
                n -= 1
                continue
                    
            if total_size % 2 == 0:
                return (max(n2_lmax, n1_lmax) + min(n2_rmin, n1_rmin))/2
            else: 
                if m+1 > len(nums2) - 1 or n+1 > len(nums1) - 1:
                    return min(n1_lmax, n2_lmax)
                else:
                    return min(n2_rmin, n1_rmin) 

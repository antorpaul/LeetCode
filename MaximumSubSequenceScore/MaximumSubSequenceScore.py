import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # create an array of tuples (nums2[i], nums1[i]) sorted by nums2[i]
        sortedTuples = [(nums1[i], nums2[i]) for i in range(0, len(nums2))]
        sortedTuples = sorted(sortedTuples, key=lambda p: p[1], reverse=True)

        minHeap = []
        result = 0
        n1Sum = 0

        # go through sortedTuples maximizing subscore in a greedy way
        for n1, n2 in sortedTuples:
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                # remove a value
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop
                
            if len(minHeap) == k:
                result = max(result, n1Sum * n2)

        return result
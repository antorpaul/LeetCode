import pytest

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        answer: list = [1 for i in range(len(nums))]

        # prefix array 
        # (1 more than len(nums) to account for first and last element)
        prefix: list = [1 for i in range(len(nums))]
        for i in range(0, len(nums)):
            prefix[i] = nums[i]*prefix[i-1]

        # postfix array
        postfix: list = [1 for i in range(len(nums))]
        for i in range(1, len(nums)+1):
            postfix[i-1] = nums[-i]*postfix[i-2]
        postfix.reverse()
        
        for i in range(len(nums)):
            prev = 1 if i-1 < 0 else prefix[i-1]
            next = 1 if i+1 >= len(nums) else postfix[i+1]
            answer[i] = prev * next
            
        return answer


def testProductOfArrayAndSelf():
    sol: Solution = Solution()
    testOne = sol.productExceptSelf([1, 2, 3, 4])
    testTwo = sol.productExceptSelf([-1,1,0,-3,3])
    assert(testOne == [24,12,8,6])
    assert(testTwo == [0,0,9,0,0])

if __name__ == '__main__':
    testProductOfArrayAndSelf()
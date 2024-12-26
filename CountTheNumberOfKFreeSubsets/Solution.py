from typing import List
from collections import defaultdict

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups = defaultdict(list)
        for x in nums:
            # defaultdict ensures that if x%k doesn't exist, we will start with an empty list
            groups[x % k].append(x)
        
        count = 1
        for g in groups.values():
            if len(g) == 1:
                count *= 2
            else:
                dp = [0 for i in range(0, len(g) + 1)]
                dp[0] = 1
                dp[1] = 2
                # since we grouped by modulo, consecutive numbers do not necessarily subtract to k
                for i in range(2, len(g) + 1):
                    if abs(g[i-1] - g[i-2]) == k:
                        dp[i] = dp[i-1] + dp[i-2]
                    else:
                        # if they do not subtract to k, we can just multiply by 2 each time
                        dp[i] = dp[i-1]*2
                count *= dp[-1]
        
        return count

nums = [968,969,970,964,967,972,971,963]
k = 1
sol = Solution()
print(sol.countTheNumOfKFreeSubsets(nums, k))
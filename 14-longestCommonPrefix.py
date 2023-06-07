class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = strs[0]
        results = {}
        longest = ""

        # find the shortest string
        for i in range(0, len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]

        for i in range(0, len(strs)):
            j = 0
            while strs[i][0:j] == shortest[0:j] and j <= len(strs[i]):
                prefix = shortest[0:j]
                if prefix in results.keys():
                    results[prefix] += 1
                else:
                    results[prefix] = 0
                j += 1
        
        maxOccurences = max(results.values())
        for k, v in results.items():
            if v == maxOccurences and longest == "":
                longest = k
            
            if v == maxOccurences and len(k) > len(longest):
                longest = k

        return longest

print("My First solution:")
sol = Solution()
caseOne = ["flow","flower","flight"]
caseTwo = ["dog","racecar","car"]
k = sol.longestCommonPrefix(caseOne)
print("k = {}".format(k))
k = sol.longestCommonPrefix(caseTwo)
print("k = {}".format(k))

print("LC Sponsored Solution:")
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     end: int = 1
    #     if s == "":
    #         return 0
        
    #     # so far we will have at least 1 entry
    #     encountered: list = [s[0]]
    #     result: int = 1

    #     while end < len(s):
    #         currChar = s[end]
    #         if currChar not in encountered:
    #             encountered.append(currChar)
    #             end += 1
    #             result = max(len(encountered), result)
    #         else:
    #             encountered = encountered[encountered.index(currChar) + 1:]
        
    #     return result
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        encountered: set = set()
        result: int = 0

        for end in range(len(s)):
            # make sure we don't consider duplicates
            while s[end] in encountered:
                encountered.remove(s[start])
                start += 1
            encountered.add(s[end])
            result = max(result, end-start + 1)
            
        
        return result
            
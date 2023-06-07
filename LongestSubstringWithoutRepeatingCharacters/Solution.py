class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start: int = 0
        end: int = 1
        result: int = 0
        encountered: dict = {s[start]: start}

        while end < len(s):
            if s[end] not in encountered.keys():
                encountered[s[end]] = end
                end += 1
            else:
                result = max(len(encountered.keys()), result)
                start = encountered[s[end]] + 1
                del encountered[s[end]]
        
        return result
            
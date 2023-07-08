class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters: dict = {}
        left, right = 0, 0
        result = 0
        subs = 0

        # go through the loop
        while right < len(s):
            substringLength = right - left
            if characters.get(s[right]) is None:
                characters[s[right]] = 1
            else:
                characters[s[right]] += 1
            
            # get the most common character
            mostCommonCharacter = ""
            occurances = 0
            for key, val in characters.items():
                occurances = max(val, occurances)
                if val == max(occurances, val):
                    mostCommonCharacter = key
            
            # get the number of substitutions
            # by counting all of the characters 
            # that aren't the most common character
            subs = substringLength - occurances
            
            if subs <= k:
                right += 1
                result = max(substringLength, result)
            else:
                left += 1

        return result
            


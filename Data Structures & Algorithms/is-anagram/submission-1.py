class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency_s = {}
        frequency_t = {}

        for char in s:
            if char in frequency_s:
                frequency_s[char] += 1
            else:
                frequency_s[char] = 1

        for char in t:
            if char in frequency_t:
                frequency_t[char] += 1
            else:
                frequency_t[char] = 1

        return frequency_s == frequency_t
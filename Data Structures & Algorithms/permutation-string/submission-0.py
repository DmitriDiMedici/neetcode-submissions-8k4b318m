class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_letters = {}
        s2_letters = {}

        for letter in s1:
            s1_letters[letter] = 1 + s1_letters.get(letter, 0)

        for i in range(len(s1)):
            s2_letters[s2[i]] = 1 + s2_letters.get(s2[i], 0)

            if s1_letters == s2_letters:
                return True

        for i in range(len(s1), len(s2)):
            s2_letters[s2[i]] = 1 + s2_letters.get(s2[i], 0)
            char_out = s2[i - len(s1)]
            s2_letters[char_out] -= 1

            if s2_letters[char_out] == 0:
                del s2_letters[char_out]

            if s1_letters == s2_letters:
                return True

        return False
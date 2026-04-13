class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_anagrams = {}

        for word in strs:
            letter_count = [0] * 26

            for char in word:
                position = ord(char) - ord("a")
                letter_count[position] += 1

            key = tuple(letter_count)
            group_anagrams.setdefault(key, []).append(word)

        return list(group_anagrams.values())
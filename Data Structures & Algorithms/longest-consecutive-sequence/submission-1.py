class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers = set(nums)
        current_length = 0
        max_length = 0

        for num in numbers:
            if num - 1 not in numbers:
                current_length = 1
                current_num = num
                while current_num + 1 in numbers:
                    current_num += 1
                    current_length += 1

                if current_length > max_length:
                    max_length = current_length

        return max_length
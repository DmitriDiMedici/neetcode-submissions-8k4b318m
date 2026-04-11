class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in seen:
                return [seen[difference], index]
            else:
                seen[value] = index
        
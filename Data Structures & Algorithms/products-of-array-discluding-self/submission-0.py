class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        suffix = [1] * len(nums)
        res = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(nums[i - 1] * prefix[i - 1])

        for j in reversed(range(len(nums) - 1)):
            suffix[j] = suffix[j + 1] * nums[j + 1]

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res
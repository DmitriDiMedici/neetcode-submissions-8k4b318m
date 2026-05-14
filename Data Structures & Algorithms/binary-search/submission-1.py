class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int(len(nums) / 2)

        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
                mid = int((left + right) / 2)
            else:
                left = mid + 1
                mid = int((left + right) / 2)

        return -1
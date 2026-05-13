class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        greaters = {}
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                number = stack.pop()
                greaters[number] = nums2[i]
            stack.append(nums2[i])

        res = [greaters.get(num, -1) for num in nums1]

        return res
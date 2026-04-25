class Solution:
    def trap(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_left = height[i]
        max_right = height[j]
        trapped_water = 0

        while i < j:
            if max_left < max_right:
                i += 1
                max_left = max(max_left, height[i])
                trapped_water += max_left - height[i]
            else:
                j -= 1
                max_right = max(max_right, height[j])
                trapped_water += max_right - height[j]

        return trapped_water
        
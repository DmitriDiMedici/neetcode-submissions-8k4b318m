class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            current_area = (j - i) * min(heights[i], heights[j])

            if current_area > max_area:
                max_area = current_area

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area
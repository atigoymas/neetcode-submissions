class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1
        while l < r:
            length = min(heights[l], heights[r])
            width = r - l
            ans = max(ans, length*width)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans

        
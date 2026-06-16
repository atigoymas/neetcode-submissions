class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i, val in enumerate(heights):
            start = i
            while stack and stack[-1][1] > val:
                tmp_idx, tmp_val = stack.pop()
                ans = max(ans, tmp_val*(i-tmp_idx))
                start = tmp_idx
            stack.append((start, val))

        for i, h in stack:
            ans = max(ans, h*(len(heights) - i))
        return ans


        
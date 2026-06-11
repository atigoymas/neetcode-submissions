class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = ''
        maxL = 1
        length = 1
        l, r = 0, 0
        while r < len(s):
            if s[r] not in ans:
                ans += s[r]
                print(ans)
                length = max(length, len(ans))
                r += 1
            else:
                l += 1
                r = l
                length = 0
                ans = ''
            maxL = max(maxL, length)
        return maxL
            


        
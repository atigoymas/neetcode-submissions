class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        mp = {}
        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            while (r-l+1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

            
            
            



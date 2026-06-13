class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1)-1
        mp = {}
        for i in s1:
            mp[i] = 1 + mp.get(i, 0)
        mp2 = {}
        for j in range(len(s1)):
            mp2[s2[j]] = 1 + mp2.get(s2[j], 0)
        
        if mp == mp2:
            return True

        while r < len(s2)-1:
            mp2[s2[l]] -= 1
            if mp2[s2[l]] == 0:
                del mp2[s2[l]]
            l += 1
            r += 1
            mp2[s2[r]] = 1 + mp2.get(s2[r], 0)

            if mp == mp2:
                return True
                
        return False


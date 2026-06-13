class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}
        window = {}

        l, formed = 0, 0
        res = (float("inf"), 0, 0)

        for i in t:
            need[i] = 1 + need.get(i, 0)
        
        required = len(need)
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in need and window[c] == need[c] :
                    formed += 1

            while formed == required:
                if (r-l+1) < res[0]:
                    res = (r-l+1, l, r)
            
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                l+= 1
                    
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]


        

        
        
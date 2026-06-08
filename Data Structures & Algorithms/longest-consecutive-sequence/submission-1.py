class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not(nums): 
            return 0
        lcs = 1
        ans = 1

        srt_nums = list(sorted(set(nums)))
        
        for i in range(1, len(srt_nums)):
            if 1 + srt_nums[i-1] == srt_nums[i]:
                lcs += 1
            else: 
                lcs = 1
            ans = max(ans, lcs)
        return ans
            
            

        
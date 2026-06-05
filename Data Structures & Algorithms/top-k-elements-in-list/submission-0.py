class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
        for key, val in mp.items():
            freq[val].append(key)
        
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        